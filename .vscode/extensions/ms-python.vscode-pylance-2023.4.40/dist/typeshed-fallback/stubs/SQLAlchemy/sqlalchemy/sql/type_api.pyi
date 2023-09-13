from _typeshed import Incomplete
from typing import Any, Generic, TypeVar

from .. import util
from . import operators
from .base import SchemaEventTarget
from .visitors import Traversible, TraversibleType

_T = TypeVar("_T")

BOOLEANTYPE: Any
INTEGERTYPE: Any
NULLTYPE: Any
STRINGTYPE: Any
MATCHTYPE: Any
INDEXABLE: Any
TABLEVALUE: Any

class TypeEngine(Traversible):
    class Comparator(operators.ColumnOperators[_T], Generic[_T]):
        default_comparator: Any
        def __clause_element__(self): ...
        expr: Any
        type: Any
        def __init__(self, expr) -> None: ...
        def operate(self, op, *other, **kwargs): ...
        def reverse_operate(self, op, other, **kwargs): ...
        def __reduce__(self): ...
    hashable: bool
    comparator_factory: Any
    sort_key_function: Any
    should_evaluate_none: bool
    def evaluates_none(self): ...
    def copy(self, **kw): ...
    def compare_against_backend(self, dialect, conn_type) -> None: ...
    def copy_value(self, value): ...
    def literal_processor(self, dialect) -> None: ...
    def bind_processor(self, dialect) -> None: ...
    def result_processor(self, dialect, coltype) -> None: ...
    def column_expression(self, colexpr) -> None: ...
    def bind_expression(self, bindvalue) -> None: ...
    def compare_values(self, x, y): ...
    def get_dbapi_type(self, dbapi) -> None: ...
    @property
    def python_type(self) -> None: ...
    def with_variant(self, type_, dialect_name): ...
    def as_generic(self, allow_nulltype: bool = False): ...
    def dialect_impl(self, dialect): ...
    def adapt(self, cls, **kw): ...
    def coerce_compared_value(self, op, value): ...
    def compile(self, dialect: Incomplete | None = None): ...

class VisitableCheckKWArg(util.EnsureKWArgType, TraversibleType): ...

class ExternalType:
    cache_ok: Any

class UserDefinedType:
    __visit_name__: str
    ensure_kwarg: str
    def coerce_compared_value(self, op, value): ...

class Emulated:
    def adapt_to_emulated(self, impltype, **kw): ...
    def adapt(self, impltype, **kw): ...

class NativeForEmulated:
    @classmethod
    def adapt_native_to_emulated(cls, impl, **kw): ...
    @classmethod
    def adapt_emulated_to_native(cls, impl, **kw): ...

class TypeDecorator(ExternalType, SchemaEventTarget, TypeEngine):
    __visit_name__: str
    impl: Any
    def __init__(self, *args, **kwargs) -> None: ...
    coerce_to_is_types: Any

    class Comparator(TypeEngine.Comparator[Any]):
        def operate(self, op, *other, **kwargs): ...
        def reverse_operate(self, op, other, **kwargs): ...

    @property
    def comparator_factory(self): ...
    def type_engine(self, dialect): ...
    def load_dialect_impl(self, dialect): ...
    def __getattr__(self, key: str): ...
    def process_literal_param(self, value, dialect) -> None: ...
    def process_bind_param(self, value, dialect) -> None: ...
    def process_result_value(self, value, dialect) -> None: ...
    def literal_processor(self, dialect): ...
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...
    def bind_expression(self, bindparam): ...
    def column_expression(self, column): ...
    def coerce_compared_value(self, op, value): ...
    def copy(self, **kw): ...
    def get_dbapi_type(self, dbapi): ...
    def compare_values(self, x, y): ...
    @property
    def sort_key_function(self): ...

class Variant(TypeDecorator):
    cache_ok: bool
    impl: Any
    mapping: Any
    def __init__(self, base, mapping) -> None: ...
    def coerce_compared_value(self, operator, value): ...
    def load_dialect_impl(self, dialect): ...
    def with_variant(self, type_, dialect_name): ...
    @property
    def comparator_factory(self): ...

def to_instance(typeobj, *arg, **kw): ...
def adapt_type(typeobj, colspecs): ...
