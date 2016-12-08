from setuptools import find_packages, setup

setup(
    name='rw_rate_all',
    version='2.1.0',
    author='William Jackson',
    author_email='william@subtlecoolness.com',
    url='https://github.com/williamjacksn/rw_rate_all',
    description='Rate songs on Rainwave',
    license='MIT License',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'rw_rate_all = rw_rate_all.rw_rate_all:main'
        ]
    }
)
