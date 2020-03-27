# DrugLinker

This package is a very simple tool to obtain all unique drug identifiers that match a specific input string.
 It does so by matching the input term with DrugBank open-data vocabulary : https://www.drugbank.ca/releases/latest#open-data. 

First, let's install this package by running: 

```
git clone https://github.com/fgh95/DrugLinker
cd DrugLinker
pip install .
```

Example of use: 

```
from druglinker import dbsearch
dbsearch.get_ids("amoxicillin")
# output: ["DB01060"]
```
