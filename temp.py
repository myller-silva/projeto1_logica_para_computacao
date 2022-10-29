from pysat.formula import *
from pysat.solvers import *
import pandas as pd
from LogiComp.formula import * 
from my_functions.list_manipulation import list_to_form 
from LogiComp.functions import atoms



var_pool = IDPool()


#restricao_quatro:
def temp_restricao_4(dataframe = pd.DataFrame([[], []]), m_regras=4):
    # Para cada paciente sem patologia e cada regra, 
    # algum atributo do paciente n˜ao pode ser aplicado à regra.

    # Para cada paciente com patologia, cada regra e cada atributo, se o atributo do paciente n˜ao se aplicar
    # ao da regra, ent˜ao a regra n˜ao cobre esse paciente
    and_list = []
    
    data = dataframe.values.tolist()
 

    for i in range (0, m_regras):
        for j in range(1, len(data)):
            if(data[j][-1] == 1):
                for a in range(0, len(data[j])-1):
                    or_list = []
                    if(data[j][a] == 0):
                        or_list.append(Not(f'C{data[0][a]},{i+1},p'))
                        or_list.append(Not(f'C{i+1},{j}')) 
                    and_list.append(list_to_form(or_list, Or))
    return list_to_form( and_list, And )


 

# ***********

 
def satisfiablity_checking(formula): #força bruta
  list_atoms = atoms(formula)
  interpretation = [] #conjunto vazio
  return sat(formula, list_atoms, interpretation)


def UniaoDeConjuntos(interpretacao, interpretacao2): #obs 
  intercecao = None
  return interpretacao + interpretacao2 - intercecao

def sat(formula, atoms, interpretation):
  if(len(atoms)==0):
    if(truth_value(formula, interpretation)):
      return interpretation
    else:
      False 
    
  atom = atoms.pop()
  interpretation1 = UniaoDeConjuntos(interpretation, {atom, True})
  interpretation2 = UniaoDeConjuntos(interpretation, {atom, False})
  result = sat(formula, atoms, interpretation1)
  if(result!= False):
    return result
  return sat(formula, atoms, interpretation2)
  

def truth_value():
  pass
 