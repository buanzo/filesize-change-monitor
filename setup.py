# -*- coding: utf-8 -*-
from os import path
from setuptools import setup

# Imports content of requirements.txt into setuptools' install_requires
with open('requirements.txt') as f:
    requirements = f.read().splitlines()


def get_version():
    with open('filesizemon.py') as f:
        for line in f:
            if line.startswith('__version__'):
                return eval(line.split('=')[-1])


# Imports content of README.md into setuptools' long_description
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.txt'), encoding='utf-8') as f:
    long_description = f.read()


setup(name='filesizemon',
      version=get_version(),
      description="Script that monitors a folder for filesize changes. Good to determine culprit during server performance analysis.",
      long_description=long_description,
      keywords="log, analysis, performance, filesize, monitor",
      author='Arturo "Buanzo" Busleiman',
      author_email='buanzo@buanzo.com.ar',
      url='https://github.com/buanzo/filesize-change-monitor',
      license='MIT License',
      zip_safe=False,
      python_requires='>=3.6',
      py_modules=['filesizemon'],
      namespace_packages=[],
      install_requires=requirements,
      entry_points={
         'console_scripts': [
            'filesizemon = filesizemon:logsizemon',
         ],
      },
      classifiers=[
         'Environment :: Console',
         'Intended Audience :: System Administrators',
         'Programming Language :: Python',
      ])
