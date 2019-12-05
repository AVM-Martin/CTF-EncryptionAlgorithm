from AES import constants


def decompose_to_matrix(s):
	return [
		[ (s >> (128 - 8 - 32*i - 8*j)) & 0xFF for j in range(4) ]
		for i in range(4)
	]


def decompose_from_matrix(s):
	result = 0
	for i in range(4):
		for j in range(4):
			result = (result << 8) | s[i][j]

	return result

def transpose(s):
	return [ [ s[j][i] for j in range(4)] for i in range(4) ]


def substitute_bytes(s):
	return constants.SBOX[(s >> 4) & 0xF][s & 0xF]


def substitute_bytes_inverse(s):
	return constants.RSBOX[(s >> 4) & 0xF][s & 0xF]


def shift_rows(data):
	return [ data[i][i:] + data[i][:i] for i in range(4) ]


def shift_rows_inverse(data):
	return [ data[i][-i:] + data[i][:-i] for i in range(4) ]


def xtime(a):
	return (a << 1) ^ 0x11B if a & 0x80 else (a << 1)


def mix_columns(s):
	result = [ [ x for x in row ] for row in s ]

	for i in range(4):
		temp = s[0][i] ^ s[1][i] ^ s[2][i] ^ s[3][i]
		result[0][i] ^= temp ^ xtime(s[0][i] ^ s[1][i])
		result[1][i] ^= temp ^ xtime(s[1][i] ^ s[2][i])
		result[2][i] ^= temp ^ xtime(s[2][i] ^ s[3][i])
		result[3][i] ^= temp ^ xtime(s[3][i] ^ s[0][i])

	return result


def mix_columns_inverse(s):
	result = [ [ x for x in row ] for row in s ]

	for i in range(4):
		result[0][i] ^= xtime(xtime(s[0][i] ^ s[2][i]))
		result[1][i] ^= xtime(xtime(s[1][i] ^ s[3][i]))
		result[2][i] ^= xtime(xtime(s[0][i] ^ s[2][i]))
		result[3][i] ^= xtime(xtime(s[1][i] ^ s[3][i]))

	return mix_columns(result)


def xor(a, b):
	return [ [ a[i][j] ^ b[i][j] for j in range(4) ] for i in range(4) ]
