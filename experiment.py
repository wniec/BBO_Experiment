import numpy as np
import cocoex  # experimentation module of `COCO`
import cocopp  # post-processing module of `COCO`
from pypop7.optimizers.core import Optimizer


def coco_bbob(optimizer: Optimizer, options: dict, evaluations_multiplier: int = 1_000):
    suite, output, results = "bbob", f"{optimizer.__name__}_{evaluations_multiplier}", None
    observer = cocoex.Observer(suite, "result_folder: " + output)
    cocoex.utilities.MiniPrint()
    for function in cocoex.Suite(suite, "", ""):
        function.observe_with(observer)
        options["max_function_evaluations"] = (
                evaluations_multiplier * function.dimension
        )
        if 'x' in options:
            options['x'] = np.random.uniform(low=function.lower_bounds, high=function.upper_bounds,
                                             size=(function.dimension,))
        coco_bbob_single_function(optimizer, function, options)
    return observer.result_folder


def coco_bbob_single_function(optimizer, function, options):
    problem = {
        "fitness_function": function,
        "ndim_problem": function.dimension,
        "lower_boundary": function.lower_bounds,
        "upper_boundary": function.upper_bounds,
    }
    # run black-box optimizer
    results = optimizer(problem, options).optimize()
    return results


def get_aocc(
        run_data: np.ndarray, lower_bound: float, upper_bound: float
):
    normalised_run = (
                             np.minimum(np.maximum(run_data, lower_bound), upper_bound) - lower_bound
                     ) / (upper_bound - lower_bound)
    return 1 - normalised_run.mean(axis=0)[0, 0]


def average_aocc(function_data: cocopp.pproc.DataSet):
    trials = function_data.splitByTrials(whichdata="funvals")
    # trials[0] - ERF
    # trials[1] - fitness
    lower_bound = 1e-08
    upper_bound = 1e2  # if dimensions <= 20 else 1e8
    # average over all runs
    result = sum(
        get_aocc(run_data, lower_bound, upper_bound)
        for key, run_data in trials.items()
    ) / len(trials)
    return result
