'''Psaudokode: skal ta ut hver linje fra filen bolla.txt
og legge til en liste, gå gjennom listen og plukke ut
primtallene og legge til en ny liste, deretter bruke 
long_to_bytes() for å finne flagget.
'''
from sympy.ntheory import isprime
primtall=[]

#åpner fil og lager liste
with open("bolla.txt", "r") as primtall_liste:
	lines = primtall_liste.readlines()


def is_prime(liste):
	for i in liste:
		i.replace('\n', '')
		 #HER skal du legge inn hva man skal dele på for å finne ut om det er et primtall
		if (isprime(i)) == True:
			primtall.append(i)


is_prime(lines)
print(primtall)
'''
def is_prime(n):
	for i in range(2,n):
		if(n%i) == 0
		return False
	return True

long_to_bytes(primtall_liste)
'''
