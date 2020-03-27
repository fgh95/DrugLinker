import pandas as pd

tabdata = pd.read_csv("dbvocab.csv")


def splitstr(inp_str):
    out_list = inp_str.lower().split("|")
    return [x.strip() for x in out_list]


def perform_search(string_term, fromterminal=False):
    newdf = tabdata.fillna("")
    newdf["Synonyms"] = newdf["Synonyms"].apply(splitstr)
    for c, synlist in enumerate(newdf["Synonyms"].values):
        identifiers = []
        if string_term.lower() in synlist:
            dbid = newdf["DrugBank ID"].values[c]
            if fromterminal:
                print(dbid)
            else:
                identifiers.append(dbid)
    if not fromterminal:
        return identifiers


if __name__ == "__main__":
    myterm = input("Enter drug term to be search: ")
    myterm = str(myterm)
    print("Term searched is: ", myterm)
    print("Here you have the DrugBank ID/s of the drugs matched: ")
    perform_search(myterm, fromterminal=True)
