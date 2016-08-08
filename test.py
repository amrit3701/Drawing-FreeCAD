stories=8                       #Number of stories

dep_of_foun=6.0                 #Depth of Foundation

plinth_lev=4.0                  #Plinth level of building

clear_height=[10,10,10,10,6,8,8,8,8]          #Clear Height of each story

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

import pdb
def z_sum(i):
        zsum = 0
        index = 0
        while index < i:
                # zsum = zsum + clear_height[index] + dep_slab - dep_beam/2.0 + ((dep_beam/2.0) * index)
                # zsum = zsum + clear_height[index]
                zsum = zsum + clear_height[index] + dep_beam
                #pdb.set_trace()
                if(index == 0):
                    zsum = zsum - dep_beam/2.0
                index = index + 1
        return zsum


def cen(i):
    z = z_sum(i)
    if (i == 1):
        cen_story = z/2
        #xx = zzsum - zzsum2
    else:
        cen_story = z - dep_beam/2 - clear_height[i-1]/2
        return cen_story



print z_sum(4) #-z_sum(1)#- clear_height[4]/2
print cen(4)
