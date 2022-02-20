from random import choice,randint
from string import ascii_uppercase



def rannum(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return str(randint(range_start, range_end))
    


def ranchar(n):
 	return (''.join(choice(ascii_uppercase) for i in range(n)))




def encrypt(data):
	grn = rannum(len(data))
	grchr = ranchar(len(data))
	lst = [str.upper, str.lower]
	x = 0
	final_product = []
	for i in data:

		temp = ord(i) + int(grn[x])
		final_product.append(chr(temp))
		final_product.append(choice(lst)(grchr[x]))
		x+=1

	for k in grn:
		
		final_product.append(choice(lst)(ascii_uppercase[int(k)]))

	return ("".join(final_product))



def decrypt(data):
	mainlen = len(data)/3
	rmhash = data[(int(mainlen)*2):]
	mainhash = data[:-int(mainlen)]

	rannumber = []
	for ok in rmhash.upper():
		rannumber.append(ascii_uppercase.index(ok))

	#filtersmap
	main = []
	for i in range(len(mainhash)):
		if  i % 2 == 0:
			main.append(mainhash[i])

	final = []
	for i in  range(len(main)):
		final.append(chr( ord(main[i]) - rannumber[i]))
	return("".join(final))






