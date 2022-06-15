import random
from time import sleep
def resultado(t):
	print('=' * 10)
	print(f'{t}')
	print('=' * 10)


def naipe():
	if '♧' in p1:
		sleep(1)
		resultado('WIN')
	elif '♧' in p2:
		sleep(1)
		resultado('LOSE')
	elif '♡' in p1:
		sleep(1)
		resultado('WIN')
	elif '♡' in p2:
		sleep(1)
		resultado('LOSE')
	elif '♤' in p1:
		sleep(1)
		resultado('WIN')
	elif '♤' in p2:
		sleep(1)
		resultado('LOSE')
	elif '◇' in p1:
		sleep(1)
		resultado('WIN')
	elif '◇' in p2:
		sleep(1)
		resultado('LOSE')

def vira():
	if Cards.get(mesa) == 13:
		num = 4
	else:
		num = Cards.get(mesa) + 1
	valor = list(Cards.values())
	posição1 = valor.index(num)
	return posição1
	
count = 0
while count <= 5:
	count += 1	
	
	Cards = {'4◇' : 4, '4♤' : 4, '4♡' : 4, '4♧' : 4, '5◇' : 5, '5♤' : 5, '5♡' : 5, '5♧' : 5, '6◇' : 6, '6♤' : 6, '6♡' : 6, '6♧' : 6, '7◇' : 7, '7♤' : 7, '7♡' : 7, '7♧' : 7, 'Q◇' : 8, 'Q♤' : 8, 'Q♡' : 8, 'Q♧' : 8, 'J◇' : 9, 'J♤' : 9, 'J♡' : 9, 'J♧' : 9, 'K◇' : 10, 'K♤' : 10, 'K♡' : 10, 'K♧' : 10, 'A◇' : 11, 'A♤' : 11, 'A♡' : 11, 'A♧' : 11, '2◇' : 12, '2♤' : 12, '2♡' : 12, '2♧' : 12,'3◇' : 13, '3♤' : 13, '3♡' : 13, '3♧' : 13}
	
	p1 = random.sample(list(Cards.keys()), 1)
	p1 = p1[0]
	Cards_Copy = Cards.copy()
	del Cards_Copy[p1]
	p2 = random.choice(list(Cards_Copy.keys()))
	Cards_Copy2 = Cards_Copy.copy()
	del Cards_Copy2[p2]
	mesa = random.choice(list(Cards_Copy2.keys()))
	print(f'Suas Cartas :{p1}\n')
	print(f'Vira        :{mesa}')
	print(f'\nCartas da IA:{p2}')
	chaves = list(Cards.keys())
	Cards.update({chaves[vira()] : 14})
	Cards.update({chaves[vira()] : 14})
	Cards.update({chaves[vira()] : 14})
	Cards.update({chaves[vira()] : 14})
	if Cards.get(p1) > Cards.get(p2):
		sleep(1)
		resultado('WIN')
	elif Cards.get(p1) < Cards.get(p2):
		sleep(1)
		resultado('LOSE')
	else:
		naipe()
	sleep(5)
