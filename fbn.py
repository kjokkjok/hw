from Bio import SeqIO
import argparse


parser = argparse.ArgumentParser(description='script for filtering sequences by their names')
parser.add_argument( '-in', '--input_file', help = 'path to file with names', type = str, metavar = 'str')
parser.add_argument( '-out', '--output_file', help = 'path to file for output', type = str, metavar = 'str')
parser.add_argument( '-fasta', '--fasta', help = 'path to files with sequences', type = str, metavar = 'str')
args = parser.parse_args()
with open(str(args.input_file)) as handle:
    list_names=handle.read().splitlines()
with open(str(args.output_file), 'w') as out:

    with open(str(args.fasta)) as fasta:
        for seq_record in SeqIO.parse(fasta, "fasta"):
            if seq_record.id in list_names:
                SeqIO.write(seq_record, out, "fasta")
