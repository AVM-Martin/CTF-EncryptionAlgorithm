def transform(c, delta):
	if 'A' <= c <= 'Z':
		c = (ord(c) - ord('A') + delta + 26) % 26
		return chr(c + ord('A'))

	elif 'a' <= c <= 'z':
		c = (ord(c) - ord('a') + delta + 26) % 26
		return chr(c + ord('a'))

	else:
		return c
