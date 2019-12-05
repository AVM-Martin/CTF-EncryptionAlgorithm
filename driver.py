def driver(main_class, key, text, ciphertext):
	enc = main_class(key)
	cipher = enc.encrypt(text)

	dec = main_class(key)
	result = dec.decrypt(ciphertext)

	assert(result == text)
	assert(cipher == ciphertext)
