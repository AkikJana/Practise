import json
data=json.load(open("data.json"))

def translate(w):
	return data[w]

word=input("enter word: ")
print(translate(word))