print( '---------------------------EXERCICE Moyenne-------------------------------------------')


Murielle = {'SDA':[15,16,18], 'Java':[16,15,18], 'Statistique':[16,14,18], 'Reseau': [14,15,16], 'UML':[13,16,17], 'Sys_Information':[16,15,18]}

s1 = (Murielle['SDA'][0] + Murielle['SDA'][1] + Murielle['SDA'][2])/3
s2 = (Murielle['Java'][0] + Murielle['Java'][1] + Murielle['Java'][2])/3
s3 = (Murielle['Statistique'][0] + Murielle['Statistique'][1] + Murielle['Statistique'][2])/3
s4 = (Murielle['Sys_Information'][0] + Murielle['Sys_Information'][1] + Murielle['Sys_Information'][2])/3
s5=  (Murielle['Reseau'][0] + Murielle['Reseau'][1] + Murielle['Reseau'][2])/3
s6=  (Murielle['UML'][0] + Murielle['UML'][1] + Murielle['UML'][2])/3


print ((s1+s2+s3+s4+s5+s6)/6)


print( '---------------------------EXERCICE E0-------------------------------------------')

l =list(range(1,11))
print (l)

print('----------------------------------------------------------')

l[0] = l[0]+11
l[1] = l[1]+11
l[2] = l[2]+11
l[3] = l[3]+11
l[4] = l[4]+11
l[5] = l[5]+11
l[6] = l[6]+11
l[7] = l[7]+11
l[8] = l[8]+11
l[9] = l[9]+11

print(list(l))


print('----------------------------------------------------------')

l.append(22)
print(list(l))
print('----------------------------------------------------------')


l.extend([23,24])
print(list(l))
print('----------------------------------------------------------')
print("la sous-liste de nombres impairs")
print(l[1:13 :2])
print("la sous-liste de nombres pairs")
print(l[0:13 :2])
print('----------------------------------------------------------')

l.remove(15)
print(l)




print(-------------EXERCICE E1----------------)


d={'nom': 'Dupuis','prenom':'Jacque','age':30}

d['prenom']= ['Jacques']
print(d)
print("------------------")

print(d.keys())
print("------------------")

print(d.values())
print("------------------")

desp={'esp':' ', 'anne': 'ans.'}

print (d['prenom']+ desp['esp'] +d['nom']+ desp['esp'] + d[age] + desp['esp'] + desp['anne'])
