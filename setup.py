from setuptools import setup, find_packages

def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="DrugLinker",
    version="0.1.0",
    long_description = readme(),
    author="Ferran Gonzalez Hernandez",
    license="MIT",
    packages=["DrugLinker"],
    install_requires=["pandas==1.0.3"],
    include_package_data=True

)
