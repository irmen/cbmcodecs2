import os
import re

from setuptools import setup

VERSION_RE = re.compile(".*__version__ = '(.*?)'", re.MULTILINE)
v_file = os.path.join(os.path.dirname(__file__), 'cbmcodecs2', '__init__.py')
with open(v_file) as f:
    version = VERSION_RE.search(f.read()).group(1)

setup(
    name='cbmcodecs2',
    description='Python codecs for CBM PETSCII and Screencode encodings',
    long_description=open('README.rst', 'rb').read().decode(errors="replace"),
    author='Irmen de Jong',
    author_email='irmen@razorvine.net',
    packages=['cbmcodecs2'],
    license='GPLv2',
    url='https://github.com/irmen/cbmcodecs2',
    version=version,
    install_requires=[],
    test_suite="tests",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
