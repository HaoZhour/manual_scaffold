## manual_scaffold

# Discription 
Manual_scaffold is used for artificial inversion and splicing of contig sequences, mostly used to manually debug the erroneously assembled part after the scaffold step in genome assembly.


# Usage

\`python manual_scaffold.py fasta config\`


# Configure file
It need one configure file, the example format of the file is as follows, in this case, manual_scaffold will reverse contig2 and link it to contig1, it will output : reversed contig2 seq + N*200 + contig1 seq

[input]

merged_header = scaffold_test

seq_headers = contig2 contig1

[reverse]

reverse_headers = contig2