# -*- coding: utf-8 -*-

from grokker import grokker, directive
from .directives import sources, target, name, registry
from .current import current
from .interfaces import IRegistry


@grokker
@directive(sources)
@directive(target)
@directive(name)
@directive(registry)
def component(scanner, pyname, obj, sources, target, name='', registry=None):
    def register():
        if registry is None:
            use_registry = current.registry
        elif not IRegistry.providedBy(registry):
            use_registry = registry()
        else:
            use_registry = registry
        use_registry.register(sources, target, name, obj)
    scanner.config.action(
        discriminator=('component', sources, target, name, registry),
        callable=register
        )


@grokker
@directive(sources)
@directive(target)
@directive(registry)
def subscription(scanner, pyname, obj, sources, target, registry=None):
    def register():
        if registry is None:
            use_registry = current.registry
        elif not IRegistry.providedBy(registry):
            use_registry = registry()
        else:
            use_registry = registry
        use_registry.subscribe(sources, target, obj)
    scanner.config.action(
        discriminator=None,
        callable=register
        )


adapter = component
