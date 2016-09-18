from __future__ import division
import xml.etree.ElementTree as ET
from collections import Counter

doc = ET.parse('C:/Users/bb/Documents/Dropbox/Data analysis/\
City of Toronto/dinesafe.xml')
rows = doc.findall('ROW')
name_words = Counter()
word_frequency = {}
total_word_count = 0

for row in rows:
	name = row.find('ESTABLISHMENT_NAME').text.split()
	for word in name:
		name_words[word] += 1
		total_word_count += 1
		word_frequency[word] = 0
			
#for word in word_frequency:
#	numerator = name_words[word]+1
#	denominator = total_word_count+1
#	word_frequency[word] = round(float(numerator/denominator),4)
	
#print word_frequency.items()

sort_namewords = sorted(name_words.iteritems(), key=lambda (k, v): (-v, k))
		
for key, value in sort_namewords:
	#print str(key) + " " + str(value)
	print str(key) + " " + str(value) 