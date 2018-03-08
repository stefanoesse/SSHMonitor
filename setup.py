#!/usr/bin/env python

#import distutils.cmd,setuptools,os

from setuptools import setup  
from distutils.errors import DistutilsExecError
from distutils.command.install import install as init

#class Install(distutils.cmd.Command):
class install(init):
    def run(self):
        try:
            self.spawn('/bin/echo', '-e', 'Setting up SSHMonitor')
            self.spawn('/bin/bash','build/build.sh')
        except DistutilsExecError:
            self.warn('listing directory failed')
            super.run()

#setuptools.setup(
setup(
    name='sshmonitor',
    version='0.0.2',
    author='Anthony Guevara',
    author_email='amboxer21@gmail.com',
    license='GPL-3.0',
    url='https://github.com/amboxer21/SSHMonitorPy',
    packages=[],
    classifiers=[
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Development Status :: 2 - Beta',
        'Programming Language :: Python :: 2.7',
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: GNU General Public License (GPL)', 
    ],
    cmdclass={
        'install': install,

    },
)
