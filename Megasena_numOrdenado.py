Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random

>>> def megasena():
	jogo = []
	while len(jogo) < 6:
		num = random.randint(1,60)
		if num in jogo:
			continue
		else:
			jogo.append(num)
	print(sorted(jogo))
