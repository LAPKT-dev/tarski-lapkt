# -*- coding: utf-8 -*-
import itertools


def get_symbols(lang, type_="all", include_builtin=True):
    """ Return all symbols of the given type (function/predicate), and including or excluding builtins as desired """
    if type_ == "predicate":
        iterate_over = lang.predicates
    elif type_ == "function":
        iterate_over = lang.functions
    else:
        assert type_ == "all"
        iterate_over = itertools.chain(lang.predicates, lang.functions)

    if include_builtin:
        return iterate_over
    else:
        return (x for x in iterate_over if not x.builtin)


def get_id_from_literal(val):
    """ Return the (string) name of the given constant, if a constant, or the actual value, if it is a literal """
    from . import Constant
    if isinstance(val, Constant):
        return val.name
    return val
