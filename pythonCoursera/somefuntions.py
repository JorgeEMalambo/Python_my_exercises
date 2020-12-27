def test1():
	def cleanSpace(string):
		# clean the string of empty spaces
		string = string.replace(" ", "")
		string = string.lower()
		return string


	def palidromeRecursive(string):
		# base case
		if string == '':
			return True
		# base case codition
		if string[0] == string[len(string) - 1]:
			return palidromeRecursive(string[1:len(string) - 1])
		return False


	def is_palindrome(string):
		string = cleanSpace(string)
		return palidromeRecursive(string)


	print(is_palindrome("Never Odd or Even"))  # Should be True
	print(is_palindrome("abc"))  # Should be False
	print(is_palindrome("kayak"))  # Should be True

def test2():
	def counter(start, stop):
		x = start


		if start == stop:
			return_string = 'A count is not necessary since the quantities are identical'
			return return_string

		if x > stop:
			return_string = "Counting down: "
			while x >= stop:
				return_string += str(x)
				if x > stop:
					return_string += ","
				x -= 1
		else:
			return_string = "Counting up: "
			while x <= stop:
				return_string += str(x)
				if x < stop:
					return_string += ","
				x += 1
		return return_string
	print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
	print(counter(2, 1)) # Should be "Counting down: 2,1"
	print(counter(5, 5)) # Should be "Counting up: 5"

def test3():
	def multiplication_table(start, stop):
		for x in range (start,stop+1):
			for y in range(start,stop+1):
				print(str(x*y), end=" ")
			print()

	multiplication_table(1,3)
	multiplication_table(2,7)

def test4():
	def even_numbers(maximum):
		return_string = ""
		for x in range (2,maximum+1,2):
			return_string += str(x) + " "
		return return_string.strip()

	print(even_numbers(6))  # Should be 2 4 6
	print(even_numbers(10)) # Should be 2 4 6 8 10
	print(even_numbers(1))  # No numbers displayed
	print(even_numbers(3))  # Should be 2
	print(even_numbers(0))  # No numbers displayed

def test5():
	def initials(phrase):
		phrase = phrase.upper()
		words = phrase.split()
		result = ""
		for word in words:
			result += word[0]
		return result

	print(initials("Universal Serial Bus")) # Should be: USB
	print(initials("local area network")) # Should be: LAN
	print(initials("Operating system")) # Should be: OS

"""
In Python, there are a lot of things you can do with strings. In this cheat sheet, you’ll find the most common string operations and string methods.

String operations
len(string) Returns the length of the string
for character in string Iterates over each character in the string
if substring in string Checks whether the substring is part of the string
string[i] Accesses the character at index i of the string, starting at zero
string[i:j] Accesses the substring starting at index i, ending at index j-1. If i is omitted, it's 0 by default. If j is omitted, it's len(string) by default.
String methods
string.lower() / string.upper() Returns a copy of the string with all lower / upper case characters
string.lstrip() / string.rstrip() / string.strip() Returns a copy of the string without left / right / left or right whitespace
string.count(substring) Returns the number of times substring is present in the string
string.isnumeric() Returns True if there are only numeric characters in the string. If not, returns False.
string.isalpha() Returns True if there are only alphabetic characters in the string. If not, returns False.
string.split() / string.split(delimiter) Returns a list of substrings that were separated by whitespace / delimiter
string.replace(old, new) Returns a new string where all occurrences of old have been replaced by new.
delimiter.join(list of strings) Returns a new string with all the strings joined by the delimiter 
"""

def test6():
	def convert_distance(miles):
		km = miles * 1.6
		result = "{} miles equals {:.1f} km".format(miles, km)
		return result

	print(convert_distance(12))  # Should be: 12 miles equals 19.2 km
	print(convert_distance(5.5))  # Should be: 5.5 miles equals 8.8 km
	print(convert_distance(11))  # Should be: 11 miles equals 17.6 km

def test7():
	def replace_ending(sentence, old, new):
		sentence = sentence.split()
		# Check if the old string is at the end of the sentence
		if sentence[len(sentence) - 1] == old:
			# Using i as the slicing index, combine the part
			# of the sentence up to the matched string at the
			# end with the new string
			i = sentence[:len(sentence) - 1]
			i.append(new)
			new_sentence = " ".join(i)
			return new_sentence

		# Return the original sentence if there is no match
		return " ".join(sentence)

	print(replace_ending("It's raining cats and cats", "cats", "dogs"))
	# Should display "It's raining cats and dogs"
	print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
	# Should display "She sells seashells by the seashore"
	print(replace_ending("The weather is nice in May", "may", "april"))
	# Should display "The weather is nice in May"
	print(replace_ending("The weather is nice in May", "May", "April"))

