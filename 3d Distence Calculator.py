import numpy as np

xyz1 = input("Enter xyz From: ")
xyz2 = input("Enter xyz To: ")
'''
Takes X Y Z 
with space 
'''
xy1 = xyz1.split()
xy2 = xyz2.split()

ns1 = ""
ns2 = ""
for ele1,ele2 in zip(xy1, xy2):
    ns1 += ele1
    ns2 += ele2

for a in xy1:
    x1 = xy1[0]
    y1 = xy1[1]
    z1 = xy1[2]

for b in xy2:
    x2 = xy2[0]
    y2 = xy2[1]
    z2 = xy2[2]

p1 = np.array([x1,y1,z1], dtype=float)
p2 = np.array([x2,y2,z2], dtype=float)

squared_dist = np.sum((p1-p2)**2, axis=0)
dist = np.sqrt(squared_dist)

print(f"From {x1,y1,z1} To {x2,y2,z2} is {round(dist)} blocks away")


