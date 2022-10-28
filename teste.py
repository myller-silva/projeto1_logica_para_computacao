from LogiComp.formula import *
from LogiComp.functions import *
from my_functions.list_manipulation import list_to_form
p, q, t, r = Atom('p'), Atom('q'), Atom('t'), Atom('r')
form = And(
  p,
  And(
    q, 
    Or(
      t,
      r
    )
  )
)

print(form)
atoms_list = atoms(form)
print(atoms_list)
print(
  Or(
    Not(    list_to_form(atoms_list, And)),
    Not(p)
  )
)
