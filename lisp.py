
#--------------   types          ------------
class LispObj:
    @property
    def type(self):
        return self.__class__.__name__
    
#------------ ConsList -----------
class ConsList(LispObj):
    def __init__(self, car, cdr):
        self.car = car
        self.cdr = cdr
    
    
    
def cons(car, cdr):
    return ConsList(car, cdr)
def car(pair):
    return pair.car
def cdr(pair):
    return pair.cdr
def EmptyList():
    return ConsList(None, None)
 
def isEmptyList(L):
    return L.car == None and L.cdr == None

m_EmptyList = EmptyList()
#-------- Symbol -----
class Symbol(LispObj):
    def __init__(self, s):
        self.value = s
    
#-------- binOp -----
class binOp(LispObj):
    def __init__(self, s):
        self.value = s
    
#--------- Functions ---------
def getType(o):
    """There could be only return o.__class__.__name__"""
    if isinstance(o, LispObj):
        return o.type
    return o.__class__.__name__
  
def getValue(o):
    if isinstance(o, LispObj):
        return o.value
    return o
  
def showConsList(L):
    if isEmptyList(L):
        return ""
    if isEmptyList(cdr(L)):
        return ' ' + show(car(L))
    return ' ' + show(car(L)) + showConsList(cdr(L)) 
  
def show(o):
    if getType(o) == "ConsList":
        return '(' + showConsList(o)[1:] + ')'
    elif getType(o) == "Symbol":
        return o.value
    elif getType(o) == "binOp":
        return o.value
    elif getType(o) == "str":
        return '\"' + o + '"'
    else:
        return str(o)

def evalBinOp(op, L):
    if isEmptyList(L):
        return None
    r = evalExpr(car(L))
    tail = cdr(L)
    while not isEmptyList(tail):
        r = realBinOp(op, r, evalExpr(car(tail)))
        tail = cdr(tail)
    return r

def realBinOp(op, x, y):
    o = getValue(op)
    if o == "+":
        return x + y
    elif o == "-":
        return x - y
    elif o == "*":
        return x * y
    elif o == "/":
        return x / y
    elif o == "%":
        return x % y
    else:
        return None
  
  
def evalExpr(o):
    t = getType(o)
    if t == "ConsList":
        if isEmptyList(o):
            return o
        else:
            hf = evalExpr(car(o))
            t_hf = getType(hf)
            tail = cdr(o)
            if t_hf == "binOp":
                return evalBinOp(hf, tail)
            else:
                return "not binOp"
    else:
        return o
#------------- Testing --------------
#def addToResult(val)
def testEval(expr):
    print(show(expr))
    print(evalExpr(expr))
  
def main():
    
    add = binOp('+')
    sub = binOp('-')
    mul = binOp('*')
    div = binOp('/')
  
    c1 = cons(add, cons(1, cons(2, m_EmptyList)))
    print(show(c1))
    print(evalExpr(c1))
    c2 = cons(add, (cons(1, cons(3, cons(2, m_EmptyList)))))
    testEval(c2)
    c3 = cons(mul, cons(5, cons(6, m_EmptyList)))
    testEval(c3)
    c4 = cons(mul, cons(10, cons(c2, m_EmptyList)))
    testEval(c4)
 
if __name__ == "__main__":
    main()
