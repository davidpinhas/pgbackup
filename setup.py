from importlib_metadata import entry_points
from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    description='Database backups locally or to AWS S3.',
    long_description=readme,
    author='David Pinhas',
    auther_email='davidp@jfrog.com',
    install_requires=['boto3'],
    pacakges=find_packages('src'),
    pacakge_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'pgbackup=pgbackup.cli:main',
        ]
    }
)
