
# coding: utf-8

# In[ ]:


from Bio import SeqIO
import argparse

parser = argparse.ArgumentParser(description='script looks like Trimmomatic')
parser.add_argument( '-in', '--input_file', help = 'path to file in fastq format', type = str, metavar = 'str')
parser.add_argument( '-out', '--output_file', help = 'path to file for output', type = str, metavar = 'str')
parser.add_argument( '-slide_window', '--integer1', help = 'size of window', type = int, metavar = 'int')
parser.add_argument( '-right_end', '--integer2', help = 'length to crop at right end', type = int, metavar = 'int')
parser.add_argument( '-left_end', '--integer3', help = 'length to crop at left end', type = int, metavar = 'int')
parser.add_argument( '-quality_threshold', '--integer4', help = 'quality to crop', type = int, metavar = 'int')

args = parser.parse_args()

with open(args.output_file, 'w') as out:        
    handle = SeqIO.parse(args.input_file, 'fastq')
   
    for seq in handle:
        
	seq = seq[args.integer2:-args.integer3]
      
        for index in range(len(seq.seq)-args.integer1+1):
            
            if (sum(seq.letter_annotations['phred_quality'][index:(index + args.integer1)])/len(seq.letter_annotations['phre$

                SeqIO.write(seq[0:index], out, 'fastq')

                break           

            else:
                continue
            if index == len(seq.seq)-args.integer1+1:
                SeqIO.write(seq, out, 'fastq')
