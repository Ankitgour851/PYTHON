import pickle

#Pickling a Python obj

# cars=["Audi","BMW","Maruti Suzuki","Harry Tuzuki"]
# file="Mycar.pkl"
# fileobj=open(file,"wb")
# pickle.dump(cars,fileobj)
# fileobj.close()


file="mycar.pkl"
fileobj=open(file,"rb")
mycar=pickle.load(fileobj)
print(mycar)
print(type(mycar))