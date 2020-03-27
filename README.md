# DrugLinker

This package is a very simple tool to obtain all unique drug identifiers that match a specific input string. It does so by matching synonyms with drugbank vocabulary of term synonyms. 

First, let's install this package by running: 

```
git clone 
cd DrugLinker
python setup.py install
```

Now download the open-access list of Drugbank identifiers and synonyms: 

````

curl -Lfv -o dbvocabulary.zip https://www.drugbank.ca/releases/5-1-5/downloads/all-drugbank-vocabulary
unzip dbvocabulary.zip

````
