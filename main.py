from my_functions import *
from LogiComp.formula import *
import LogiComp.functions as f
import pandas as pd
from my_functions.restricoes import *
from LogiComp.semantics import *

def solver(file_csv = './file.csv', m_regras=1 ):
  dataframe = pd.read_csv(file_csv)
  arr = []
  arr.append(restricao_um(dataframe,m_regras))
  arr.append(restricao_dois(dataframe, m_regras))
  arr.append(restricao_tres(dataframe, m_regras))
  arr.append(restricao_quatro(dataframe, m_regras))
  arr.append(restricao_cinco(dataframe, m_regras))

  formula = list_to_form(arr, And)
  interpretation = satisfiability_brute_force(formula) 
  atributos = get_atributos(dataframe)
  set_rules = []
  for i in interpretation:
    print(f'{i}: {interpretation[i]}')
  if(interpretation!=False):
    for i in range(0, m_regras):
      rules = [] 
      for a in atributos: 
        # temp = (f'X{a},{i+1},{S}')
        # if(interpretation[temp] != True):
        temp = (f'X{a},{i+1},{LE}')
        if((temp in interpretation) and (interpretation[temp] == True) ):
            rules.append(f'{a}') 
        temp = (f'X{a},{i+1},{GT}')
        if((temp in interpretation) and (interpretation[temp] == True) ):
            rules.append(f'{a}'.replace("<=", ">"))

      if(len(rules)!=0):
        set_rules.append(rules)
  return set_rules


# file = 'arquivo_dos_pacientes/column_bin_3a_3p.csv'
file = 'teste.csv'
df = pd.read_csv(f'./{file}')

m_regras = 2

print(df)

r = solver(file, m_regras)

print(r)

# há regras que nao cobrem nenhum paciente







interpretation = {
  'XPI <= 42.09,2,le': True,
  'XPI <= 42.09,2,gt': False,
  'XPI <= 42.09,2,s ': False,
  'XPI <= 48.12,2,le': True,
  'XPI <= 48.12,2,gt': False,
  'XPI <= 48.12,2,s ': False,
  'XPI <= 54.92,2,le': False,
  'XPI <= 54.92,2,gt': True,
  'XPI <= 54.92,2,s ': False,
  'XPI <= 42.09,1,s ': True,
  'XPI <= 48.12,1,s ': True,
  'XPI <= 54.92,1,s ': False,
  'XPI <= 42.09,1,gt': True,
  'XPI <= 48.12,1,gt': True,
  'XPI <= 54.92,1,gt': True,
  'XPI <= 42.09,1,le': False,
  'XPI <= 48.12,1,le': False,
  'XPI <= 54.92,1,le': False,
  'C1,1': True,
  'C1,2': True,
  'C2,1': False,
  'C2,2': True
}

