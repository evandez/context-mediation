"""Some useful type aliases relevant to this project."""
import pathlib
from typing import AbstractSet, List, Mapping, Tuple, Union

import torch

PathLike = Union[str, pathlib.Path]
Device = Union[str, torch.device]

# All strings are also Sequence[str], so we have to distinguish that we
# mean lists or tuples of strings, or sets of strings, not other strings.
StrSequence = Union[List[str], Tuple[str, ...]]
StrSet = AbstractSet[str]
StrIterable = Union[StrSet, StrSequence]
StrMapping = Mapping[str, str]