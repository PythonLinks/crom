# -*- coding: utf-8 -*-

import venusian
from zope.configuration.config import ConfigurationMachine

base_ignores = ['.testing', '.tests', '.ftests']


def grok(package, config, ignores=base_ignores):
    scanner = venusian.Scanner(config=config)
    scanner.scan(package, ignore=ignores)


def configure(*packages):
    config = ConfigurationMachine()
    for package in packages:
        grok(package, config)
    config.execute_actions()
