#åpner fil og lager liste
with open("bolla.txt", "r") as primtall_liste:
	lines = "bolla.txt".readlines()
print(lines)

'''Psaudokode: skal ta ut hver linje fra filen bolla.txt
og legge til en liste, gå gjennom listen og plukke ut
primtallene og legge til en ny liste, deretter bruke 
long_to_bytes() for å finne flagget.

def is_prime():
	for i in lines:
		if (num%i) == 0:




def is_prime(n):
	for i in range(2,n):
		if(n%i) == 0
		return False
	return True

long_to_bytes(primtall_liste)
'''
