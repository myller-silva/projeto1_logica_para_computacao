from msilib.schema import Error
import pandas as pd
# import pysat.formula 
from LogiComp.formula import Atom, Or, And

def list_to_form(or_list = [] , Form=And):
  n = len(or_list)
  if(n==0):
    raise OverflowError('Lista vazia')
  
  formula =  Atom(or_list[0])
  for i in range(1, n):
    formula = Form(formula, or_list[i])
  return formula


def quinta_restricao(data_frame = pd.DataFrame() , n=3, m=4): 
  # AndZao(1 a n ) OrZao(1 a m) C(i,j)
  # Cada paciente com patologia deve ser coberto por alguma das regras.
  # m é o numero de regras que estamos verificando se é possivel obter para classificar corretamente todos os pacientes
  # n é o numero de pacientes
  #  
  and_list = list()
  for i in range(0, n):
    or_list = list()
    for j in range(0, m): 
      or_list.append(f'C{i+1},{j+1}')
    print(list_to_form(or_list, Or))
    and_list.append(or_list)
  return and_list
 




file_name = 'column_bin_3a_2p.csv'
data = pd.read_csv(f'./arquivo_dos_pacientes/{file_name}')
print(data)

print("quinta restricao: ")
and_list = quinta_restricao(data)


print('\n\n\n')
print( pd.DataFrame(and_list) ) 


list_to_form([])