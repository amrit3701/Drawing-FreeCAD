import csv, sys

#sys.path.insert(0, '..')

#from views import lis

#print lis



f = open('../some.csv')
sp = csv.reader(f, delimiter=' ')

for i in sp:
    data = i


stories=int(data[0])                       #Number of stories

dep_of_foun=float(data[1])                 #Depth of Foundation

plinth_lev=float(data[2])                  #Plinth level of building

cclear_height=data[3]            #Clear Height of each story

dep_slab=float(data[4])                    #Depth of Slab

#rep_span_len="2@8+9+1@10+2@12"  #Representation of span length
rep_span_len=data[5]

#rep_span_wid="2@7+6+1@5"       #Representation of span width
rep_span_wid=data[6]

col_type=int(data[7])                      #Column type 0 for cylindrical and 1 for rectangular

len_col=float(data[8])                       #Length of Column (for column type 1)

wid_col=float(data[9])                       #Width of Column (for column type 1)

radius_col=float(data[10])                   #Radius of column (for column type 0)

dep_beam=float(data[11])                      #Depth of Beam

wid_beam=float(data[12])                      #Width of Beam


print("stories %s" %stories)
print("wid_beam %s" %wid_beam)
"""
stories=8                       #Number of stories

dep_of_foun=6.0                 #Depth of Foundation

plinth_lev=4.0                  #Plinth level of building

cclear_height="3@10+30+6+3@8"            #Clear Height of each story

dep_slab=1                    #Depth of Slab

#rep_span_len="2@8+9+1@10+2@12"  #Representation of span length
rep_span_len="4@8"

#rep_span_wid="2@7+6+1@5"       #Representation of span width
rep_span_wid="4@8"

col_type=1                      #Column type 0 for cylindrical and 1 for rectangular

len_col=1                       #Length of Column (for column type 1)

wid_col=1                       #Width of Column (for column type 1)

radius_col=.5                   #Radius of column (for column type 0)

dep_beam=2                      #Depth of Beam

wid_beam=1                      #Width of Beam
"""
