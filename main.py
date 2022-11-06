from my_functions import *
from LogiComp.formula import *
import LogiComp.functions as f
import pandas as pd
from my_functions.restricoes import *
from LogiComp.semantics import *



file = './pacientes_testes/column_bin_2a_3p.csv'
df = pd.read_csv(f'./{file}')
m_regras = 2

print(df)

s = solver(df, m_regras)
if(len(s)!=0):
  print("conjunto de regras: ")
  for rule in s:
    print(rule)
else:
  print(f'Nao é possivel definir um conjunto de regras com {m_regras} regra(s)')

