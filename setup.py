from setuptools import find_packages, setup

# Package meta-data.
NAME = "netdaemon"
DESCRIPTION = "An ML-based Network Management System."
AUTHOR = "Mr-Skully"
REQUIRES_PYTHON = ">=3.8.0"
VERSION = "0.1.0"

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    python_requires=REQUIRES_PYTHON,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'netdaemon = netdaemon.run:main',
        ],
    },
)