"""Convert a SMILES string into an MDL MolBlock with 2-D coordinates (RDKit).

Problem: SMILES is compact but most drawing and modelling tools expect a MOL
file with atom coordinates. This script bridges the two.

How it works: reads a SMILES string from the file ``xfile_protocol`` (next to
the script), parses it with RDKit, computes 2-D depiction coordinates, and
prints the resulting MolBlock.

Usage: ``python smiles_to_molblock.py`` (requires ``rdkit``). Put any SMILES
into ``xfile_protocol`` to convert your own molecule.
"""
from __future__ import print_function
#import os

from rdkit import Chem
from rdkit.Chem import AllChem


print("name : ", "New Molecule")
f = open('xfile_protocol')
fa = f.read()
f.close()
print("smiles : ", fa)

m = Chem.MolFromSmiles(fa)

AllChem.Compute2DCoords(m)

mm = Chem.MolToMolBlock(m)

print(mm)
