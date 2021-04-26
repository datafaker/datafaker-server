#!/usr/bin/env python3

import setuptools

setuptools.setup(
  name = 'rest-server',
  version = '0.0.1',
  description = 'The REST API server for datafaker tools',
  author = 'datafaker',
  license = 'GPL-3.0',
  url = 'https://github.com/datafaker/rest-server',
  download_url = 'https://github.com/datafaker/rest-server/downloads',
  keywords = ['distributed-locks'],
  classifiers = [],
  install_requires = open("requirements.txt").readlines(),
  python_requires=">=3.0,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*",
  package_dir = {'':'src'},
  packages = setuptools.find_packages('src'),
)
