import os ; os.system("cls")

# 1
print("Oppgave 1:")
Alder = int(input("Hvor gamel er du?: "))
if Alder <= 12:
    Billettpris = 80
elif Alder >= 18:
    Billettpris = 140
else:
    Billettpris = 100
print(f"Du er {Alder} år gamel, så din billetpris blir: {Billettpris}kr")

# 2
print("\nOppgave 2:")
summen = 0
for tall in range (2, 101):
    if tall % 2 == 0:
        summen += tall
        print(tall)
print(f"Total summen av alle partallene er: {summen}\n")

summen = 0
tall = 0
while tall != 100:
    tall += 1
    if tall % 2 == 0:
        summen += tall
        print(tall)
print(f"Total summen av alle partallene er: {summen}")

# 3
print("\nOppgave 3:")
def gjennomsnitt(liste):
    if liste == []:
        return print("Listen er tom")
    else:
        gjennomsnitt = sum(liste)/len(liste)
        return print(f"Gjennomsnitt av listen er: {gjennomsnitt}")
gjennomsnitt([1, 2, 3])
gjennomsnitt([10, 20, 30, 40])
gjennomsnitt([])

# 4
print("\nOppgave 4")
karakterregister = {
    "Per" : 5,
    "Kari" : 4,
    "Ola" : 6
}
with open("Python/VG2/karakterer", "w", encoding="utf-8") as fil:
    for key, value in karakterregister.items():
        fil.write(f"{key}: {value}\n")

with open("Python/VG2/karakterer", "r", encoding="utf-8") as fil:
    for line in fil:
        key, value = line.strip().split(":", 1)
        karakterregister[key] = int(value)
print(karakterregister)
gjennomsnitt_karakter = sum(karakterregister.values())/len(karakterregister)
print(f"Gjennomsnittet til alle karakterene er: {gjennomsnitt_karakter}")

# 5
print("\nOppgave 5")
class Motorsykkel:
    def __init__(self, merke, hastighet, antallKM):
        self.merke = merke
        self.hastighet = hastighet
        self.antallKM = antallKM
    
    def økerKM(self, nyDistanse):
        self.antallKM += nyDistanse
    
    def skrivUt(self):
        print(f"Motorsykkel info - \nMerke: {self.merke} \nHastighet: {self.hastighet} \nAntall Km: {self.antallKM}")

Ny_Motorsykel = Motorsykkel("BMW", 200, 300)
Ny_Motorsykel.økerKM(200)
Ny_Motorsykel.skrivUt()