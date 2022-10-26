import pandas as pd 
from LogiComp.formula import Atom, Implies, Not, Or, And

from restricoes import *



df = pd.read_csv('./exemplo_dado_no_pdf.csv')

print(df)

# restricao2 = restricao_dois(df)

p_diagnostico = df['P'].values.tolist()


print(  restricao_quatro(df) )

