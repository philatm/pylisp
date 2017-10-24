### Урок 1:
Будем создавать реализацию списка. Список у нас это, то что имеет голову и хвост. 
Поэтому напишем конструкторы и селекторы:
```python
def cons(v, l):
	return (v,l)
def car(pair):
	return pair[0]
def cdr(pair):
	return pair[1]
```

Теперь мы можем пользовться ими:
```python
null = [None, None]
s1 = cons(1, null)
s2 = cons(2, s1)
```
при чем:
```python
car(s2)
=> 2
car(s1)
=> 1
```
Сейчас определим, что пустой список, это такой у которого голова и хвост равны None. 
Напишем предикат is_null(s), который принимает список s и возвращает true,если он пустой и false иначе:
```python
def is_null(s):
    return car(s) is None and cdr(s) is None
```
