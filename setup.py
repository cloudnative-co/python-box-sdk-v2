from setuptools import setup, find_packages

setup(
    name="PyBox",
    version="0.9.1",
    description="Lite Weight Box API SDK for python",
    author="sebastian",
    author_email="seba@cloudnative.co.jp",
    packages=find_packages(),
    install_requires=[
        "cryptography",
        "pytz"
    ],
    entry_points={
        "console_scripts": [
        ]
    },
)
