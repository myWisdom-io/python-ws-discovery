from setuptools import setup

setup(name='WSDiscovery',
      version='2.1.2',
      packages=['wsdiscovery', 'wsdiscovery.actions'],
      setup_requires=['ifaddr', 'click'],
      install_requires=['ifaddr', 'click'],
      tests_require=['pytest', 'mock']
      )
