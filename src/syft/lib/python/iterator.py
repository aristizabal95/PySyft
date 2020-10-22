# stdlib
from typing import Any
from typing import Iterable

# syft relative
from ...core.common.uid import UID
from ...decorators import syft_decorator
from .primitive_interface import PyPrimitive
from .util import SyPrimitiveRet


class Iterator(PyPrimitive):
    @syft_decorator(typechecking=True, prohibit_args=False)
    def __init__(self, _ref: Iterable):
        super().__init__()
        self._obj_ref = _ref
        self._index = 0
        self._id = UID()
        self._exhausted = False

    @syft_decorator(typechecking=True, prohibit_args=False)
    def __iter__(self) -> SyPrimitiveRet:
        return self

    @syft_decorator(typechecking=True, prohibit_args=False)
    def __next__(self) -> Any:
        if self._exhausted:
            raise StopIteration

        if self._index >= len(self._obj_ref):
            self._exhausted = True
            raise StopIteration

        obj = self._obj_ref[self._index]
        self._index += 1
        return obj
