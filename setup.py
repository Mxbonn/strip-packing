from setuptools import find_packages, setup

setup(
    name='strip-packing',
    packages=find_packages(),
    version='0.1.0',
    description='A priority heuristic for the guillotine rectangular packing problem.',
    author='Maxim Bonnaerens',
    license='',
    install_requires=[
        'matplotlib',
        ]
)