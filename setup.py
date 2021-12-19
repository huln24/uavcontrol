#!/usr/bin/env python
from setuptools import setup, find_packages


if __name__ == "__main__":
    setup(
        name="uavcontrol",
        version="0.0.0",
        description="UAV control library",
        author="Khulan Ulziibat",
        packages=find_packages(),
        setup_requires=["setuptools"],
    )
