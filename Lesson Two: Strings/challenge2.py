# jtyurkovich, 2014

# coding: utf-8

# In[1]:

# Open an existing text file (must be in current directory for Python to 
# be able to find and open it) and read in the text. Download the text file
# ApolloandDaphne.txt from the Github page (Ovid's "Apollo and Daphne" in 
# the original Latin from his Metamorphoses) and print the text to the 
# screen, line by line.
textfile = open('ApolloandDaphne.txt','r')
print textfile.read()
textfile.close()


# In[2]:

# Now let us edit the file. This is poetry, so let us add line numbers at
# the beginning of each line, then save the file as ApolloandDaphne_edited.txt.
textfile = open('ApolloandDaphne.txt','r')
newfile = open('ApolloandDaphne_edited.txt','w')

count = 0

for line in textfile:
    count += 1
    newline = '[%s] ' %count
    newfile.write(newline + line)
    
textfile.close()
newfile.close()


# In[3]:

# Going back to the original (unedited) file, let us count the number of 
# words in the excerpt. For this particular file, notice that some of the
# "words" that are reported look very weird; this is because the file 
# contained quotation marks, and Python has trouble interpreting those.
textfile = open('ApolloandDaphne.txt','r')

for line in textfile:
    words = line.split()
    print words    


# In[4]:

# Now let us turn to a bioinformatics application. Read in the text file 
# dna_sequence.txt and list:
#   (1) the length of the sequence
#   (2) how many bases are A
#   (3) how many start codons (ATG)
#   (4) how many TAA stop codons (check to make sure they are in the same
#       reading frame as the start codons found in (3))
#   (5) the sequence running from the start codon to the stop codon
#   (6) the amino acid sequence using this dictionary:
#       aa = {'ATG':'M','CTA':'L','GTC':'V','GTG':'V','GAT':'D','CGA':'R'}
dna_sequence = open('dna_sequence.txt','r')

seq = dna_sequence.read().rstrip('\n')

print '(1) %s bases long' %len(seq)
print '(2) %s As' %seq.count('A')
print '(3) %s start codon(s)' %seq.count('ATG')

pos = seq.find('ATG')
codon = 'NNN'

while codon != 'TAA':
    codon = seq[pos:pos+3]
    pos = pos + 3
    
    if codon == 'TAA':
        print '(4) %s TAA stop codons' %seq.count('TAA')
        flag = True
    
    if pos > len(seq) - 4:
        print '(5) No TAA stop codons in reading frame'
        flag = False
        break

if flag:
    nu_seq = seq[seq.find('ATG'):seq.find('TAA')]
        
    print '(5) ' + nu_seq

    aa = {'ATG':'M','CTA':'L','GTC':'V','GTG':'V','GAT':'D','CGA':'R'}
    aa_seq = ''

    for index in range(0,len(nu_seq),3):
        codon = nu_seq[index:index+3]
        aa_seq += aa[codon]

    print '(6) ' + aa_seq

