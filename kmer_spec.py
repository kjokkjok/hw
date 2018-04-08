from Bio import SeqIO
import pandas as pd
from collections import Counter

class Kmer():
    
    def __init__(self):
        
        self.kmer_dict = Counter()
        self.kmer_distr = Counter()
          
    #парсим файл, фильтруем риды по качеству и заполняем словарь к-меров
    def fq_parse(self, file, size, qual):

        self.kmer_size = size
        self.handle = SeqIO.parse(file, 'fastq')
        self.q = qual
        for seq in self.handle:

            for index in range(len(seq.seq) - self.kmer_size+1):
                self.current_kmer = seq.seq[index:(index + self.kmer_size)]

                if all(x < self.q for x in seq.letter_annotations['phred_quality'][index:(index + self.kmer_size)]):
                    
                    self.kmer_dict[str(self.current_kmer)] += 1
        
        return self.kmer_dict
    
    #переводим словарь с к-мерами в массив и сразу убираем шум:
    def to_array(self, kmerdict):
        
        
        for i, j in self.kmer_dict.items():
            if j > 1:
                self.kmer_distr[j] += 1
        
        self.plot_data = [[j]*i for i, j in self.kmer_distr.items() if j > 1 ]
        
        print(self.kmer_dict)
        print(self.kmer_distr)
        print(self.plot_data)
        
    #визуализируем распределение
    def viz_distr(self, data, maxX, stepX, maxY, stepY):

        plt.hist(data, bins=50, facecolor='g',ec='k')
        plt.axis([0,maxX, 0, maxY])
        plt.xlabel('counts k-mer')
        plt.ylabel('frequency')
        plt.xticks([i for i in range(0,maxX,stepX)], size=5)
        plt.yticks([i for i in range(0,maxY, stepY)])
        plt.title('Histogram of k-mer distribution')

    #считаем примерный размер генома
    def genome_length(self):
       
        self.genome_size = sum(map(lambda x: len(x)*x[0], self.plot_data))/(max(self.plot_data, key=len))[0]
        print(round(self. genome_size))
        
data = Kmer()
data.fq_parse('Загрузки/test_kmer.fastq', 10, 30)
data.to_array(data.kmer_dict)
data.viz_distr(data.plot_data, 4000, 200, 40, 5)
data.genome_length()
