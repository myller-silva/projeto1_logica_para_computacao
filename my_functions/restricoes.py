import pandas as pd 
from my_functions.list_manipulation import list_to_form
from LogiComp.formula import Atom, Implies, Not, Or, And
from LogiComp.semantics import satisfiability_brute_force
LE, GT, S = 'le', 'gt', 's '


def get_columns_names(dataframe=pd.DataFrame()):
  return dataframe.columns.to_list()


def number_of_patients(dataframe = pd.DataFrame()):
  return len(dataframe)


def get_attributes(dataframe = pd.DataFrame()):
  columns_names = get_columns_names(dataframe) 
  return columns_names[0:-1]

def dataframe_data_to_list(dataframe = pd.DataFrame()):
  return dataframe.values.tolist()

# ok
def restricao_um(dataframe = pd.DataFrame(), m_regras=1): 
  and_list = []
  attributes = get_attributes(dataframe)
  for attribute in attributes:     
    for i in range(0, m_regras):
      x1 = Atom(f'X{attribute},{i+1},{LE}')
      x2 = Atom(f'X{attribute},{i+1},{GT}')
      x3 = Atom(f'X{attribute},{i+1},{S}')  
      a = list_to_form( [   x1, Not(x2), Not(x3)], And )
      b = list_to_form( [Not(x1),    x2, Not(x3)], And )
      c = list_to_form( [Not(x1), Not(x2),    x3], And )
      and_list.append( list_to_form( [a, b, c], Or ) ) 
  and_form = list_to_form(and_list, And)  
  return and_form 


#ok
def restricao_dois(dataframe = pd.DataFrame(), m_regras=1):
  columns =  get_columns_names(dataframe)
  n = len(columns)-1
  and_list = []
  for i in range(0, m_regras):
    or_list = []
    for j in range(0, n):
      or_list.append( Not(Atom( f'X{columns[j]},{i+1},{S}' )) )
    and_list.append(list_to_form(or_list, Or))
  return list_to_form(and_list, And)


#ok
def restricao_tres(dataframe = pd.DataFrame(), m_regras=1):
  data_array = dataframe_data_to_list(dataframe)
  columns =  get_columns_names(dataframe)
  n_atributos = len(columns)-1
  and_list = [] 
  n = number_of_patients(dataframe)   
  for j in range(0, n):
    sem_patologia = data_array[j][-1]==0
    if(sem_patologia):
      for i in range(0, m_regras):
        or_list = []
        for a in range(0, n_atributos): 
          le_or_gt = LE if(data_array[j][a] != 1) else GT
          or_list.append( Atom(f'X{columns[a]},{i+1},{le_or_gt}') ) 
        if(len(or_list)!=0):
          and_list.append( list_to_form(or_list, Or) )
  return list_to_form(and_list, And)


#ok
def restricao_quatro(dataframe = pd.DataFrame(), m_regras=1):
  and_list = [] 
  attributes = get_attributes(dataframe)
  data_array = dataframe_data_to_list(dataframe)
  n = len(data_array) 

  for i in range(0, m_regras):
    for j in range(0, n):
      tem_patologia = data_array[j][-1] == 1 
      if(tem_patologia):
        for a in range(0, len(data_array[j])-1): 
          le_or_gt = LE if(data_array[j][a] == 0) else GT
          and_list.append(
            Implies(
              Atom( f'X{attributes[a]},{i+1},{le_or_gt}' ),
              Not( Atom( f'C{i+1},{j+1}' ) )
            )
          ) 
  return list_to_form(and_list, And)


#ok
def restricao_cinco(dataframe = pd.DataFrame(), m_regras=1): 
  n = len(dataframe)
  data_array = dataframe_data_to_list(dataframe)
  and_list = []
  for j in range(0, n):
    tem_patologia = data_array[j][-1]==1
    if(tem_patologia):
      or_list = []
      for i in range(0, m_regras):
        or_list.append((Atom(f'C{i+1},{j+1}')))
      if(len(or_list)!=0):
        and_list.append(list_to_form(or_list, Or)) 
  return list_to_form(and_list, And)


# cada regra deve cobrir pelo menos um paciente com patologia
def restricao_seis(dataframe = pd.DataFrame(), m_regras = 1):
  data_array = dataframe_data_to_list(dataframe)
  and_list = []
  n = len(data_array)
  for i in range(0, m_regras):
    or_list = []
    for j in range(0, n): 
      tem_patologia = data_array[j][-1] == 1 
      if(tem_patologia): 
        or_list.append(Atom(f'C{i+1},{j+1}')) 
    if(len(or_list) != 0):
      and_list.append(list_to_form(or_list, Or)) 
  return list_to_form(and_list, And)


def rule_set_generator(dataframe = pd.DataFrame() , interpretation={}, m_regras=1):
  set_of_rules = []
  attributes = get_attributes(dataframe)
  if(interpretation!=False):  
    for i in range(0, m_regras):
      rules = [] 
      for a in attributes:  
        temp = f'X{a},{i+1},{LE}'
        if((temp in interpretation) and (interpretation[temp] == True) ):
            rules.append(f'{a}') 
        temp = f'X{a},{i+1},{GT}'
        if((temp in interpretation) and (interpretation[temp] == True) ):
            rules.append(f'{a}'.replace("<=", ">")) 
      set_of_rules.append(rules)
  return set_of_rules


  
def solver( dataframe=pd.DataFrame(), m_regras=1 ): 
  arr = [
    restricao_um(dataframe, m_regras),
    restricao_dois(dataframe, m_regras),
    restricao_tres(dataframe, m_regras), 
    restricao_quatro(dataframe, m_regras),
    restricao_cinco(dataframe, m_regras), 
    # restricao_seis(dataframe, m_regras)
  ] 
  interpretation = satisfiability_brute_force( list_to_form(arr, And) )   
  set_of_rules = rule_set_generator(dataframe, interpretation, m_regras)     
  return set_of_rules



