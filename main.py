import pandas as pd 
from LogiComp.formula import Atom, Implies, Not, Or, And

from my_functions.restricoes import *



df = pd.read_csv('./exemplo_dado_no_pdf.csv')

print(df)

# p_diagnostico = df['P'].values.tolist()



print("-"*30)
print("restricao 1:")
print( restricao_um(df))



print("-"*30)
print("restricao 2:")
print( restricao_dois(df))

print("-"*30)
print("restricao 3:")
print( restricao_tres(df) )

# print("-"*30)
# print("restricao 4:")
# print( restricao_quatro(df) ) #erro


print("-"*30)
print("restricao 5:")
print( restricao_cinco(df) )
