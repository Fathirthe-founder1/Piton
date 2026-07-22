from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pitonx",
    version="8.0.3",
    author="Jameson AlFathir Void",
    author_email="fathiragata22@gmail.com",
    description="PitonX - A Python Programming Language with Indonesian Keywords",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Fathirthe-founder1/PitonX",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Languages",
        "Topic :: Education",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Natural Language :: Indonesian",
        "Development Status :: 4 - Beta",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "pitonx=pitonx.main:main",
            "piton=pitonx.main:repl_main",
        ],
    },
    keywords=[
        "python",
        "programming",
        "language",
        "indonesian",
        "transpiler",
        "interpreter",
        "bahasa-pemrograman",
    ],
    project_urls={
        "Bug Reports": "https://github.com/Fathirthe-founder1/PitonX/issues",
        "Documentation": "https://github.com/Fathirthe-founder1/PitonX",
        "Source Code": "https://github.com/Fathirthe-founder1/PitonX",
    },
    include_package_data=True,
)
