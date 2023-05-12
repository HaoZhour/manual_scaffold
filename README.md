## manual_scaffold

# Discription 
Manual_scaffold is used for artificial inversion and splicing of contig sequences, mostly used to manually debug the erroneously assembled part after the scaffold step in genome assembly.


# Usage

\`python manual_scaffold.py fasta config\`


# Configure file
It need one configure file, the example format of the file:

[input]

inputfilename = misassembly_contig.fa

merged_header = test

seq_headers = contig_header1 contig_header2

[reverse]

reverse_headers = contig_header1
