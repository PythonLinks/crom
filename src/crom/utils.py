# -*- coding: utf-8 -*-

from .directives import order


def _sort_key(component):
    explicit = order.get_policy(component, order.dotted_name, 0)
    return (explicit, component.__module__, component.__class__.__name__)


def sort_components(components, key=_sort_key):
    return sorted(components, key=key)
