import tinycudann as tcnn
import tinycudann32 as tcnn32

from tinycudann32_bindings import _C as _C32
from tinycudann_bindings import _C as _C

assert "Fp32" in str(_C32.preferred_precision())
assert "Fp16" in str(_C.preferred_precision())
