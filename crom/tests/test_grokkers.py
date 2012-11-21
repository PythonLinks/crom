# -*- coding: utf-8 -*-

# XXX check the situation where a registry is passed
# that is an IRegistry instance. Will it conflict with
# the same registration on that registry correctly?
    
# need to add tests for stackable lookup


import crom
from crom import monkey, extiface, utils, testing


def setup_function(method):
    testing.setup()


def teardown_function(method):
    testing.teardown()


def test_component():
    from .fixtures import component as module

    # grok the component module
    crom.configure(module)

    # we should now be able to adapt things
    source = module.Source()
    adapted = module.ITarget(source)
    assert module.ITarget.providedBy(adapted)
    assert isinstance(adapted, module.Adapter)
    assert adapted.context is source


def test_subscriptions():
    from .fixtures import subscriptions as module

    # grok the component module
    crom.configure(module)

    # we should now be able to get simple subscriptions
    source1 = module.One()
    subs = list(extiface.subscription_lookup(
        module.ISomeSubscription, source1))

    assert len(subs) == 1
    assert isinstance(subs[0], module.Subscription)

    # we should also be able to get multi subscriptions
    source2 = module.Two()
    source3 = module.Three()

    subs = list(extiface.subscription_lookup(
        module.ISomeSubscription, source2, source3))

    assert len(subs) == 2
    assert isinstance(subs[0], module.MultiSubscription1)
    assert isinstance(subs[1], module.MultiSubscription2)

    # ordered components are sortable
    sorted_subs = list(utils.sort_components(subs))
    assert isinstance(sorted_subs[0], module.MultiSubscription2)
    assert isinstance(sorted_subs[1], module.MultiSubscription1)


def test_new_grokker():
    from .fixtures import new_grokker as module
    # this module defines a new 'view' grokker that uses the
    # same registration machinery as the component grokker

    # grok the new grokker module
    crom.configure(module)
    # we should now be able to adapt things
    source = module.Source()
    view = module.ITarget(source, name='foo')
    assert module.ITarget.providedBy(view)
    assert isinstance(view, module.View)
    assert view.context is source
  
    
# XXX check the situation where a registry is passed
# that is an IRegistry instance. Will it conflict with
# the same registration on that registry correctly?
