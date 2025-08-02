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

modules = {
    key: val
    for key, val in globals().items()
    if all((i.isupper() or i.isdigit()) for i in key)
}


def extract(name: str):
    splitted = name.split("{")
    cls = modules[splitted[0]]
    params = eval("{" + splitted[1])
    return cls, params


failed_optimizers = ["FEP{'sigma': 0.3}",
                     "SGES{'sigma': 3.0}",
                     'COEA{}',
                     "SGES{'sigma': 0.9}",
                     'COCMA{}',
                     "MMES{'sigma': 0.6}",
                     "MRAS{'sigma': 0.3}",
                     'RPEDA{}',
                     'AEMNA{}',
                     'GL25{}',
                     'EMNA{}',
                     "SGES{'sigma': 0.1}",
                     "FEP{'sigma': 1.5}",
                     "FEP{'sigma': 0.9}",
                     "ENES{'sigma': 0.6}",
                     "FEP{'sigma': 3.0}",
                     "CEP{'sigma': 1.5}",
                     "CEP{'sigma': 0.9}",
                     "ONES{'sigma': 3.0}",
                     "MMES{'sigma': 1.5}",
                     "SGES{'sigma': 1.5}",
                     "MMES{'sigma': 3.0}",
                     'COSYNE{}',
                     "ENES{'sigma': 0.1}",
                     "FEP{'sigma': 0.6}",
                     "DDCMA{'sigma': 0.6}",
                     "ENES{'sigma': 1.5}",
                     "LEP{'sigma': 3.0}",
                     "ONES{'sigma': 0.3}",
                     'HCC{}',
                     "LEP{'sigma': 0.6}",
                     "DDCMA{'sigma': 1.5}",
                     "CCPSO2{'group_sizes': [2, 4, 8, 20]}",
                     "ONES{'sigma': 1.5}",
                     "SGES{'sigma': 0.6}",
                     "RHC{'x': [], 'sigma': 0.3, 'temperature': 500.0}",
                     'GENITOR{}',
                     "CEP{'sigma': 0.1}",
                     "DDCMA{'sigma': 0.1}",
                     "MRAS{'sigma': 1.5}",
                     "DDCMA{'sigma': 3.0}",
                     "MRAS{'sigma': 0.9}",
                     "ONES{'sigma': 0.6}",
                     'SHADE{}',
                     "MRAS{'sigma': 3.0}",
                     "FEP{'sigma': 0.1}",
                     "ONES{'sigma': 0.9}",
                     'LAMCTS{}',
                     "ENES{'sigma': 3.0}",
                     "DDCMA{'sigma': 0.3}",
                     "MMES{'sigma': 0.9}",
                     "CEP{'sigma': 0.6}",
                     "CEP{'sigma': 3.0}",
                     "ENES{'sigma': 0.3}",
                     "SGES{'sigma': 0.3}",
                     "DDCMA{'sigma': 0.9}",
                     "LEP{'sigma': 0.9}",
                     "LEP{'sigma': 0.1}",
                     "MRAS{'sigma': 0.1}",
                     "LEP{'sigma': 0.3}",
                     'G3PCX{}',
                     'JADE{}',
                     "ONES{'sigma': 0.1}",
                     "ENES{'sigma': 0.9}",
                     "MRAS{'sigma': 0.6}",
                     "CEP{'sigma': 0.3}",
                     "LEP{'sigma': 1.5}",
                     "MMES{'sigma': 0.3}",
                     "MMES{'sigma': 0.1}"]

optimizers = sorted([extract(i) for i in failed_optimizers], key=lambda x: str(x))
