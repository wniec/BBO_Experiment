import os
import json
import cocopp
from experiment import coco_bbob, average_aocc
from optimizers import optimizers

cocopp.genericsettings.interactive_mode = False
cocopp.genericsettings.isFig = False
cocopp.genericsettings.isRLDistr = False
cocopp.genericsettings.isLogLoss = False


def main(name, evaluations_multiplier):
    optimizer, options = optimizers[name]
    result_path = coco_bbob(optimizer, options)
    case_name = f"{name}_{evaluations_multiplier}"
    dslist = cocopp.main(result_path)
    return {
        f'f{i.funcId}_{i.dim}': average_aocc(i) for i in dslist[(case_name, "")]
    }


if __name__ == "__main__":
    algorithm_name = "NSA"
    evaluations_multiplier = 1_000
    result = main(algorithm_name, evaluations_multiplier)
    with open(f'{algorithm_name}_{evaluations_multiplier}.json', 'w') as fp:
        json.dump(result, fp)

