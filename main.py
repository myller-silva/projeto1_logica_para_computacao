from my_functions import *
from LogiComp.formula import *
import LogiComp.functions as f
import pandas as pd
from my_functions.restricoes import *
from LogiComp.semantics import *




file = 'exemplo_dado_no_pdf.csv'

df = pd.read_csv(f'./{file}')

print(df)
m_regras = 2
s = solver(file, m_regras)

for rule in s:
  print(rule)