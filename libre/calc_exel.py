"""Tips and tricks calc/exel tables about. Primitive little bit."""

#1 Sum
=SUM(A1:A4)  # apply from one cell result to another, A1+A2+A3+A4

#2 Count currency

=A4*VLOOKUP(B4,F4:G11,2,FALSE)
# A4 = 100, B4 = EUR, D4 = answer, F4-11 = name of money, G4-11 = currency

#3 
