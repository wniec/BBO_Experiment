from itertools import product

from pypop7.optimizers.core import Optimizer
from pypop7.optimizers.es.lmcma import LMCMA  # noqa
from pypop7.optimizers.es.mmes import MMES  # noqa
from pypop7.optimizers.es.ddcma import DDCMA  # noqa
from pypop7.optimizers.es.lmmaes import LMMAES  # noqa
from pypop7.optimizers.es.rmes import RMES  # noqa
from pypop7.optimizers.es.r1es import R1ES  # noqa
from pypop7.optimizers.es.lmcmaes import LMCMAES  # noqa
from pypop7.optimizers.es.fmaes import FMAES  # noqa
from pypop7.optimizers.es.maes import MAES  # noqa
from pypop7.optimizers.es.ccmaes2016 import CCMAES2016  # noqa
from pypop7.optimizers.es.ccmaes2009 import CCMAES2009  # noqa
from pypop7.optimizers.es.opoa2010 import OPOA2010  # noqa
from pypop7.optimizers.es.opoa2015 import OPOA2015  # noqa
from pypop7.optimizers.es.opoc2006 import OPOC2006  # noqa
from pypop7.optimizers.es.opoc2009 import OPOC2009  # noqa
from pypop7.optimizers.es.sepcmaes import SEPCMAES  # noqa
from pypop7.optimizers.es.cmaes import CMAES  # noqa
from pypop7.optimizers.es.samaes import SAMAES  # noqa
from pypop7.optimizers.es.saes import SAES  # noqa
from pypop7.optimizers.es.csaes import CSAES  # noqa
from pypop7.optimizers.es.dsaes import DSAES  # noqa
from pypop7.optimizers.es.ssaes import SSAES  # noqa
from pypop7.optimizers.es.res import RES  # noqa

from pypop7.optimizers.eda.rpeda import RPEDA  # noqa
from pypop7.optimizers.eda.aemna import AEMNA  # noqa
from pypop7.optimizers.eda.emna import EMNA  # noqa
from pypop7.optimizers.eda.umda import UMDA  # noqa

from pypop7.optimizers.nes.r1nes import R1NES  # noqa
from pypop7.optimizers.nes.snes import SNES  # noqa
from pypop7.optimizers.nes.xnes import XNES  # noqa
from pypop7.optimizers.nes.enes import ENES  # noqa
from pypop7.optimizers.nes.ones import ONES  # noqa
from pypop7.optimizers.nes.sges import SGES  # noqa

from pypop7.optimizers.cem.mras import MRAS  # noqa
from pypop7.optimizers.cem.dscem import DSCEM  # noqa
from pypop7.optimizers.cem.scem import SCEM  # noqa

from pypop7.optimizers.de.shade import SHADE  # noqa
from pypop7.optimizers.de.code import CODE  # noqa
from pypop7.optimizers.de.jade import JADE  # noqa
from pypop7.optimizers.de.tde import TDE  # noqa
from pypop7.optimizers.de.cde import CDE  # noqa

from pypop7.optimizers.pso.ccpso2 import CCPSO2  # noqa
from pypop7.optimizers.pso.clpso import CLPSO  # noqa
from pypop7.optimizers.pso.cpso import CPSO  # noqa
from pypop7.optimizers.pso.ipso import IPSO  # noqa
from pypop7.optimizers.pso.spso import SPSO  # noqa
from pypop7.optimizers.pso.spsol import SPSOL  # noqa

from pypop7.optimizers.cc.hcc import HCC  # noqa
from pypop7.optimizers.cc.cocma import COCMA  # noqa
from pypop7.optimizers.cc.cosyne import COSYNE  # noqa
from pypop7.optimizers.cc.coea import COEA  # noqa

from pypop7.optimizers.sa.csa import CSA  # noqa
from pypop7.optimizers.sa.nsa import NSA  # noqa
from pypop7.optimizers.sa.esa import ESA  # noqa

from pypop7.optimizers.ga.gl25 import GL25  # noqa
from pypop7.optimizers.ga.g3pcx import G3PCX  # noqa
from pypop7.optimizers.ga.genitor import GENITOR  # noqa

from pypop7.optimizers.ep.lep import LEP  # noqa
from pypop7.optimizers.ep.fep import FEP  # noqa
from pypop7.optimizers.ep.cep import CEP  # noqa

from pypop7.optimizers.ds.powell import POWELL  # noqa
from pypop7.optimizers.ds.gps import GPS  # noqa
from pypop7.optimizers.ds.nm import NM  # noqa
from pypop7.optimizers.ds.hj import HJ  # noqa
from pypop7.optimizers.ds.cs import CS  # noqa

