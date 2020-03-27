# DrugLinker

This package is a simple tool to obtain all unique drug identifiers that match a given input string.
It does so by matching the input term with DrugBank open-data vocabulary : https://www.drugbank.ca/releases/latest#open-data. 
It is useful to process candidate drug tokens after drug named-entity recognition (NER) or to directly match sentences after tokenization,

To install the package simply run:

```
pip install druglinker==0.1.0
```

Example of use: 

```
from druglinker import dbsearch
dbsearch.get_ids("amox")
# output: ["DB01060"]
dbsearch.get_ids("amoxicillin")
# output: ["DB01060"]
dbsearch.get_ids("vancomycin")
# output: ["DB00512"]

# Simple sentence tagging:

text = "20mg of midazolam were administered intravenously"
for term in string.split():
    ids = dbsearch.get_ids(term)
    if ids:
        print(term)
        print(ids)

# output:
# midazolam
# ['DB00683']

```
