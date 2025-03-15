## Zadatak 5: Izračun ostatka pri dijeljenju

'''
Napišite program koji traži od korisnika da unese dva cijela broja. 
Program treba izračunati i ispisati ostatak pri dijeljenju prvog broja drugim brojem.
'''

prvi_broj = int(input('Unesi prvi cijeli broj: '))
drugi_broj = int(input('Unesi drugi cijeli broj: '))

ostatak = prvi_broj % drugi_broj

print(f'Ostatak pri dijeljenju {prvi_broj} sa {drugi_broj} je: {ostatak}')

