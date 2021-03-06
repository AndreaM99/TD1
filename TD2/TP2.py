from collections import namedtuple

Point1D = namedtuple("Point1D",["x"])
# namedtuple sert a donner des noms aux variables
print(Point1D)

p_04 = Point1D(0.4)
print(p_04)
p_05 = Point1D(0.5)

print(p_04+p_05)

# Ce qu'on voudrait :
# p_04 + p_05 == Point1D(0.9)
# Ce que l'on a :
# (0.4, 0.5)

def ajout_point1d(point1, point2):
  x = point1.x + point2.x
  
  return Point1D(x)

print(f"Addition ok:{ajout_point1d(p_04, p_05)}")

def norme1d(p1):
  return (p1.x**2) ** 0.5

p_09 = ajout_point1d(p_04, p_05)

print(norme1d(p_09))


#####

Point2D = namedtuple('Point2D', ['x','y'])

p2d = Point2D(x=0,y=1)
p2d[0]
print(p2d.x)
print(p2d.y)

p1 = Point2D(0, 1) 
p2 = Point2D(1, 0)
print(p1)
print(p2)
print("*************")

def ajout_point2d(p_1, p_2):
  x = p_1[0] + p_2[0]
  y = p_1[1] + p_2[1]
  return Point2D(x, y)

p3 = ajout_point2d(p1,p2)
print(p3)

print(f"Addition ok: {ajout_point2d(p1, p2) == Point2D(1,1)}")

def ajout2_point2d(p_1, p_2):
  coord = []
  for indice in range((len(p_1))):
    coord.append(p_1[indice]+p_2[indice])
  return Point2D(coord[0], coord[1])

print(f"Addition ok: {ajout2_point2d(p1, p2) == Point2D(1,1)}")

def ajout3_point2d(p_1, p_2):
  coord = tuple(x+y for x, y in zip(p_1,p_2))
  return Point2D._make(coord)

print(f"Addition ok: {ajout2_point2d(p1, p2) == Point2D(1,1)}")

#####
liste = []
liste.append("a")
print(liste)
liste.append("n")
print(liste)
#####

# La 3D
Point3D = namedtuple('Point3D', ['x','y',"z"])

def ajout_point3d(p_1, p_2):
  
  return Point3D._make((p1 + p2 for p1, p2 in zip(p_1, p_2)))

p3_1 = Point3D(0,0,1)
p3_2 = Point3D(0,0,1)

print(ajout_point3d(p3_1, p3_2))


# Les classes
class Point1D:
  def __init__(self, x):
    self.x = x

np1d = Point1D(0.9)
print(np1d) # Bizarre donc on creer une fonction

def afficher_point1d(point):
  print(f"Point: {point.x}")

print(afficher_point1d(np1d))

