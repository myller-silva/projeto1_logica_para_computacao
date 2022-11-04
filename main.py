from my_functions import *
from LogiComp.formula import *
import LogiComp.functions as f
import pandas as pd
from my_functions.restricoes import *
from LogiComp.semantics import *




file = 'arquivo_dos_pacientes/column_bin_3a_3p.csv'

df = pd.read_csv(f'./{file}')

m_regras = 2

print(df)

r = solver(file, m_regras)

print(r)
