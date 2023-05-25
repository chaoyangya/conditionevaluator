# -*- coding: utf-8 -*-
"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""
import setuptools
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setuptools.setup(
    name="conditionevaluator",
    version="1.0.0",
    author="cy what",
    author_email="45204307@qq.com",
    description="Package of modules that encapsulate the if else multi-condition judgment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chaoyangya/conditionevaluator",
    packages=setuptools.find_packages(),
    license="conditionevaluator",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",

    ],
    keywords="conditionevaluator, conditionevaluator_python",
)
