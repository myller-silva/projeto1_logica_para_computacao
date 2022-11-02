from my_functions import *
from LogiComp.formula import *
import LogiComp.functions as f
import pandas as pd

from my_functions.restricoes import *
from LogiComp.semantics import *

def solver(file_csv = './file.csv', m_regras=1 ):
  dataframe = pd.read_csv(file_csv)
  arr = []

  n = number_of_patients(dataframe) 

  arr.append(restricao_um(dataframe,m_regras))
  arr.append(restricao_dois(dataframe, m_regras))
  arr.append(restricao_tres(dataframe, m_regras))
  arr.append(restricao_quatro(dataframe, m_regras))
  arr.append(restricao_cinco(dataframe, m_regras))

  formula = list_to_form(arr, And)
  interpretation = satisfiability_brute_force(formula) 
  atributos = get_atributos(dataframe)
  set_rules = []
  if(interpretation!=False):
    for i in range(0, m_regras):
      rules = []
      #gerar regras
      for a in atributos:
      # set_rules.append(f'regra[{c}]')
        temp = (f'X{a},{i+1},{"le"}')
        if( (interpretation[temp] == True) ):
          rules.append(f'{a}')
          # continue
        temp = (f'X{a},{i+1},{"gt"}')
        if( (interpretation[temp] == True) ):
          rules.append(f'{a.replace("<=", ">")}')

      if(len(rules)!=0):
        set_rules.append(rules)
  return set_rules


file = 'arquivo_dos_pacientes/column_bin_3a_2p.csv'
df = pd.read_csv(f'./{file}')

m_regras = 1

print(df)

r = solver(file, m_regras)

# print(r)
for regra in r:
  print(regra)
