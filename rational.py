class Q(object):
   def __init__(self, a, b):
       self.a = a
       self.b = b
   def __repr__(self):
       if self.b == 1:
           return str(self.a)
       return f'{self.a}/{self.b}'
   def __add__(self, q):
        a = self.a
        b = self.b
        c = q.a
        d = q.b
        return Q(..., ...)

q1 = Q(1,2)
q2 = Q(1,3)
print (q1.add(q2))