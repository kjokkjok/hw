
# coding: utf-8

# In[3]:


from Bio import SeqIO
import pandas as pd
class Kmer():
    
        def __init__(self, seq):
            self.counter = 0
            self.seq = seq
            self.location=[]
        def increase(self):
            self.counter += 1
        def add_location(self, start, stop):
            self.location.append((start,stop))
        def return_frame(self):
            print(self.seq)
            self.frame = pd.DataFrame({'kmer_name':[str(self.seq)]*self.counter,                                       'coordinates':self.location,                                       'locus': [locus]*self.counter})
            return self.frame
            
handle = list(SeqIO.parse("/home/kjokkjok/bioinf/seq_y_pestis2.fasta",                          "fasta")) #parsing fasta and converting into list
kmer_size = 13
kmer_dict = {} 

seq = handle[0].seq
locus = handle[0].id
seq_lng = len(seq)
for index in range(seq_lng - kmer_size + 1):
    current_kmer = seq[index:(index + kmer_size)]

    if current_kmer in kmer_dict:
        kmer_dict[current_kmer].add_location(index,index+kmer_size)
    else:
        kmer_dict[current_kmer] = Kmer(current_kmer)
        kmer_dict[current_kmer].add_location(index, index+kmer_size)
    
    kmer_dict[current_kmer].increase()   

    
#находим наиболее часто встречающийся к-мер с помощью lambda по счётчику и выводим:
    
print("Наиболее часто встречающийся k-mer:'{}' встречается {} раз(a) и имеет координаты:{}".format(max(kmer_dict, key=lambda k: kmer_dict[k].counter),kmer_dict[max(kmer_dict, key=lambda k: kmer_dict[k].counter)].counter,kmer_dict[max(kmer_dict, key=lambda k: kmer_dict[k].counter)].location))

#делаем датафрейм по самому частому к-меру из координат, локуса, имени:
df = kmer_dict[max(kmer_dict, key=lambda k: kmer_dict[k].counter)].return_frame()
df

