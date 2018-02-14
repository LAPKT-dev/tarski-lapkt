from types import MethodType
from . import builtins as syntax_builtins
from . terms import Term

class ArithmeticOperatorImplementation :

    def __init__(self, sym):
        self._symbol = sym

    def __call__( self, lhs: Term, rhs: Term ) :
        sym = lhs.language.resolve_function_symbol(self._symbol, lhs.sort, rhs.sort)
        return sym(lhs, rhs)

    def __get__(self, instance, owner):
        return MethodType(self, instance) if instance else self


class RelationalOperatorImplementation :
    def __init__(self, sym):
        self._symbol = sym

    def __call__( self, lhs: Term, rhs: Term ) :
        return getattr(syntax_builtins,self._symbol)(lhs,rhs)

    def __get__(self, instance, owner):
        return MethodType(self, instance) if instance else self
