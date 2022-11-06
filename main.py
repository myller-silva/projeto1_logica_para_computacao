from my_functions import *
from LogiComp.formula import *
import LogiComp.functions as f
import pandas as pd
from my_functions.restricoes import *
from LogiComp.semantics import *



# file = './pacientes_testes/exemplo_dado_no_pdf.csv'
file = './arquivo_dos_pacientes/column_bin_3a_3p.csv'
df = pd.read_csv(f'./{file}')
m_regras = 2

print(df)

set_of_rules = solver(df, m_regras)
if(len(set_of_rules)!=0):
  print("conjunto de regras: ")
  for rule in set_of_rules:
    print(rule)
else:
  print(f'Nao é possivel definir um conjunto de regras com {m_regras} regra(s)')

