import numpy as np
import cocoex  # experimentation module of `COCO`
import cocopp  # post-processing module of `COCO`
from pypop7.optimizers.core import Optimizer


def coco_bbob(
    optimizer: Optimizer,
    options: dict,
    evaluations_multiplier: int = 1_000,
    run_id: id = 0,
):
    suite, output = "bbob", f"{run_id}_{evaluations_multiplier}"
    observer = cocoex.Observer(suite, "result_folder: " + output)
    cocoex.utilities.MiniPrint()
    for function in cocoex.Suite(suite, "", ""):
        function.observe_with(observer)
        options["max_function_evaluations"] = (
            evaluations_multiplier * function.dimension
        )
        options["verbose"] = False
        if "x" in options:
            options["x"] = np.random.uniform(
                low=function.lower_bounds,
                high=function.upper_bounds,
                size=(function.dimension,),
            )
        coco_bbob_single_function(optimizer, function, options)
    return observer.result_folder


def coco_bbob_single_function(optimizer, function: cocoex.interface.Problem, options):
    problem = {
        "fitness_function": function,
        "ndim_problem": function.dimension,
        "lower_boundary": function.lower_bounds,
        "upper_boundary": function.upper_bounds,
    }
    # run black-box optimizer
    results = optimizer(problem, options).optimize()
    return results


def get_auoc(run_data: np.ndarray):
    return run_data.mean(axis=0)[0, 0]


def average_auoc(function_data: cocopp.pproc.DataSet):
    # Area under optimization curve I used that instead of constrained version, because various functions have optima
    # in different ranges, not necessarily [0, 1]
    trials = function_data.splitByTrials(whichdata="funvals")
    # average over all runs
    result = sum(get_auoc(run_data) for key, run_data in trials.items()) / len(trials)
    return result
