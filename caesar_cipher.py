import re


class Caesar:
	ans=0
	alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	def __init__(self):
		text=""
		
		while True:
			print "Menu\n"
			print "\t1.- Cipher\n"
			print "\t2.- Decipher\n"
			print "\t3.- Exit\n"
			self.ans=raw_input("What would you like to do?\n ")
			
			if(self.ans=="1"):
				text=self.readText()
				shift=self.changeShift()
				if(0 < shift < 26 and shift is not 3):
					print shift
					self.cipher(text, shift)
				else:
					self.cipher(text, 3)
			elif(self.ans=="2"):
				text=self.readText()
				shift=self.changeShift()
				if (shift is not 3 and 0 < shift < 26):
					self.decipher(text, shift)
				else:
					self.decipher(text, 3)
			elif(self.ans=="3"):
				exit()
			else:
				print "Not a valid option, try again"

			
	def cipher(self, plaintext, shift):
		cipher=""
		print "\tThe current shift is: ",(shift)
		for i in plaintext:
			cipher+=self.alphabet[((self.alphabet.index(i)+shift)%26)]
		print "\tYour plaintext is: "+plaintext
		print "\tYour ciphered text is: "+cipher
		print "\t------------------------------------------------------------"


	def decipher(self, ciphertext, shift):
		decipher=""
		print "\tThe current shift is: ",(shift)
		for i in ciphertext:
			decipher+=self.alphabet[((self.alphabet.index(i)-shift)%26)]
		print "\tYour ciphered text is: "+ciphertext
		print "\tYour deciphered text is: "+decipher
		print "\t------------------------------------------------------------"

	def readText(self):
		text=raw_input("\nPlease provide the text\n>").lower()
		clean=re.sub("\d+|\W|_","",text,flags=re.IGNORECASE)
		return clean

	def changeShift(self):
		ans2=0
		shift= -1
		ans2=raw_input("Would you like to change the shift?[Y/N]\n>").upper()
		if(ans2 == "Y"):
			while(shift < 1 or shift > 26):
				print "Note: The shift has to be between 1 and 26\n"
				shift=int(raw_input("Enter the new shift\n>"))
			return shift
		elif(ans2 == "N"):
			print "Ok the shift is 3\n"
			pass
		else:
			return 3
			
cesar=Caesar()