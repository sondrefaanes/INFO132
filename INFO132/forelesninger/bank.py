# class Bankkonto:
#     kontonummer = None
#     navn = None
#     saldo = None
#     rentesats = None

#     neste_kontonummer = 10000

#     def __init__(self, navn, saldo=0.0, rentesats = 1.5):
#         self.navn = navn
#         self.saldo = saldo
#         self.rentesats = rentesats
#         self.kontonr = Bankkonto.neste_kontonummer
#         Bankkonto.neste_kontonummer += 1

#     def innskudd(self, beløp):
#         self.saldo += beløp
    
#     def uttak(self, beløp):
#         if beløp >= self.saldo:
#             self.saldo -= beløp 
                
#     def skriv_ut(self):
#         print(self.kontonummer,self.navn,self.saldo,self.rentesats)

# ole = Bankkonto("Ole Olsen", saldo = 1000)
# ole.skriv_ut()

x = "123"
print(x.isnumeric())

