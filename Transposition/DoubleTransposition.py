from Transposition import Transposition


class DoubleTransposition(Transposition):
	def encrypt(self, text):
		return super().encrypt(super().encrypt(text))

	def decrypt(self, text):
		return super().decrypt(super().decrypt(text))
