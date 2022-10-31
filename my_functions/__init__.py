from LogiComp.functions import atoms
from LogiComp.semantics import truth_value
from LogiComp.formula import And, Or, Implies, Atom, Not
from my_functions.list_manipulation import list_to_form


def print_dicionary(dicionary):
  for key in dicionary:
    print(f'{key}: {dicionary[key]}')



def my_satisfiability(formula): #ok
  list_atoms = atoms(formula)
  interpretation = {}
  for atom in list_atoms:
    interpretation[atom] = False
  return my_sat(formula, interpretation)

def my_sat(formula, interpretation): #ok
  # print(f'interpretation: {interpretation}')
  if(truth_value(formula, interpretation)):
    return interpretation
  else:
    last = None
    for key in interpretation:
      if(interpretation[key]==False):
        last = key
        interpretation[key] = True
        # print(f'interpretation: {interpretation}')
        if(truth_value(formula, interpretation)):
          return interpretation
        interpretation[key] = False
    if(last!=None): 
      interpretation[last] = True
      return my_sat(formula, interpretation)
    return False


#bug:
def duplo_satisfativel(formula):
  interpretation = my_satisfiability(formula)  
  if(interpretation!=False): 
    for atom in interpretation:
      temp = interpretation.copy()
      temp[atom] = not temp[atom]
      temp = my_sat(formula, temp)
      if(temp!=False and temp!=interpretation):
        return [interpretation, temp]
    return False
  else:
    return False

