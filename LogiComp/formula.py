"""This module is designed to define formulas in propositional logic.
For example, the following piece of code creates an object representing (p v s).

formula1 = Or(Atom('p'), Atom('s'))


As another example, the piece of code below creates an object that represents (p → (p v s)).

formula2 = Implies(Atom('p'), Or(Atom('p'), Atom('s')))
"""

simbolo = {
    'not': u"\u00ac",
    'and': u"\u2227",
    'or': u"\u2228",
    'implies': u"\u2192" 
}

class Formula:
    def __init__(self):
        pass


class Atom(Formula):
    """
    This class represents propositional logic variables.
    """

    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return str(self.name)

    def __eq__(self, other):
        return isinstance(other, Atom) and other.name == self.name

    def __hash__(self):
        return hash((self.name, 'atom'))


class Implies(Formula):

    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right

    def __str__(self):
        return "(" + self.left.__str__() + " " + u"\u2192" + " " + self.right.__str__() + ")"

    def __eq__(self, other):
        return isinstance(other, Implies) and other.left == self.left and other.right == self.right

    def __hash__(self):
        return hash((hash(self.left), hash(self.right), 'implies'))


class Not(Formula):

    def __init__(self, inner):
        super().__init__()
        self.inner = inner

    def __str__(self):
        if( isinstance(self.inner, Atom) ):
            return simbolo["not"] + self.inner.__str__()
        else:
            return  simbolo["not"] +"(" + self.inner.__str__() + ")"
    
    def __eq__(self, other):
        return isinstance(other, Not) and other.inner == self.inner

    def __hash__(self):
        return hash((hash(self.inner), 'not'))


class And(Formula):

    def __init__(self, left, right):
        super().__init__()
        self.left = left        
        self.right = right
        
        
    # def str_line(self, quebrar_linha=True):
    #     temp =  "\n" if(quebrar_linha==True) else ""
    #     return f'{temp}{self.left.str_line(True)} {simbolo["and"]} {self.right.str_line(True)} {temp}'
    def __str__(self):
        return f'({self.left.__str__() } {simbolo["and"]} {self.right.__str__()})'

    def __str__(self):

        l = self.left.__str__()
        if((isinstance(self.left, Or)) or (isinstance(self.left, Implies) )  ):
        # # if((not isinstance(self.left, And)) and (not isinstance(self.left, Atom) ) and (not isinstance(self.left, Not) ) ):
            l = f'({l})'
        r = self.right.__str__()
        if((isinstance(self.right, Or)) or (isinstance(self.right, Implies) )  ):
        # # if((not isinstance(self.right, And)) and (not isinstance(self.right, Atom) ) and (not isinstance(self.right, Not) ) ):
            r = f'({r})' 
        return f'{l} {simbolo["and"]} {r}'


    def __eq__(self, other):
        return isinstance(other, And) and other.left == self.left and other.right == self.right

    def __hash__(self):
        return hash((hash(self.left), hash(self.right), 'and'))


class Or(Formula):

    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right 
        
    # def __str__(self): 
    #     return f'({self.left.__str__() } {simbolo["or"]} {self.right.__str__() })'

    def __str__(self):
        l = self.left.__str__()
        if((isinstance(self.left, And)) or (isinstance(self.left, Implies) )  ):
        # if((not isinstance(self.left, Or)) and (not isinstance(self.left, Atom) ) and (not isinstance(self.left, Not) ) ):
            l = f'({l})'
        r = self.right.__str__()
        if((isinstance(self.right, And)) or (isinstance(self.right, Implies) )  ):
        # if((not isinstance(self.right, Or)) and (not isinstance(self.right, Atom) ) and (not isinstance(self.right, Not) ) ):
            r = f'({r})'
        return f'{l} {simbolo["or"]} {r}' 

    def __eq__(self, other):
        return isinstance(other, Or) and other.left == self.left and other.right == self.right

    def __hash__(self):
        return hash((hash(self.left), hash(self.right), 'or'))


class Iff:
    """
    Describes the 'if and only if' logical connective (<->) from propositional logic.
    Unicode value for <-> is 2194.
    """
    pass


class Xor:
    """
    Describes the xor (exclusive or) logical connective from propositional logic.
    Unicode value for xor is 2295.
    """
    pass
