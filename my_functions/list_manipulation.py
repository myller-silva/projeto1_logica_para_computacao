from LogiComp.formula import And, Or, Implies, Not, Atom

def subTree(list = [],  Form=And): 
  length = len(list)
  if( length==0 ): 
    return None
  midpoint = length//2
  if( length%2==0 ):
    first_half = list[0 : midpoint]
    second_half = list[midpoint : length] 
    return Form( subTree( first_half,  Form ) , subTree(second_half,  Form) )
  else:   
    quite = list[midpoint] 
    first_half = list[0:midpoint]
    second_half = list[midpoint+1 : length]
    l = subTree( first_half, Form ) 
    r = subTree( second_half, Form )
    if( l==None and r==None ): 
      return quite
    if( l!=None and r!=None ): 
        return Form( Form(l, quite) , r)
    if( l==None ): 
      return Form(quite, r)
    else: 
      return Form(l, quite)
    

def list_to_form(list = [], Form = And):
  tree = subTree(list, Form)
  return tree

