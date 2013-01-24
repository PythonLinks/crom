# -*- coding: utf-8 -*-

from zope.interface.interfaces import ComponentLookupError
from .implicit import implicit
from .interfaces import NoImplicitLookupError


SENTINEL = object()


def do_lookup(iface, lookup_func, component_name, *args, **kw):
    sources = args
    target = iface
    name = kw.pop('name', '')
    default = kw.pop('default', SENTINEL)
    if kw:
        raise TypeError("Illegal extra keyword arguments: %s" %
                        ', '.join(kw.keys()))
    component = lookup_func(sources, target, name)

    if component is not None:
        return component
    if default is not SENTINEL:
        return default
    raise ComponentLookupError(
        "Could not find %s from sources %s to target %s." %
        (component_name, sources, target))


def find_lookup(kw):
    lookup = kw.pop('lookup', None)
    if lookup is None:
        if implicit.lookup is None:
            raise NoImplicitLookupError(
                "Cannot lookup without explicit lookup argument "
                "because implicit lookup is not configured.")
        lookup = implicit.lookup
    return lookup


def get_all_components(iface, *required, **kw):
    lookup = find_lookup(kw)
    return lookup.lookup_all(required, iface)


def component_lookup(iface, *args, **kw):
    # iface will serve as 'self' when monkey-patched onto InterfaceClass
    return do_lookup(
        iface, find_lookup(kw).lookup, 'component', *args, **kw)


def adapter_lookup(iface, *args, **kw):
    # a shortcut rule to make sure self-adaption works even without
    # a registry supplied
    if len(args) == 1 and iface.providedBy(args[0]):
        return args[0]
    return do_lookup(
        iface, find_lookup(kw).adapt, 'adapter', *args, **kw)


def subscription_lookup(target, *sources, **kws):
    lookup = find_lookup(kws)
    subscribe = kws.pop('subscribe', False)
    for sub in lookup.subscriptions(sources, target):
        if subscribe:
            yield sub(*sources)
        else:
            yield sub
