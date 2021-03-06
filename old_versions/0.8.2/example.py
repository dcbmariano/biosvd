#!/usr/bin/python
#     Program: example.py
#    Function: Test library BioSVD
# Description: It shows tests using BioSVD for sequence classification
#      Author: TS Correia, DCB Mariano, JR Barroso, RC de Melo-Minardi
#     Version: 0.8.2


# Help - Use: python example.py file_1.fasta file_2.fasta file_n.fasta


# Requirements
from BioSVD import *
import sys
import os


# Testing function "read"
seqs = BioSVD.read('fasta',sys.argv[1:])

# Testing function "kmer"
mfkmer = BioSVD.kmer(seqs,3,'a')

# Testing function "svds"
[U, S, V] = BioSVD.svds(mfkmer)

# Testing function "factor"
s = BioSVD.factor(S,'plot')

# Testing function "extractFactor"
mfkmer_3 = BioSVD.extractFactor(S,V,3)

# Testing function "plot2"
BioSVD.plot2( mfkmer,'plot')

# Testing function "plot3"
BioSVD.plot3( mfkmer,'plot')
