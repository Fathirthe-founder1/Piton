from setuptools import setup, find_packages

setup(
    name='piton',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'piton = piton.cli:main'
        ]
    },
    description='Bahasa Pemrograman Indonesia berbasis Python',
    author='Fathirthe-founder1',
    url='https://github.com/Fathirthe-founder1/Piton',
    python_requires='>=3.6',
)
