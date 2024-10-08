import pathlib
import codecs
import setuptools


here = pathlib.Path(__file__).resolve().parent

with codecs.open(here.joinpath('DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='modular_client',

    version = '8.4.3',

    description='Modular device Python client interface for communicating with and calling remote methods on modular device servers.',
    long_description=long_description,

    url='https://github.com/janelia-python/modular_client_python',

    author='Peter Polidoro',
    author_email='peter@polidoro.io',

    license='BSD',

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: BSD License',

        'Programming Language :: Python :: 3',
    ],

    keywords='modular serial arduino device client modulardevice modular-device modular_device modularclient modular-client modular_client json json-rpc',

    packages=setuptools.find_packages(exclude=['contrib', 'docs', 'tests*']),

    install_requires=['serial_interface',
                      'inflection',
                      'sre_yield',
    ],
)
