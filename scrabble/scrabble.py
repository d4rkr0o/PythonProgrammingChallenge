dictio={
	'a': 1,
	'b': 3,
	'c': 3,
	'd': 2,
	'e': 1,
	'f': 4,
	'g': 2,
	'h': 4,
	'i': 1,
	'j': 8,
	'k': 5,
	'l': 1,
	'm': 3,
	'n': 1,
	'o': 1,
	'p': 3,
	'q': 10,
	'r': 1,
	's': 1,
	't': 1,
	'u': 1,
	'v': 4,
	'w': 4,
	'x': 8,
	'y': 4,
	'z': 10
}
count=0
user_input=""
while True:
	user_input=raw_input("Input the word\n>").lower()
	if 0 < len(user_input) < 16 and user_input.isalpha():
		for i in user_input:
			count+=dictio[i]
		print "You scored => " +str(count) +" with the word",(user_input)
	elif(user_input=='quit()'):
		break
	else:
		print "Invalid Word the valid range is 1..15 inclusive your word length is " +str(len(user_input))
		continue