import pandas as pd
import pkg_resources

path = "dbvocab.csv"
filepath = pkg_resources.resource_filename(__name__, path)
tabdata = pd.read_csv(filepath)

def splitstr(inp_str):
    out_list = inp_str.lower().split("|")
    return [x.strip() for x in out_list]


def get_ids(string_term, fromterminal=False):
    newdf = tabdata.fillna("")
    newdf["Synonyms"] = newdf["Synonyms"].apply(splitstr)
    identifiers = []
    for c, synlist in enumerate(newdf["Synonyms"].values):
        if string_term.lower() in synlist:
            dbid = newdf["DrugBank ID"].values[c]
            identifiers.append(dbid)
            if fromterminal:
                print(dbid)
    if not fromterminal:
        return identifiers


if __name__ == "__main__":
    myterm = input("Enter drug term to be search: ")
    myterm = str(myterm)
    print("Term searched is: ", myterm)
    print("Here you have the DrugBank ID/s of the drugs matched: ")
    get_ids(myterm, fromterminal=True)
