from setuptools import setup, find_packages

with open("README.md") as f:
    descr = f.read()

setup(
    name="DrugLinker",
    version="0.1.0",
    packages=find_packages(),
    author="Ferran Gonzalez Hernandez",
    license="MIT",
    install_requires=["pandas==1.0.3"],
    package_data={'DrugLinker': ["dbvocab.csv"]}

)
