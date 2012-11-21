# -*- coding: utf-8 -*-

from grokker import grokker, directive, Directive
from .directives import sources, target, name
from .current import current
from .implicit import implicit
from .interfaces import IRegistry, NoImplicitRegistryError


def registry_converter(registry):
    if registry is not None:
        if not IRegistry.providedBy(registry):
            return registry()
        return registry
    if implicit.registry is None:
        raise NoImplicitRegistryError(
            "Cannot register without explicit "
            "registry decorator because implicit registry "
            "is not configured.")
    return implicit.registry


# this needs to be defined here to avoid circular imports
registry = Directive('registry', 'crom', converter=registry_converter)


@grokker
@directive(sources)
@directive(target)
@directive(name)
@directive(registry)
def component(scanner, pyname, obj, sources, target, registry, name=''):

    def register():
        registry.register(sources, target, name, obj)

    scanner.config.action(
        discriminator=('component', sources, target, name, registry),
        callable=register)


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
