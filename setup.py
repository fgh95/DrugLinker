from setuptools import setup, find_packages


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="druglinker",
    version="0.1.0",
    description="Simple drug linking",
    long_description=readme(),
    long_description_content_type="text/markdown",
    author="Ferran Gonzalez Hernandez",
    author_email="ucbpfgo@ucl.ac.uk",
    license="MIT",
    packages=find_packages(),
    install_requires=["pandas==1.0.3"],
    include_package_data=True,
    package_data={'druglinker': ['dbvocab.csv']},
    python_requires='>=3.6',
    url="https://github.com/fgh95/DrugLinker"

)
