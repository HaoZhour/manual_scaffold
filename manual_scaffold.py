"""
author:haozhou
data:2023-5-12
usage: It is used for artificial inversion and splicing of contig sequences, mostly used to manually debug the erroneously assembled part after the scaffold step in genome assembly.
inputfile: fasta file, config.ini
outputfile: a combined one scaffold  sequences file

config.ini:

[input]
inputfilename = 5_misassembly_contig.fa
merged_header = scaffold_test
seq_headers = ptg000042l ptg000010l
[reverse]
reverse_headers = ptg000042l
"""

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

inputfilename = config["input"]["inputfilename"]
merged_header = config["input"]["merged_header"]
seq_headers = config["input"]["seq_headers"].split()
reverse_seq_headers = config["reverse"]["reverse_headers"].split() #分开的contig读成列表


#combine fasta sequences
def merge_sequences(inputfilename, merged_header, *seq_headers,reverse_seq_headers):
    records = list(SeqIO.parse(inputfilename, "fasta"))
    seq_records = []
    for seq_header in seq_headers:
        seq_record = next((record for record in records if record.id == seq_header), None)
        if seq_record is not None:
            if seq_header in reverse_seq_headers:
                seq_record.seq = seq_record.seq.reverse_complement()
            seq_records.append(seq_record)
    Ns= "N"*200

    seqs = Ns.join([str(seq_record.seq) for seq_record in seq_records])
    merged_seq = Seq(seqs)
    merged_seq_record = SeqRecord(merged_seq, id=merged_header, description="")
    outfilename = merged_header+".fasta"
    with open(outfilename, "w") as output_handle:
        SeqIO.write(merged_seq_record, output_handle, "fasta")

merge_sequences(inputfilename, merged_header, *seq_headers,reverse_seq_headers)






