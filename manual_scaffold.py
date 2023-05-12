"""
author:haozhou
data:2023-5-12
discription: It is used for artificial inversion and splicing of contig sequences, mostly used to manually debug the erroneously assembled part after the scaffold step in genome assembly.
usage:python manual_scaffold.py fasta config
inputfile: fasta file, config.ini
outputfile: a combined one scaffold sequences file

config.ini:

[input]
merged_header = scaffold_test
seq_headers = contig1 contig2
[reverse]
reverse_headers = contig1
"""

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import configparser
import argparse

#定义参数
parser = argparse.ArgumentParser(description='Combine fasta sequences')
parser.add_argument('fasta', type=str, help='input fasta file name')
parser.add_argument('config', type=str, help='config file name')
args = parser.parse_args()

inputfile = args.fasta
configfile = args.config

#解析配置文件
config = configparser.ConfigParser()
config.read(configfile)
merged_header = config["input"]["merged_header"]
seq_headers = config["input"]["seq_headers"].split()
reverse_seq_headers = config["reverse"]["reverse_headers"].split() #分开的contig读成列表


#合并fasta文件的函数
def merge_sequences(inputfile, merged_header, seq_headers, reverse_seq_headers):
    records = list(SeqIO.parse(inputfile, "fasta"))
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

#运行函数
merge_sequences(inputfile, merged_header, seq_headers, reverse_seq_headers)






