import json
import os
import shutil
import cocopp

from experiment import coco_bbob, average_auoc
from optimizers import optimizers
import argparse
import warnings

warnings.filterwarnings("ignore", module="cocopp.archiving")

cocopp.genericsettings.interactive_mode = False
cocopp.genericsettings.isFig = False
cocopp.genericsettings.isRLDistr = False
cocopp.genericsettings.isLogLoss = False

OPTIMIZERS_NUM = 422


def main(evaluations_multiplier, run_id):
    optimizer, options = optimizers[run_id]
    algorithm_name = optimizer.__name__
    print(f"Testing {algorithm_name} with {evaluations_multiplier}n maximum FE.")
    result_path = coco_bbob(optimizer, options, evaluations_multiplier, run_id)
    case_name = f"{run_id}_{evaluations_multiplier}"
    cocopp.genericsettings.outputdir = f"{optimizer_id}_{evaluations_multiplier}"
    dslist = cocopp.main(result_path)
    return {f"f{i.funcId}_{i.dim}": average_auoc(i) for i in dslist[(case_name, "")]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("optimizer_id", type=int, help="An Id of optimizer to use")
    parser.add_argument("output", type=str, help="A path to store results")
    args = parser.parse_args()
    optimizer_id = args.optimizer_id
    results_path = args.output
    if not os.path.exists(results_path):
        os.makedirs(results_path)
    # Two integer parameters passed in order to easily create a slurm array job for all tests
    if not (0 <= optimizer_id < 422):
        raise ValueError(
            f"Incorrect optimizer ID: {optimizer_id}. It must be a natural number smaller than {OPTIMIZERS_NUM}"
        )
    name = optimizers[optimizer_id][0].__name__ + str(optimizers[optimizer_id][1])
    os.makedirs(os.path.join(results_path, name))
    for evaluations_multiplier in (10, 50, 100, 500, 1_000, 5_000, 10_000):
        result = main(evaluations_multiplier, optimizer_id)
        with open(
            os.path.join(results_path, name, f"{evaluations_multiplier}.json"), "w"
        ) as fp:
            json.dump(result, fp)

        shutil.rmtree(os.path.join("exdata", f"{optimizer_id}_{evaluations_multiplier}"))
        shutil.rmtree(os.path.join(f"{optimizer_id}_{evaluations_multiplier}"))