from pypop7.optimizers.rs.bes import BES  # noqa
from pypop7.optimizers.rs.gs import GS  # noqa
from pypop7.optimizers.rs.srs import SRS  # noqa
from pypop7.optimizers.rs.arhc import ARHC  # noqa
from pypop7.optimizers.rs.rhc import RHC  # noqa
from pypop7.optimizers.rs.prs import PRS  # noqa

from pypop7.optimizers.bo.lamcts import LAMCTS  # noqa

ES_methods = [
    "RES",
    "SSAES",
    "DSAES",
    "CSAES",
    "SAES",
    "SAMAES",
    "CMAES",
    "MAES",
    "FMAES",
    "DDCMA",
    "OPOC2006",
    "SEPCMAES",
    "OPOC2009",
    "CCMAES2009",
    "OPOA2010",
    "LMCMAES",
    "OPOA2015",
    "CCMAES2016",
    "LMCMA",
    "R1ES",
    "RMES",
    "LMMAES",
    "MMES",
]
EDA_methods = ["UMDA", "EMNA", "AEMNA", "RPEDA"]
NES_methods = [
    "SGES",
    "ONES",
    "ENES",
    "XNES",
    "SNES",
    "R1NES",
    "VDCMA",
    "VKDCMA",
]
CEM_methods = ["SCEM", "DSCEM", "MRAS"]
DE_methods = ["CDE", "TDE", "JADE", "CODE", "SHADE"]
PSO_methods = ["SPSO", "SPSOL", "CPSO", "CLPSO", "IPSO", "CCPSO2"]
CC_methods = ["COEA", "HCC", "COSYNE", "COCMA"]
SA_methods = ["CSA", "ESA", "NSA"]
GA_methods = ["GENITOR", "G3PCX", "GL25"]
EP_methods = ["CEP", "FEP", "LEP"]
DS_methods = ["CS", "HJ", "NM", "GPS", "POWELL"]
RS_methods = ["PRS", "RHC", "ARHC", "SRS", "GS", "BES"]
BO_methods = ["LAMCTS"]

modules = {
    key: val
    for key, val in globals().items()
    if all((i.isupper() or i.isdigit()) for i in key)
}

methods_groups = {
    key: val
    for key, val in globals().items()
    if isinstance(val, list) and "_" in key and key[0].isupper()
}

methods2groups = {
    i: group for group, content in methods_groups.items() for i in content
}


def _get_parameter_grid() -> dict[str, dict[str, list]]:
    sigma = [0.1, 0.3, 0.6, 0.9, 1.5, 3.0]
    x = [
        []
    ]  # Placeholder value, indicates that initial x must be set according to number of dimensions
    return {
        "ES_parameters": {"sigma": sigma},
        "EDA_parameters": {},
        "NES_parameters": {"sigma": sigma},
        "CEM_parameters": {"sigma": sigma},
        "DE_parameters": {},
        "PSO_parameters": {},
        "CC_parameters": {},
        "SA_parameters": {
            "x": x,
            "sigma": sigma,
            "temperature": [20.0, 50.0, 100.0, 200.0, 500.0],
        },
        "GA_parameters": {},
        "EP_parameters": {"sigma": sigma},
        "DS_parameters": {"x": x, "sigma": sigma},
        "RS_parameters": {"x": x},
        "BO_parameters": {},
    }


def _get_params(
    opt_name: str, grid: dict[str, dict[str, list]]
) -> dict[str, list[float | int]]:
    method_group = methods2groups[opt_name]
    parameters_name = method_group.split("_")[0] + "_parameters"
    result = grid[parameters_name].copy()
    if opt_name == "CCPSO2":
        result["group_sizes"] = [[40 // i for i in [20, 10, 5, 2]]]
    if opt_name == "CPSO":
        result["n_individuals"] = [20]
    if opt_name in ["SRS", "ARHC", "RHC"]:
        result["sigma"] = [0.1, 0.3, 0.6, 0.9, 1.5, 3.0]
    if opt_name in ["RHC", "ARHC"]:
        result["temperature"] = [20.0, 50.0, 100.0, 200.0, 500.0]
    return result


def _get_optimizers() -> list[tuple[Optimizer, dict]]:
    param_grid = _get_parameter_grid()
    optimizers: list[tuple[Optimizer, dict]] = []
    for key, cls in modules.items():
        all_possible_params = _get_params(key, param_grid)
        params_names = list(all_possible_params.keys())
        for params_set in product(
            *[all_possible_params[name] for name in params_names]
        ):
            params_dict = {name: val for name, val in zip(params_names, params_set)}
            optimizers.append((cls, params_dict))

    return optimizers


optimizers = sorted(_get_optimizers(), key=lambda x: str(x))
