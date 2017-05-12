import sys

ofile = open('english_clean.txt','w')
sys.stdout = ofile

with open('wiki.simple') as ifile:
	for line in ifile:
	    lines = line.split('.')
	    for sentence in lines:
		if(len(sentence)>20):
			sentence = sentence.replace("`", "")		
			print sentence.strip()
        
ifile.close();
ofile.close();
