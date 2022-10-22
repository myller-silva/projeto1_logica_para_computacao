import pandas as pd 
from LogiComp.formula import Atom, Or, And


def show_data_list(data_list=[[], []]):
  for l in data_list:
    for c in l:
      print(c, end=' ')
    print()



def list_to_form(or_list = [], Inner=Atom, Form=And):
  n = len(or_list)

  if(n==0):
    raise OverflowError('Lista vazia')
  
  formula = Inner(or_list[0])
  for i in range(1, n):
    formula = Form(formula, Inner(or_list[i]))
  return formula


def quinta_restricao(data_list = [], n=3, m=4): 
  # AndZao(1 a n ) OrZao(1 a m) C(i,j)
  # Cada paciente com patologia deve ser coberto por alguma das regras.
  # m é o numero de regras que estamos verificando se é possivel obter para classificar corretamente todos os pacientes
  # n é o numero de pacientes

  and_list = list()
  for i in range(0, n):
    or_list = list()
    for j in range(0, m): 
      or_list.append(f'C{i+1},{j+1}')
    and_list.append( list_to_form(or_list, Atom, Or) )
  return list_to_form(and_list, Atom, And)
 

def restricao_dois(data_list = [], n=3, m=4):
  and_list = list()
  # AndZao(1 a m )
  # OrZao

  return


# file_name = 'column_bin_3a_2p.csv'
# dir = f'./arquivo_dos_pacientes/{file_name}'
# df = pd.read_csv(dir) 


df = pd.read_csv('./exemplo_dado_no_pdf.csv')
data_list = df.values.tolist()

# print(df)
