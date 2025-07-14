import json
import os

import cocopp
from pypop7.optimizers.core import Optimizer

from experiment import coco_bbob, average_aocc
from optimizers import optimizers
import argparse

cocopp.genericsettings.interactive_mode = False
cocopp.genericsettings.isFig = False
cocopp.genericsettings.isRLDistr = False
cocopp.genericsettings.isLogLoss = False

OPTIMIZERS_NUM = 422


def main(optimizer: Optimizer, options: dict, evaluations_multiplier):
    result_path = coco_bbob(optimizer, options, evaluations_multiplier)
    case_name = f"{optimizer.__name__}_{evaluations_multiplier}"
    dslist = cocopp.main(result_path)
    return {f"f{i.funcId}_{i.dim}": average_aocc(i) for i in dslist[(case_name, "")]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("optimizer_id", type=int, help="An Id of optimizer to use")

    args = parser.parse_args()
    optimizer_id = args.optimizer_id
    optimizer, options = optimizers[optimizer_id]
    algorithm_name = optimizer.__name__
    results_path = os.path.join("results", algorithm_name)
    if not os.path.exists(results_path):
        os.makedirs(results_path)
    # Two integer parameters passed in order to easily create a slurm array job for all tests
    if not (0 <= optimizer_id < 422):
        raise ValueError(
            f"Incorrect optimizer ID: {optimizer_id}. It must be a natural number smaller than {OPTIMIZERS_NUM}"
        )
    for evaluations_multiplier in (10, 50, 100, 500, 1_000, 5_000, 10_000):
        print(f"Testing {algorithm_name} with {evaluations_multiplier}n maximum FE.")
        result = main(optimizer, options, evaluations_multiplier)
        with open(
            os.path.join(results_path, f"{evaluations_multiplier}.json"), "w"
        ) as fp:
            json.dump(result, fp)
