# -*- coding: utf-8 -*-
"""
The basic ILookup is implemented by crom.Registry (in registry.py).
This module contains alternative Lookups that can be used to combine
lookups together.
"""
from oset import oset
from .implicit import implicit
from .interfaces import ILookup, ILookupsChain
from .directives import implements


@implements(ILookupsChain, ILookup)
def ChainedLookup(oset):
    """
    """
    def add(self, lookup):
        assert ILookup.providedBy(lookup):
        oset.add(self, lookup)

    def adapt(self, obs, target, name):
        for lookup in self.lookups:
            result = lookup.adapt(obs, target, name)
            if result is not None:
                return result
        return None

    def lookup(self, obs, target, name):
        for lookup in self.lookups:
            result = lookup.lookup(obs, target, name)
            if result is not None:
                return result
        return None

    def lookup_all(self, obs, target):
        for lookup in self.lookups:
            results = list(lookup.lookupAll(
                list(map(providedBy, obs)), target))
            if results is not None:
                return iter(results)
        return None

    def subscriptions(self, obs, target):
        for lookup in self.lookups:
            results = list(lookup.subscriptions(map(providedBy, obs), target))
            if results is not None:
                return iter(results)
        return None


class LookupContext(object):
    """A context manager to work in a given lookup.
    """
    def __init__(self, lookup):
        assert ILookup.providedBy(lookup), (
            u"A LookupContext lookup must be an ILookup object.")
        self.node = node

    def __enter__(self):
        implicit.lookup = self.lookup
        return self.lookup

    def __exit__(self, type, value, traceback):
        implicit.registry.reset_lookup()


class LookupChainLink(object):
    """A context manager to work in a given looku, added to a lookups' chain.
    """
    def __init__(self, link):
        assert ILookup.providedBy(link), (
            u"A LookupChainLink link must be an ILookup object.")
        self.link = link

    def __enter__(self):
        assert ILookupsChain.providedBy(implicit.lookup), (
            u"LookupChainLink can only be called if the current"
            u" implicit is an ILookupsChain lookup.")
        implicit. = self.link
        return self.link

    def __exit__(self, type, value, traceback):
        implicit.registry.reset_lookup()
