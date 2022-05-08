class perro():

  def __init__(self, nombre, size, raza):
      self.nombre=nombre
      self.size=size
      self.raza=raza

  def ladra(self):
     s=""
     for l in self.nombre:
      s+="wof"
     print (s)


chucho=perro("chucho","grande","husky")
chucho.ladra() 

#wofwofwofwofwofwof

cloe=perro("cloe","mini","chihuahua")
cloe.ladra()
