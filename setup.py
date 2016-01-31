from setuptools import setup, find_packages

setup(
    name="romaine",
    version="0.1.0",
    package_dir={'': 'src'},
    packages=find_packages('src'),
    package_data={'romaine': [
        'schemas/*.json',
        'schemas/types/*.json',
    ]},

    test_suite="tests",
)
