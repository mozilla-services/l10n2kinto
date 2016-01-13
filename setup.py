import codecs
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    README = f.read()


REQUIREMENTS = [
    'kinto-client',
    'six',
]


ENTRY_POINTS = {
    'console_scripts': [
        'l10n2kinto = l10n2kinto.__main__:main'
    ]
}


setup(name='l10n2kinto',
      version='0.1.0.dev0',
      description='l10n properties file upload into Kinto',
      long_description=README,
      license='Apache License (2.0)',
      classifiers=[
          "Programming Language :: Python",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.4",
          "License :: OSI Approved :: Apache Software License"
      ],
      keywords="web services",
      author='Mozilla Services',
      author_email='services-dev@mozilla.com',
      url='https://github.com/mozilla-services/l10n2kinto',
      packages=find_packages(),
      zip_safe=False,
      install_requires=REQUIREMENTS,
      entry_points=ENTRY_POINTS)
