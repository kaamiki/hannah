"""H.A.N.N.A.H: Heuristically Aiding Neural Network based AI for Humans
"""

from ._logging import *

try:
    from ._version import __version__
except ImportError:
    __version__ = "Unknown version"

__all__ = _logging.__all__  # type: ignore