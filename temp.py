from pysat.formula import *
from pysat.solvers import *
import pandas as pd
from LogiComp.formula import * 
from my_functions.list_manipulation import list_to_form

# var_pool = IDPool()






file = './exemplo_dado_no_pdf.csv'
df = pd.read_csv(file)

print("_"*40)

print(df)

print("_"*40)

print(df.values.tolist())

print("_"*40)

print(temp_restricao_4(df))