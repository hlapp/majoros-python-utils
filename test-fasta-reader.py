#!/bin/env python
#=========================================================================
# This is OPEN SOURCE SOFTWARE governed by the Gnu General Public
# License (GPL) version 3, as described at www.opensource.org.
# Copyright (C)2016 William H. Majoros (martiandna@gmail.com).
#=========================================================================
from __future__ import (absolute_import, division, print_function, 
   unicode_literals, generators, nested_scopes, with_statement)
from builtins import (bytes, dict, int, list, object, range, str, ascii,
   chr, hex, input, next, oct, open, pow, round, super, filter, map, zip)
from FastaReader import FastaReader

filename="/home/bmajoros/1000G/assembly/combined/HG00096/1.fasta"

#reader=FastaReader("/home/bmajoros/1000G/assembly/combined/HG00096/1.fasta")
#while(True):
#    [defline,seq]=reader.nextSequence()
#    if(not defline): break
#    print("defline="+defline);
#    L=len(seq)
#    print("length="+str(L))

print(FastaReader.getSize("/home/bmajoros/1000G/assembly/BRCA1-NA19782.fasta"))

