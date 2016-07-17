import mysql.connector

cnx=mysql.connector.connect(user='root',password='a', database='Sim')

cursor=cnx.cursor()

query = ("select idd,x,y,z from Joint;")

cursor.execute(query)

a=[]

for i in cursor:
    a.append(i)

joints = dict()
for i in range(len(a)):
   val=a[i][0]
   temp=[]
   for j in range(1,4):
       temp.append(a[i][j])
   joints[a[i][0]] = temp

App.newDocument("Unnamed")
App.setActiveDocument("Unnamed")

for i in joints.keys():
    Draft.makePoint(joints[i][0], joints[i][1], joints[i][2])


cursor2=cnx.cursor()
query2 = ("select member_id, joint_id from Member_incidence;")
cursor2.execute(query2)

b=[]

for i in cursor2:
    b.append(i)

# Initialise a dictionary
mem_incidence = dict()
# Iterate from 0 to len of a
for i in range(0,len(b)):
    temp=[]
    # Storing the value of the key for dictionary
    val=b[i][0];
    for j in range(0,len(b)):
        # Check if val is equal to another key i.e "a[j][0]"
        if val == b[j][0]:
            # Append the value of the key in temp
            temp.append(b[j][1]);
    # Append key (val) and value (temp in dictionary)
    mem_incidence[val]=temp

for i in mem_incidence.keys():
    w=mem_incidence[i][0]
    w1=mem_incidence[i][1]
    start_pt=FreeCAD.Vector(joints[w][0],joints[w][1],joints[w][2])
    end_pt=FreeCAD.Vector(joints[w1][0],joints[w1][1],joints[w1][2])
    Points=[start_pt,end_pt]
    Draft.makeWire(Points,closed=False,face=True,support=None)


from math import sqrt,pow
from FreeCAD import Base

def make_box(name, length, width, height, base_vector, base_rotation):
        ac_doc = FreeCAD.ActiveDocument
        ac_doc.addObject("Part::Box",name)
        getattr(ac_doc, name).Length = length
        getattr(ac_doc, name).Width = width
        getattr(ac_doc, name).Height = height
        getattr(ac_doc, name).Placement=Base.Placement(Base.Vector(base_vector[0],base_vector[1],base_vector[2]),Base.Rotation(base_rotation[0],base_rotation[1],        base_rotation[2],base_rotation[3]))

dim1=.5
dim2=.5

for i in mem_incidence.keys():
    w1=mem_incidence[i][0]
    w2=mem_incidence[i][1]

    dis = sqrt(pow((joints[w2][0]-joints[w1][0]),2)+pow((joints[w2][1]-joints[w1][1]),2)+pow((joints[w2][2]-joints[w1][2]),2))

    if (joints[w2][0]-joints[w1][0]) != 0:
        nam = "beam_xaxis"+str(i)
        if joints[w2][0] > joints[w1][0]:
            make_box(nam, dis, dim1, dim2, [joints[w1][0]+.25,joints[w1][1],joints[w1][2]], [0, 0, 0, 1])
        else:
            make_box(nam, dis, dim1, dim2, [joints[w2][0]+.25,joints[w2][1],joints[w2][2]], [0, 0, 0, 1])

    if (joints[w2][1]-joints[w1][1]) != 0:
        nam = "column_yaxis"+str(i)
        if joints[w2][1] > joints[w1][1]:
            make_box(nam, dim1, dis, dim2, [joints[w1][0],joints[w1][1]+.25,joints[w1][2]], [0, 0, 0, 1])
        else:
            make_box(nam, dim1, dis, dim2, [joints[w2][0],joints[w2][1]+.25,joints[w2][2]], [0, 0, 0, 1])

    if (joints[w2][2]-joints[w1][2]) != 0:
        nam = "beam_zaxis"+str(i)
        if joints[w2][2] > joints[w1][2]:
            make_box(nam, dim1, dim2, dis, [joints[w1][0],joints[w1][1],joints[w1][2]+.25], [0, 0, 0, 1])
        else:
            make_box(nam, dim1, dim2, dis, [joints[w2][0],joints[w2][1],joints[w2][2]+.25], [0, 0, 0, 1])

