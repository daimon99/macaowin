# coding:utf8
from setuptools import setup, find_packages

long_description = "我要去澳门"

EXCLUDE_FROM_PACKAGES = []

setup(name="macaowin",
      version='1.0',
      url='http://github.com/daimon99/macaowin',
      license='MIT',
      author="Daimon",
      author_email="daijian1@qq.com",
      description=long_description,
      long_description=long_description,
      packages=find_packages('.'),
      include_package_data=True,
      zip_safe=False,
      platforms='any',
      install_requires=[
          'click>=2.0'
      ],
      console=['macaowin.py']

      )
