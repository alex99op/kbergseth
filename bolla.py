#åpner fil og lager liste
with open("bolla.txt", "r") as primtall_liste:
	lines = primtall_liste.readlines()
print(lines)

#Alle tallene ender med /n, dermed er det en enkel måte å skille på dem. Evt må det også fjernes før man kan
#begynne å regne. Tror tallene blir sett på som en string siden den har en bokstav bak seg og da går det ikke å 
#Slette 

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
