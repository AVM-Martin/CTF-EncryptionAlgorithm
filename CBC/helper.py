def shift_left(key, x, length):
	return ((key << x) | (key >> (length - x))) & ((1 << length) - 1)
