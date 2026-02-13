import pandas as pd
import pubchempy as pcp
import requests 


# Methods 
# Step 1: Recognize the drug by SMILES code with PubChem database

def retrieve_compound(smiles_code):
    compounds = pcp.get_compounds(smiles_code, namespace='smiles') #returns a list of matches
    if not compounds: 
        return None
    compound = compounds[0]
    return compound

def compound_information(compound):
    return{
        'cid': compound.cid,
        'synonyms': compound.synonyms[0],
        'name': compound.iupac_name,
        'molecular_formula': compound.molecular_formula,
        'molecular_weight': compound.molecular_weight,
    }


# Step 2: Get Interactions and Pathways CSV from compound -> get it from the PUG REST API 
def retrieve_compoundURL(compound):
    cid = compound.cid
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/{cid}/JSON/"

    response = requests.get(url) #in a Request form
    if response.status_code != 200:
        print("Invalid URL. Failed to retrieve Interactions & Pathway of: "+compound.synonyms[0])
        return None
    
    print("Valid URL")

    data = response.json() #parse to JSON 



    return data
