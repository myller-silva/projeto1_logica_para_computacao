from pysat.formula import *
from pysat.solvers import *
import pandas as pd
from LogiComp.formula import * 
from my_functions.list_manipulation import list_to_form

# var_pool = IDPool()

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



from LogiComp.formula import *
from LogiComp.functions import atoms, is_negation_normal_form


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


print()
p = Atom('p')
q = Atom('q')
r = Atom('r')
s = Atom('s')


formula = Not(p)


a = atoms(formula)
print(formula)
print(a)














def quarta_restricao(matriz, numero_regras):
    '''
    Restrição original: (X49,02_1_p -> ~C_1_1) ∧ (X72,62_1_p -> ~C_1_1) ∧ (X80,61_1_n -> ~C_1_1) ∧
                             (X37,89_1_p -> ~C_1_1) ∧ (X57,55_1_n -> ~C_1_1) ∧ ....

    Restrição CNF: (~X49,02_1_p v ~C_1_1) ∧ (~X72,62_1_p v ~C_1_1) ∧ (~X80,61_1_n v ~C_1_1) ∧
                             (~X37,89_1_p v ~C_1_1) ∧ (~X57,55_1_n v ~C_1_1) ∧ ....
    '''

    and_list = []
    for i in range(0, numero_regras):
        for j in range(1, len(matriz)):
            if (int(matriz[j][-1]) == 1):
                for a in range(len(matriz[j]) - 1):
                    or_list = []
                    if (int(matriz[j][a]) == 0):
                        or_list.append(-var_pool.id(str(matriz[0][a]) + '_' + str(i+1) + '_p'))
                        or_list.append(-var_pool.id('C' + '_' + str(i+1) + '_' + str(j)))
                    elif (int(matriz[j][a]) == 1):
                        or_list.append(-var_pool.id(str(matriz[0][a]) + '_' + str(i+1) + '_n'))
                        or_list.append(-var_pool.id('C' + '_' + str(i+1) + '_' + str(j)))
                    if (len(or_list) > 0):
                        and_list.append(or_list)
    return and_list



file = './exemplo_dado_no_pdf.csv'
df = pd.read_csv(file)

print("_"*40)

print(df)

print("_"*40)

print(df.values.tolist())

print("_"*40)

print(temp_restricao_4(df))