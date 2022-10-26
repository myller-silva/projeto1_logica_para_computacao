import pandas as pd 
from LogiComp.formula import Atom, Implies, Not, Or, And




def formula_sem_parenteses(formula):
  s = str(formula)
  new_s ='' 
  for c in s:
    if(c not in ['(', ')']):
      new_s += c 
  return new_s


def get_columns_names(dataframe=pd.DataFrame()):
  return dataframe.columns.to_list()



def show_data_list(data_list=[[], []]):
  for l in data_list:
    for c in l:
      print(c, end=' ')
    print()




def list_to_form(or_list = [], Form=And):
  n = len(or_list)

  if(n==0):
    raise OverflowError('Lista vazia')
  
  formula = or_list[0]
  for i in range(1, n):
    formula = Form(formula, or_list[i] )
  return formula






def restricao_dois(dataframe = pd.DataFrame(), n=3, m=4):
  # Cada regra deve ter algum atributo aparecendo nela.
  # AndZao(1 a m)
  # OrZao (1 a n) variando a coluna

  columns =  get_columns_names(dataframe)
  n = len(columns)-1
  and_list = []
  for i in range(0, m):
    or_list = []
    for j in range(0, n):
      or_list.append( Not(Atom( f'X{columns[j]},{i+1},s' )) )
    and_list.append(list_to_form(or_list, Or))
  return list_to_form(and_list, And)




def restricao_tres(dataframe = pd.DataFrame(), m_regras=4): # quase ok
  # Para cada paciente sem patologia e cada regra, algum atributo do paciente n˜ao pode ser aplicado à regra.
  data_array = dataframe.values.tolist()
  columns =  get_columns_names(dataframe)
  n_atributos = len(columns)-1
  and_list = []

  n = len(data_array)
  
  for j in range(0, n):
    if(data_array[j][-1]==0):
      for i in range(0, m_regras):
        or_list = []
        for a in range(0, n_atributos):
          if(data_array[j][a]==1):
            or_list.append( Atom( f'X{columns[a]},{i+1},gt') )
          else:
            or_list.append( Atom( f'X{columns[a]},{i+1},le') )
        and_list.append( list_to_form(or_list, Or) )
  return list_to_form(and_list, And)




  
#pedir ajuda na restricao 4



def restricao_quatro(dataframe= pd.DataFrame(), m_regras=4):
  # Para cada paciente com patologia, cada regra e cada atributo, 
  # se o atributo do paciente não se aplicar ao da regra, 
  # então a regra não cobre esse paciente.
  data_array = dataframe.values.tolist()
  columns =  get_columns_names(dataframe)
  n_atributos = len(columns)-1
  and_list = []

  # n = len(data_array)

  for j in range(0, n_atributos):
    if(data_array[j][-1]==1):
      for i in range(0, m_regras):
        for a in columns:
          pass













def restricao_cinco(dataframe = pd.DataFrame(), n=3, m=4): # ok
  # AndZao(1 a n ) OrZao(1 a m) C(i,j)
  # Cada paciente com patologia deve ser coberto por alguma das regras.
  # m é o numero de regras que estamos verificando se é possivel obter para classificar corretamente todos os pacientes
  # n é o numero de pacientes

  and_list = []
  for i in range(0, n):
    or_list = []
    for j in range(0, m): 
      or_list.append( Atom( f'C{i+1},{j+1}' ) )
    and_list.append( list_to_form(or_list, Or) )
  return list_to_form( and_list, And )
 