#!/usr/bin/env python

#sudo python setup.py bdist_wheel
#twine upload ./dist/*.whl

import os
import codecs
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

if os.path.exists("README.rst"):
    long_description = codecs.open('README.rst', "r", "utf-8").read()
else:
    long_description = "See http://github.com/nvie/vim_bridge/tree/master"

from vim_bridge import __version__ as version

setup(
    name="vim_bridge3",
    version=version,
    description="A Python3-to-Vim bridge decorator that allows transparent calls to Python 3 functions in native Vim scripts.",
    author="Vincent Driessen",
    author_email="vincent@datafox.nl",
    url="http://github.com/rpuntaie/vim_bridge",
    platforms=["any"],
    license="BSD",
    packages=find_packages(),
    install_requires=[],
    tests_require=['nose'],
    test_suite="nose.collector",
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX",
        "Topic :: Text Editors",
    ],
    long_description=long_description,
)
