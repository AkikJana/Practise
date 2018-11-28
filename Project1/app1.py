import json
import difflib
from difflib import get_close_matches
data=json.load(open("data.json"))

def translate(w):
	w=w.lower()
	if w in data:
		return data[w]
	elif len(get_close_matches(w,data.keys(),1,cutoff=0.8))>0:
		close_matches=get_close_matches(w,data.keys(),1,cutoff=0.8)
		for i in close_matches:
			yn=input("did you mean %s instead?\nenter y if yes else enter n if no" % i)
			if yn.lower()=="y":
				return data[close_matches[0]]
			elif yn.lower()=="n":
				return"this word doesn't exist please double check it"
			#print(data[i])
			else:
				return"wrong input"

		
	else:
		return "the word does not exist"

while(True):
	word=input("enter word else enter 1 to exit: ")
	if(word=="1"):
		break
	else:
		temp=translate(word)
		if type(temp)==list:
			for i in temp:
				print(i)
		else:
			print(temp)

		

		 	 