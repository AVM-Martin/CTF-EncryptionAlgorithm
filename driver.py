from Caesar import *
from DES import *
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

	driver(
		Caesar,
		key = 2,
		text = "EASY TO BREAK",
		ciphertext = "GCUA VQ DTGCM",
	)

	driver(
		DES,
		key = 0x133457799BBCDFF1,
		text = 0x0123456789ABCDEF,
		ciphertext = 0x85E813540F0AB405,
	)
