[![DOI](https://zenodo.org/badge/194699221.svg)](https://zenodo.org/badge/latestdoi/194699221)

This repository contains data and simulation input from the paper:

"Application of the ESMACS binding free energy protocol to a highly varied ligand dataset: lactate dehydogenase A", David W. Wright, Fouad Husseini, Shunzhou Wan, Christophe Meyer, Herman van Vlijmen, Gary Tresadern, and Peter V. Coveney

Preprint DOI: [10.26434/chemrxiv.8398055](https://doi.org/10.26434/chemrxiv.8398055)

What follows is a brief description of the contents.

# Naming conventions 

During the preparation of the paper two naming conventions have been used - internally ligands were numbered sequentially (giving l1-l22) but to agree with the experimental publication [1] we numbered the ligands LDHA12, LDHA14-LDHA34.

[1] R. A. Ward, *et al.*, J. Med. Chem., 2012, 55, 3285–3306, DOI:[10.1021/jm201734r](https://doi.org/10.1021/jm201734r)

We have named directories using a combination of both, e.g. l1-LDHA12.
In the data files (all in tab separated value format) the columns ligname represented internal numbering and jan.id the LDHA prefixed numbering.

# Directories

initial-structures  ligand-inputs  mmpbsa  protein-inputs

## initial-structures

Amber forcefield topology (`prmtop`) and coordinate (`inpcrd` and `pdb`) files for complexes of LDHA with each ligand.

## protein-inputs

Contains the PDB used to create starting structures (based on chain A of 4BJX), including conserved water molecules.

## ligand-inputs

Contains the information on the ligands used to initiate the project that led to the paper and ligand parameters used for simulations.
This includes:

- Biological data: LDHA_biol_data.tsv
- Ligand structures: LDHA_ligands.sdf
- Forcefield parameters describing parameterized ligands, in Amber formats (`frcmod` and `prep`)
  -  `ligand_params_am1_bcc` : Ligands using AM1-BCC charges
  -  `ligand_params_gaussian_resp`  : Ligands using Gaussian/RESP charges

## mmpbsa

Files related to MMPBSA analysis in tab separated values format.

- `input` - contains the MMPBSA input file used for all analyses
- `wsaa`, `normal_mode` and `variational-entropy` contain data from teh three investigated entropic contributions.

