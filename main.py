import pandas as pd 
from LogiComp.formula import Atom, Implies, Not, Or, And

from my_funcions.restricoes import *



df = pd.read_csv('./exemplo_dado_no_pdf.csv')

print(df)

p_diagnostico = df['P'].values.tolist()


print(  restricao_quatro(df) )

