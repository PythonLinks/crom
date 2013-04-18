# -*- coding: utf-8 -*-

import crom


class ISource(crom.Interface):
    pass


class ITarget(crom.Interface):
    pass


@crom.implements(ISource)
class Source(object):
    pass


@crom.adapter
@crom.sources(ISource)
@crom.target(ITarget)
@crom.implements(ITarget)
class Adapter(object):

    def __init__(self, context):
        self.context = context


@crom.component_factory
@crom.sources()
@crom.target(ITarget)
@crom.implements(ITarget)
class ComponentFactory(object):

    def __init__(self):
        pass

    def __call__(self):
        return self