def test8():
	"""
	Try out the enumerate function for yourself in this quick exercise. Complete the skip_elements 
	function to return every other element from the list, this time using the enumerate function to 
	check if an element is on an even position or an odd position.
	"""
	def skip_elements(elements):
		lista=list()
		for index, x in enumerate(elements):
			if index%2==0:
				lista.append(x)
		return lista

	print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
	print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
	# Should display "The weather is nice in April"

def test9():
	"""
	The odd_numbers function returns a list of odd numbers between 1 and n, inclusively. 
	Fill in the blanks in the function, using list comprehension. Hint: remember that 
	list and range counters start at 0 and end at the limit minus 1.
	"""
	def odd_numbers(n):
		return [x for x in range(n+1) if x%2==1]

	print(odd_numbers(5))  # Should print [1, 3, 5]
	print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
	print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
	print(odd_numbers(1))  # Should print [1]
	print(odd_numbers(-1)) # Should print []

def test10():
	"""
	Given a list of filenames, we want to rename all the files with extension hpp to the extension h. 
	To do this, we would like to generate a new list called newfilenames, consisting of the new filenames.
	 Fill in the blanks in the code using any of the methods you’ve learned thus far, like a for 
	 loop or a list comprehension.
	
	filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
	# Generate newfilenames as a list containing the new filenames
	# using as many lines of code as your chosen method requires.
	newfilenames=[file for file in filenames (if '.hpp'in file file.replace('.hpp','.h')) ] 
	HAY ALGO MAL EN PARA INTRODUCIR EL REEMPLAZO DENTRO DE LA LISTA POR COMPRENSION
	print(newfilenames) 
	# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

	"""
	filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
	# Generate newfilenames as a list containing the new filenames
	# using as many lines of code as your chosen method requires.
	newfilenames=[]
	for file in filenames:
		if '.hpp' in file:
			newfilenames.append(file.replace('.hpp','.h'))  
		else:
			newfilenames.append(file)
	

	print(newfilenames) 
	# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

def test11():
	"""
	Let's create a function that turns text into pig latin: a simple text transformation that modifies
	each word moving the first character to the end and appending "ay" to the end. For example, 
	python ends up as ythonpay.
	"""
	# funcionalidad incorrecta, este codigo invierte todos los caracteres 
	# y debe solo invertir el primero y el ultimo para luego agregar los caracteres 'ay'
	def pig_latin2(text):
		say = list()
		# Separate the text into words
		words = text.split()
		for word in words:
			# Create the pig latin word and add it to the list
			say.append(word[::-1]+'ay')
			# Turn the list back into a phrase
		return ' '.join(say)
	
	
	# funcionalidad correcta
	def pig_latin(text):
		say = list()
		# Separate the text into words
		words = text.split()
		for word in words:
			# Create the pig latin word and add it to the list
			say.append(word[1:]+word[0]+'ay')
			# Turn the list back into a phrase
		return ' '.join(say)
	
	print(pig_latin("hello how are you")) # Should be "ellohay ohway reaay ouyay"
	print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

def test13():
	"""
	The permissions of a file in a Linux system are split into three sets of three permissions: 
	read, write, and execute for the owner, group, and others. Each of the three values can be 
	expressed as an octal number summing each permission, with 4 corresponding to read, 2 to write, 
	and 1 to execute. Or it can be written with a string using the letters r, w, and x or - when
	 the permission is not granted. For example: 640 is read/write for the owner, read for the group, 
	 and no permissions for the others; converted to a string, it would be: "rw-r-----" 
	 755 is read/write/execute for the owner, and read/execute for group and others; 
	 converted to a string, it would be: "rwxr-xr-x" Fill in the blanks to make the code convert a 
	 permission in octal format into a string format.
	"""
	def octal_to_string(octal):
		result = ""
		value_letters = [(4,"r"),(2,"w"),(1,"x")]
		# Iterate over each of the digits in octal
		for digit in [int(n) for n in str(octal)]:
			# Check for each of the permissions values
			for value, letter in value_letters:
				if digit >= value:
					result += letter
					digit -= value
				else:
					result+='-'
		return result
    
	print(octal_to_string(755)) # Should be rwxr-xr-x
	print(octal_to_string(644)) # Should be rw-r--r--
	print(octal_to_string(750)) # Should be rwxr-x---
	print(octal_to_string(600)) # Should be rw-------

