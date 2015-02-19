import os, sys, re, codecs
from setuptools import setup, find_packages

def read(*parts):
    # intentionally *not* adding an encoding option to open
    # see here: https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    return codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), *parts), 'r').read()

long_description = read('README.rst')

setup(name="statkey",
      version="0.1",
      description="A simple script to make the commands 'git status', 'hg status' and 'svn status' run with a one key command - the s key.",
      long_description=long_description,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Topic :: Software Development :: Build Tools',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
#          'Programming Language :: Python :: 3',
#          'Programming Language :: Python :: 3.1',
#          'Programming Language :: Python :: 3.2',
#          'Programming Language :: Python :: 3.3',
      ],
      keywords='development environment tool git svn hg mercurial',
      author='Colm O\'Connor',
      author_email='colm.oconnor.github@gmail.com',
      license='MIT',
      packages=find_packages(exclude=["contrib", "docs", "tests*"]),
      package_data={},
      entry_points=dict(console_scripts=['s=statkey:run',]),
      zip_safe=False,
)
