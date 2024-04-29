from setuptools import setup, find_packages


setup(
    name='skcli',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'cryptography',
        'fire',
    ],
    entry_points={
        'console_scripts': [
            'skcli=cli.main:main',
        ],
    },
)
