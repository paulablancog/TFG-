# Streamlit code
import pandas as pd
import app.chem

# Asking for compound SMILES code
smiles_code = input("Enter the SMILES code: ")
compound = app.chem.retrieve_compound(smiles_code)
if compound:
    print("Compound found!")
    compound_info = app.chem.compound_information(compound)
    print("\n")
    print(compound_info)
else:
    print("No compound found, check the SMILES code entered again")

# Retrieving Compound information from PubChem
data = app.chem.retrieve_compoundURL(compound)
print(data)


# : CC(C[N+](C)(C)C)OC(=O)N  