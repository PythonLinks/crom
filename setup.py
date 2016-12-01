import os
from setuptools import setup, find_packages

setup(name='crom',
      version = '0.1.dev1',
      description="Components.",
      author="Martijn Faassen",
      author_email="faassen@startifact.com",
      license="BSD",
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'grokker',
          'oset',
          'setuptools',
          'venusian>=1.0a3',
          'zope.configuration',
          'zope.interface',
          ],
      packages=find_packages('src'),
      package_dir={'': 'src'},
      extras_require = dict(
        test=['pytest >= 2.0'],
        ),
      entry_points="""
      # Add entry points here
      """,
      )
