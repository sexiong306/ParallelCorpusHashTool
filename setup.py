#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/13 上午11:06
# @Author  : pudgeli@tecncent.com
from setuptools import setup, find_packages
VERSION = '1.0.0'
setup(
    name='ParallelCorpusHashTool',
    version=VERSION,
    install_requires=['mmh3'],
    packages=find_packages(),

    # packages=find_packages('HashTool'),  # 包含所有src中的包
    # package_dir={'': 'HashTool'},  # 告诉distutils包都在src下

    package_data={
        # 任何包中含有.txt文件，都包含它
        '': ['*.txt'],
        # 包含demo包data文件夹中的 *.dat文件
        # 'demo': ['data/*.dat'],
    },
    include_package_data=True,
    zip_safe=True,

    # metadata for upload to PyPI
    author="pudgeli",
    author_email="pudgeli@tencent.com",
    description="a tool to generate hash for parallelcorpus",
    license="MIT",
    keywords="123456",
    url="https://github.com/sexiong306/ParallelCorpusHashTool.git",
)