####### Serializing#######
'''import pickle
l = [2,3,4,5,6]
file = open("exam.txt","wb")
pickle.dump(l,file)
file.close()
print("Data convert into bytestream")'''

######deSerializing#########
import pickle
file = open("exam.txt","rb")
l = pickle.load(file)
print(l)