"""
Numbers to Words by Christopher Scott
http://www.scottdchris.com/

Program takes an integer as an input and returns the word representation of the integer.
Works up to 999,999,999
Program begins by parsing number to array of digits with numToArray mehtod
"""

units = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',]
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

places = ['', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth']
teenPlaces = ['tenth', 'eleventh', 'twelfth', 'thirteenth', 'fourteenth', 'fifteenth', 'sixteenth', 'seventeenth', 'eighteenth', 'nineteenth']
tensPlaces = ['', 'tenth', 'twentieth', 'thirtieth', 'fortieth', 'fifthieth', 'sixthieth', 'seventieth', 'eightieth', 'ninetieth']

def numToArray(num):
	numArray = [0,0,0,0,0,0,0,0,0]
	numArray[0] = num/100000000%10 	#Hundred Millions place
	numArray[1] = num/10000000%10 	#Ten Millions place
	numArray[2] = num/1000000%10 	#Millions place
	numArray[3] = num/100000%10 	#Hundred-thousands place
	numArray[4] = num/10000%10 		#Ten-thousands place
	numArray[5] = num/1000%10 		#Thousands place
	numArray[6] = num/100%10 		#Hundreds place
	numArray[7] = num/10%10 		#Tens place
	numArray[8] = num/1%10 			#Ones place
	return numArray

def hasTrailingZeros(numArray):
	if (numArray[6]!=0):
		return numArray[7]==0 and numArray[8]==0
	elif (numArray[3]!=0 or numArray[4]!=0 or numArray[5]!=0):
		return numArray[6]==0 and numArray[7]==0 and numArray[8]==0
	elif (numArray[0]!=0 or numArray[1]!=0 or numArray[2]!=0):
		return numArray[3]==0 and numArray[4]==0 and numArray[5]==0 and numArray[6]==0 and numArray[7]==0 and numArray[8]==0

def numToWords(num):
	numArray = numToArray(num)
	word = ''
	if (num==0):
		word = 'zero'
	if (num>=1 and num<=9):
		word = units[num]
	if (num>=10 and num<=19):
		word = teens[num%10]
	if (num>=20 and num<=99):
		word += tens[num/10]
		if (numArray[8]!=0):
			word+= ' ' + units[num%10]
	
	if (num>=100 and num<=999):
		word += units[numArray[6]] + ' hundred '
		if (not hasTrailingZeros(numArray)):
			word += numToWords(numArray[7]*10+numArray[8])

	if (num>=1000 and num<=999999):
		word += numToWords(numArray[3]*100+numArray[4]*10+numArray[5]) + ' thousand '
		if (not hasTrailingZeros(numArray)):
			word += numToWords(numArray[6]*100+numArray[7]*10+numArray[8])

	if (num>=1000000 and num<=999999999):
		word += numToWords(numArray[0]*100+numArray[1]*10+numArray[2]) + ' million '
		if (not hasTrailingZeros(numArray)):
			word += numToWords(numArray[3]*100000+numArray[4]*10000+numArray[5]*1000+numArray[6]*100+numArray[7]*10+numArray[8])
	
	word = ' '.join(word.split())
	return word

def numToPlace(num):
	numArray = numToArray(num)
	place = ''
	if (num==0):
		place = 'zeroth'
	if (num>=1 and num<=9):
		place = places[num]
	if (num>=10 and num<=19):
		place = teenPlaces[num%10]
	if (num>=20 and num<=99):
		if (numArray[8]==0):
			place += tensPlaces[num/10]
		else:
			place += tens[num/10] + ' ' + places[num%10]
	
	if (num>=100 and num<=999):
		if (hasTrailingZeros(numArray)):
			place += units[numArray[6]] + ' hundredth'
		else:
			place += units[numArray[6]] + ' hundred ' + numToPlace(numArray[7]*10+numArray[8])

	if (num>=1000 and num<=999999):
		if (hasTrailingZeros(numArray)):
			place += numToWords(numArray[3]*100 + numArray[4]*10 + numArray[5]) + ' thousandth'
		else:
			place += numToWords(numArray[3]*100+numArray[4]*10+numArray[5]) + ' thousand '
			if (not hasTrailingZeros(numArray)):
				place += numToPlace(numArray[6]*100+numArray[7]*10+numArray[8])

	if (num>=1000000 and num<=999999999):
		if (hasTrailingZeros(numArray)):
			place += numToWords(numArray[0]*100 + numArray[1]*10 + numArray[2]) + ' millionth'
		else:
			place += numToWords(numArray[0]*100+numArray[1]*10+numArray[2]) + ' million '
			if (not hasTrailingZeros(numArray)):
				place += numToPlace(numArray[3]*100000+numArray[4]*10000+numArray[5]*1000+numArray[6]*100+numArray[7]*10+numArray[8])
	place = ' '.join(place.split())
	return place

def main(num):
	number = input('Please enter a number: ')
	print 'Word:\t%s' % numToWords(number)
	print 'Place:\t%s' % numToPlace(number)
