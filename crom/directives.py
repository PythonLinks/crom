# -*- coding: utf-8 -*-

from grokker import Directive, ArgsDirective
from grokker import validator
from zope.interface import implementer
from .validators import class_or_interface_validator, interface_validator


order = Directive(
    'order', 'crom', validator=validator.int_validator)

target = Directive(
    'target', 'crom', validator=interface_validator)

name = Directive(
    'name', 'crom', validator=validator.str_validator)

sources = ArgsDirective(
    'sources', 'crom', validator=class_or_interface_validator)


# a factory that when called gives back the registry
registry = Directive('registry', 'crom')

implements = implementer

