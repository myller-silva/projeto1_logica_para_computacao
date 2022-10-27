import pandas as pd 
from LogiComp.formula import Atom, Implies, Not, Or, And

from restricoes import *

def truth_value(formula=Atom(''), interpretation={}):
  if(isinstance(formula, Atom)):
    return interpretation[formula.name] 
  if(isinstance(formula, Not)):
    return not truth_value(formula.inner, interpretation )
  if(isinstance(formula, And)):
    return (
      truth_value(formula.left, interpretation)
      and
      truth_value(formula.right, interpretation)
    )
  if(isinstance(formula, Or)):
    return (
      truth_value(formula.left, interpretation)
      or
      truth_value(formula.right, interpretation)
    )
  if(isinstance(formula, Implies)):
    return (
      not (truth_value(formula.left, interpretation))
      or
      truth_value(formula.right, interpretation)
    )  
  raise TypeError('Formula ou interpretacao invalida')


# df = pd.read_csv('./exemplo_dado_no_pdf.csv')

# print(df)

# # restricao2 = restricao_dois(df)

# p_diagnostico = df['P'].values.tolist()

print("-"*30)
print("testando truth_value")
print("-"*30)

p = Atom('p')

formula = Or(
  p,
  Not(p)
)

interpretation = {
  'p': True
}

print(formula)

print(
  truth_value(
    formula, 
    interpretation
  )
)