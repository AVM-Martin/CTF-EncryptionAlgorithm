from DES import constants


def shift_left(key, x):
	return ((key << x) | (key >> (28 - x))) & 0xFFFFFFF


def split(s, length):
	return (
		s >> (length >> 1),
		s & ((1 << (length >> 1)) - 1),
	)


def permute_PC1(s):
	result = 0
	for i in range(56):
		POSITION = 64 - constants.PC1[i]
		result |= ((s >> POSITION) & 0x1) << (56 - 1 - i)

	return result


def permute_PC2(s):
	result = 0
	for i in range(48):
		POSITION = 56 - constants.PC2[i]
		result |= ((s >> POSITION) & 0x1) << (48 - 1 - i)

	return result


def permute_init(s):
	result = 0
	for i in range(64):
		POSITION = 64 - constants.INITIAL_PERMUTATION_TABLE[i]
		result |= ((s >> POSITION) & 0x1) << (64 - 1 - i)

	return result


def permute_inverse(s):
	result = 0
	for i in range(64):
		POSITION = 64 - constants.INVERSE_PERMUTATION_TABLE[i]
		result |= ((s >> POSITION) & 0x1) << (64 - 1 - i)

	return result


def expand(s):
	result = 0
	for i in range(48):
		POSITION = 32 - constants.EXPANSION_TABLE[i]
		result |= ((s >> POSITION) & 0x1) << (48 - 1 - i)

	return result


def sbox(s, idx):
	x = ((s >> 4) & 0x2) | (s & 0x1)
	y = (s >> 1) & 0xF
	return constants.SBOX[idx][x][y]


def feistel(s, K):
	s = expand(s) ^ K
	box = [ (s >> (48 - 6 - 6*i)) & 0x3F for i in range(8) ]

	s = 0
	for i in range(8):
		s |= sbox(box[i], i) << (32 - 4 - 4*i)

	result = 0
	for i in range(32):
		POSITION = 32 - constants.PERMUTATION_TABLE[i]
		result |= ((s >> POSITION) & 0x1) << (32 - 1 - i)

	return result
