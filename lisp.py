def cons(v, l):
	return (v,l)
def car(pair):
	return pair[0]
def cdr(pair):
	return pair[1]
	

def is_null(s):
	return car(s) is None and cdr(s) is None
	
null = cons(None, None)
s1 = cons(1, null)
s2 = cons(2, s1)
