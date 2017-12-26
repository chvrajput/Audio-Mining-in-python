#!/usr/bin/python
import re
import string
import pandas
from collections import Counter
import numpy as np
frequency = {}
document_text = open('output.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
 
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
     
frequency_list = frequency.keys()
frequency_list.sort()
count =0 
for words in frequency_list:
    #print words, frequency[words]
        word = np.unique(words)
     #print(word)
	if word == "reachable":
		print "Not Reachable"
	else:
		if word == "switched":
			print "Switched Off"

	if (word == "switched") or (word == "reachable"):
		count=count+1
if (count >=1):
  print "Switched Off or Not reachable"
 
     


