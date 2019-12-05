from AES import *
from Caesar import *
from CBC import *
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

	driver(
		CBC,
		key = {"key": 0xB, "shift": 1, "C": 0x0, "block": 1},
		text = 0xA23A9,
		ciphertext = 0x27FDF,
	)

	driver(
		CBC,
		key = {"key": 0xA, "shift": 2, "C": 0x3, "block": 1},
		text = 0x1823A,
		ciphertext = 0x202EB,
	)

	driver(
		CBC,
		key = {"key": 0xC9F, "shift": 4*3 - 3, "C": 0x000, "block": 3},
		text = 0xC264A676E55A123,
		ciphertext = 0x217D458D6622D73,
	)

	driver(
		ECB,
		key = {"key" : 0xB, "shift": 1, "block": 1},
		text = 0xA23A9,
		ciphertext = 0x23124,
	)

	driver(
		AES,
		key = 0x133457799BBCDFF1133457799BBCDFF1,
		text = 0x0123456789ABCDEF0123456789ABCDEF,
		ciphertext = 0x2EB94DFF3CCCDB52022C4D9906B5B848,
	)

	driver(
		AES,
		key = 0x0F1571C947D9E8590CB7ADD6AF7F6798,
		text = 0x0123456789ABCDEFFEDCBA9876543210,
		ciphertext = 0xFF0B844A0853BF7C6934AB4364148FB9,
	)
