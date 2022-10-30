"""The goal in this module is to define functions associated with the semantics of formulas in propositional logic. """


from LogiComp.formula import *
from LogiComp.functions import atoms




def truth_value(formula=Atom('atom'), interpretation=dict()):
    """Determines the truth value of a formula in an interpretation (valuation).
    An interpretation may be defined as dictionary. For example, {'p': True, 'q': False}.
    """  
    if(isinstance(formula, Atom)):
        try:
            return interpretation[formula.name] 
        except: 
            raise KeyError(f"Atomica {formula.name} nao encontrada na interpretacao {interpretation}")
    if(isinstance(formula, Not)):
        return (not truth_value(formula.inner, interpretation ))
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
            (not truth_value(formula.left, interpretation))
            or
            truth_value(formula.right, interpretation)
        )  
    raise TypeError('Formula ou interpretacao invalida')



def is_logical_consequence(premises, conclusion):  # function TT-Entails? in the book AIMA.
    """Returns True if the conclusion is a logical consequence of the set of premises. Otherwise, it returns False."""
    pass
    # ======== YOUR CODE HERE ========


def is_logical_equivalence(formula1, formula2):
    """Checks whether formula1 and formula2 are logically equivalent."""
    pass
    # ======== YOUR CODE HERE ========


def is_valid(formula):
    """Returns True if formula is a logically valid (tautology). Otherwise, it returns False"""
    pass
    # ======== YOUR CODE HERE ========


def satisfiability_brute_force(formula):
    """Checks whether formula is satisfiable.
    In other words, if the input formula is satisfiable, it returns an interpretation that assigns true to the formula.
    Otherwise, it returns False.""" 
    list_atoms = atoms(formula)
    interpretation = {}
    return sat(formula, list_atoms, interpretation)


def sat(formula=Atom('p'), list_atoms=['p'], interpretation=dict(), pointer = 0 ): 
    # print(f'{formula} {list_atoms} {interpretation}')
    if( len(list_atoms) == pointer ):
        temp = truth_value(formula, interpretation)
        if(temp != False): 
            return interpretation 
        else: 
            return False 
    
    atom = list_atoms[pointer]  

    interpretation1 = interpretation.copy()
    interpretation1[atom] = True
    r = sat(formula, list_atoms, interpretation1, pointer+1)
    if(r!=False): 
        return r

    interpretation2 = interpretation.copy() 
    interpretation2[atom] = False
    r = sat(formula, list_atoms, interpretation2, pointer+1)
    if(r!=False): 
        return r
    
    return False
