from setuptools import find_packages, setup

setup(
    name='rw_rate_all',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'rw_rate_all = rw_rate_all.rw_rate_all:main'
        ]
    }
)
