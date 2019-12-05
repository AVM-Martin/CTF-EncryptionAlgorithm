from Transposition import *


def driver(main_class, key, text, ciphertext):
	enc = main_class(key)
	cipher = enc.encrypt(text)

	dec = main_class(key)
	result = dec.decrypt(ciphertext)

	assert(result == text)
	assert(cipher == ciphertext)


if __name__ == "__main__":
	driver(
		Transposition,
		key = (2,0,3,4,1,),
		text = "enemyattackstonightz",
		ciphertext = "ettheakimaotycnzntsg",
	)

	driver(
		DoubleTransposition,
		key = (2,0,3,4,1,),
		text = "enemyattackstonightz",
		ciphertext = "tiyteaozhmcseangtktn",
	)
