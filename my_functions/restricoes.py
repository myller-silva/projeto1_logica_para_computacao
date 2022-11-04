import pandas as pd 
from my_functions.list_manipulation import list_to_form
from LogiComp.formula import Atom, Implies, Not, Or, And
from LogiComp.semantics import satisfiability_brute_force
LE, GT, S = 'le', 'gt', 's '



def formula_sem_parenteses(formula):
  s = str(formula)
  new_s ='' 
  for c in s:
    if(c not in ['(', ')']):
      new_s += c 
  return new_s


def get_columns_names(dataframe=pd.DataFrame()):
  return dataframe.columns.to_list()


def number_of_patients(dataframe = pd.DataFrame()):
  return len(dataframe)


def show_data_list(data_list=[[], []]):
  for l in data_list:
    for c in l:
      print(c, end=' ')
    print()



def restricao_um(dataframe = pd.DataFrame(), m_regras=2): 
  and_list = []
  atributos = get_atributos(dataframe)
  for at in atributos:     
    for i in range(0, m_regras):
      x1 = Atom(f'X{at},{i+1},{LE}')
      x2 = Atom(f'X{at},{i+1},{GT}')
      x3 = Atom(f'X{at},{i+1},{S}') 
      form = Or(
              And(
                Not(x1),
                And(
                  Not(x2),
                  x3
                )
              ),
              Or(    
                And(
                  Not(x2),
                  And(
                    Not(x3),
                    x1
                  )
                ),    
                And(
                  Not(x3),
                  And(
                    Not(x1),
                    x2
                  )
                )
              )
            )


    and_list.append( form )
  and_form = list_to_form(and_list, And) 
  # print(type(and_form))
  return and_form 


#ok
def restricao_dois(dataframe = pd.DataFrame(), m_regras=2): # ok
  # Cada regra deve ter algum atributo aparecendo nela.
  # AndZao(1 a m)
  # OrZao (1 a n) variando a coluna 
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
def restricao_tres(dataframe = pd.DataFrame(), m_regras=2):
  data_array = dataframe.values.tolist()
  columns =  get_columns_names(dataframe)
  n_atributos = len(columns)-1
  and_list = [] 
  n = number_of_patients(dataframe)   
  for j in range(0, n):
    if(data_array[j][-1]==0):
      for i in range(0, m_regras):
        or_list = []
        for a in range(0, n_atributos):
          if(data_array[j][a] != 1):
            or_list.append( (
              Atom(f'X{columns[a]},{i+1},{LE}')
            ))
          else:
            or_list.append( (
              Atom(f'X{columns[a]},{i+1},{GT}')
            ))
        and_list.append( list_to_form(or_list, Or) )
  return list_to_form(and_list, And)



def get_atributos(dataframe = pd.DataFrame()):
  columns_names = get_columns_names(dataframe) 
  return columns_names[0:-1]


#ok
def restricao_quatro(dataframe = pd.DataFrame(), m_regras=2):
  and_list = [] 
  atributos = get_atributos(dataframe)
  data_array = dataframe.values.tolist()
  n = len(data_array) 

  for i in range(0, m_regras):
    for j in range(0, n):
      tem_patologia = data_array[j][-1] == 1 
      if(tem_patologia):
        for a in range(0, len(data_array[j])-1):
          or_list = []
          if(data_array[j][a] == 0): 
            or_list.append(
              Implies(
                Atom( f'X{atributos[a]},{i+1},{LE}' ),
                Not(Atom( f'C{i+1},{j+1}' ))
              )
            )
          else:
            or_list.append(
              Implies(
                Atom( f'X{atributos[a]},{i+1},{GT}' ),
                Not(Atom( f'C{i+1},{j+1}' ))
              )
            )
          and_list.append(list_to_form(or_list, Or)) 
  return list_to_form(and_list, And)


#ok
def restricao_cinco(dataframe = pd.DataFrame(), m_regras=2): 
  n = len(dataframe)
  data_array = list(dataframe.values)
  and_list = []
  for j in range(0, n):
    if(data_array[j][-1]==1):
      or_list = []
      for i in range(0, m_regras):
        or_list.append((Atom(f'C{i+1},{j+1}')))
      and_list.append(list_to_form(or_list, Or))
    else:
      for i in range(0, m_regras):
        and_list.append(Not(Atom(f'C{i+1},{j+1}')))
  return list_to_form(and_list, And)



#cada regra deve cobrir pelo menos um paciente 
def restricao_seis(df, m):
  n = len(list(df.values))
  and_list = []
  for i in range(0, m):
    or_list = []
    for j in range(0, n):
      or_list.append(Atom(f'C{i+1},{j+1}'))
    and_list.append(list_to_form(or_list, Or))
  return list_to_form(and_list, And)
        
  



  
def solver(file_csv = './file.csv', m_regras=1, inter={} ):
  dataframe = pd.read_csv(file_csv)
  arr = [
    restricao_um(dataframe, m_regras),
    restricao_dois(dataframe, m_regras),
    restricao_tres(dataframe, m_regras), 
    restricao_quatro(dataframe, m_regras),
    restricao_cinco(dataframe, m_regras) ,
    restricao_seis(dataframe, m_regras)
  ]
  formula = list_to_form(arr, And) 
  interpretation = satisfiability_brute_force(formula)  
  atributos = get_atributos(dataframe)
  set_rules = []
  
  if(interpretation!=False): 
    for atom in interpretation:
      inter[atom] = interpretation[atom]
    for i in range(0, m_regras):
      rules = [] 
      for a in atributos: 
        # temp = (f'X{a},{i+1},{S}')
        # if((temp in interpretation) and (interpretation[temp] == True) ):
        #   continue
        
        temp = (f'X{a},{i+1},{LE}')
        if((temp in interpretation) and (interpretation[temp] == True) ):
            rules.append(f'{a}') 
        temp = (f'X{a},{i+1},{GT}')
        if((temp in interpretation) and (interpretation[temp] == True) ):
            rules.append(f'{a}'.replace("<=", ">"))
      # if(len(rules)!=0):
      set_rules.append(rules)
  else:
    return "insatisfativel"
    
  return set_rules