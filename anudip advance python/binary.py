import pickle
f=open("anudip.dat",'ab')
li=[10,20,60,80,90]
pickle.dump(li,f)
f.close()
