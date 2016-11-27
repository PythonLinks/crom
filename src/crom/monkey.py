# -*- coding: utf-8 -*-

from zope.interface.interface import InterfaceClass
from .extiface import (
    component_lookup, adapter_lookup, subscription_lookup,
    predicates_lookup, get_all_components)


def safe():
    InterfaceClass.all_components = get_all_components
    InterfaceClass.component = component_lookup
    InterfaceClass.adapt = adapter_lookup
    InterfaceClass.subscription = subscription_lookup
    InterfaceClass.predicates = predicates_lookup


def incompat():
    safe()
    # monkey patch instead of adapter hooks mechanism as we change
    # the call signature
    InterfaceClass._original_call = InterfaceClass.__call__
    InterfaceClass.__call__ = adapter_lookup


def revert_safe():
    del InterfaceClass.component
    del InterfaceClass.adapt
    del InterfaceClass.subscription


def revert_incompat():
    revert_safe()
    InterfaceClass.__call__ = InterfaceClass._original_call
    del InterfaceClass._original_call
