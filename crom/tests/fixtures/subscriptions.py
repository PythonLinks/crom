# -*- coding: utf-8 -*-

import crom


class ISomeSubscription(crom.Interface):
    pass


class IOne(crom.Interface):
    pass


class ITwo(crom.Interface):
    pass


class IThree(crom.Interface):
    pass


@crom.implements(IOne)
class One(object):
    pass


@crom.implements(ITwo)
class Two(object):
    pass


@crom.implements(IThree)
class Three(object):
    pass


@crom.subscription
@crom.sources(IOne)
@crom.target(ISomeSubscription)
class Subscription(object):

    def __init__(self, context):
        self.context = context


@crom.subscription
@crom.order(10)
@crom.sources(ITwo, IThree)
@crom.target(ISomeSubscription)
class MultiSubscription1(object):

    def __init__(self, two, three):
        self.two = two
        self.three = three


@crom.subscription
@crom.sources(ITwo, IThree)
@crom.target(ISomeSubscription)
class MultiSubscription2(object):

    def __init__(self, two, three):
        self.two = two
        self.three = three
