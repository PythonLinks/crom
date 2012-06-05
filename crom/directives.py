from .validators import class_or_interface_validator, interface_validator
from grokker import validator, Directive, ArgsDirective
from zope.interface import implementer


implements = implementer

sources = ArgsDirective(
    'sources', 'crom', validator=class_or_interface_validator)

target = Directive(
    'target', 'crom', validator=interface_validator)

name = Directive(
    'name', 'crom', validator=validator.str_validator)
