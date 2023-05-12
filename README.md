# manual_scaffold

manual_scaffold is used for artificial inversion and splicing of contig sequences, mostly used to manually debug the erroneously assembled part after the scaffold step in genome assembly.


# it need one configure file, named config.ini, the example format of this file:
[input]
inputfilename = misassembly_contig.fa
merged_header = test
seq_headers = contig_header1 contig_header2
[reverse]
reverse_headers = contig_header1
