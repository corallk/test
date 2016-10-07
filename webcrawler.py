#!/usr/bin/env python

infile=open('place2.txt','r')
outfile=open('place3.txt','w')
c=0

for line in infile:
    item=line.split()
    n=item[0].split('_')
    if len(n)==1:
        prov=item[1:]
        num_prov=len(item[1:])
    if len(n)==2:
        city=item[1:]
        num_city=len(item[1:])
    if len(n)==3:
        town=item[1:]
        num_town=len(item[1:])
        for i in range(num_town):          
            outfile.write(prov[int(n[1])]+' '+city[int(n[2])]+' '+town[i]+'\n')


infile.close()
outfile.close()