def test14():
	"""
	The group_list function accepts a group name and a list of members, and returns a string with 
	the format: group_name: member1, member2, … For example, group_list("g", ["a","b","c"]) 
	returns "g: a, b, c". Fill in the gaps in this function to do that.
	"""
	def group_list(group, users):
		members = group+':'
		for user in users:
			members+=' '+user+','
		if (len(members)) > len (group)+1:
			return members[:len(members)-1]
		return members

	print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
	print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
	print(group_list("Users", "")) # Should be "Users:"

def test15():
	"""
	The guest_list function reads in a list of tuples with the name, age, and profession of each 
	party guest, and prints the sentence "Guest is X years old and works as __." for each one. 
	For example, guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")) 
	should print out: 
									Ken is 30 years old and works as Chef
									Pat is 35 years old and works as Lawyer 
									Amanda is 25 years old and works as Engineer 
	Fill in the gaps in this function to do that.
	"""
	def guest_list(guests):
		for name, old, job in guests:
			print('{} is {} years old and works as {}'.format(name, old, job))

	guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

	#Click Run to submit code
	"""
	Output should match:
	Ken is 30 years old and works as Chef
	Pat is 35 years old and works as Lawyer
	Amanda is 25 years old and works as Engineer
	"""

def test16():
	"""
	The "toc" dictionary represents the table of contents for a book. Fill in the blanks to do 
	the following: 1) Add an entry for Epilogue on page 39. 2) Change the page number for 
	Chapter 3 to 24. 3) Display the new dictionary contents. 4) Display True if there is 
	Chapter 5, False if there isn't.
	"""
	toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
	toc["Epilogue"]=39 # Epilogue starts on page 39
	toc["Chapter 3"]=24# Chapter 3 now starts on page 24
	print(toc)# What are the current contents of the dictionary?
	if "Chapter 5" in toc: 
		print ('True') # Is there a Chapter 5?
	else:
		print('False')

def test17():
	"""
	In Python, a dictionary can only hold a single value for a given key. To workaround this, 
	our single value can be a list containing multiple values. Here we have a dictionary called 
	"wardrobe" with items of clothing and their colors. 
	
	Fill in the blanks to print a line for each item of clothing with each color, 
	for example: "red shirt", "blue shirt", and so on."""

	wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
	for cloth in wardrobe.keys():
		for color in wardrobe[cloth]:
			print("{} {}".format(color,cloth))
	

def test19():
	"""
	The format_address function separates out parts of the address string into new strings: house_number and street_name, and returns: "house number X on street named Y". The format of the input string is: numeric house number, followed by the street name which may contain numbers, but never by themselves, and could be several words long. For example, "123 Main Street", "1001 1st Ave", or "55 North Center Drive". Fill in the gaps to complete this function.
	"""
	def format_address(address_string):
		# Declare variables
		addrees_parts=address_string.split()
		# Separate the address string into parts
		house_number=''
		street_name=''
		# Traverse through the address parts
		for part in addrees_parts:
			if part.isdigit():
				house_number+=part+' '
			else:
				street_name+=part
			# Determine if the address part is the
			# house number or part of the street name

		# Does anything else need to be done 
		# before returning the result?
		
		# Return the formatted string  
		return "house number {} on street named {}".format(house_number,street_name)

	print(format_address("123 Main Street"))
	# Should print: "house number 123 on street named Main Street"

	print(format_address("1001 1st Ave"))
	# Should print: "house number 1001 on street named 1st Ave"

def test20():
	"""
	The highlight_word function changes the given word in a sentence to its upper-case version. For example, 
	highlight_word("Have a nice day", "nice") returns "Have a NICE day". 
	Can you write this function in just one line?
	"""
	def highlight_word(sentence, word):
		return(" ".join(x) for x in sentence.split())

	print(highlight_word("Have a nice day", "nice"))
	print(highlight_word("Shhh, don't be so loud!", "loud"))
	print(highlight_word("Automating with Python is fun", "fun"))

if __name__=='__main__':
	test20()






