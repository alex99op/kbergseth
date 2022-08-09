#åpner fil og lager liste
with open("bolla.txt", "r") as primtall_liste:
	lines = primtall_liste.readlines()
#print(lines)

#Alle tallene ender med /n, dermed er det en enkel måte å skille på dem. Evt må det også fjernes før man kan
#begynne å regne. Split opp evt ved en loop, eller så burde det vell finnes en smart funksjon å gjøre det på.

'''Psaudokode: skal ta ut hver linje fra filen bolla.txt
og legge til en liste, gå gjennom listen og plukke ut
primtallene og legge til en ny liste, deretter bruke 
long_to_bytes() for å finne flagget.
'''
def is_prime(liste):
	for i in liste:
		print(i)


is_prime(lines)
'''
def is_prime(n):
	for i in range(2,n):
		if(n%i) == 0
		return False
	return True

long_to_bytes(primtall_liste)
'''
