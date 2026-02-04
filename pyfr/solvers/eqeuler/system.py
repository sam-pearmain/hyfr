from pyfr.solvers.baseadvec import BaseAdvectionSystem
from pyfr.solvers.eqeuler.elements import EquilibriumEulerElements
from pyfr.solvers.eqeuler.inters import (
    EquilibriumEulerBaseBCInters,
    EquilibriumEulerIntInters,
    EquilibriumEulerMPIInters,
)


class EquilibriumEulerSystem(BaseAdvectionSystem):
    name = "eqeuler"

    elementscls = EquilibriumEulerElements
    intinterscls = EquilibriumEulerIntInters
    mpiinterscls = EquilibriumEulerMPIInters
    bbcinterscls = EquilibriumEulerBaseBCInters
