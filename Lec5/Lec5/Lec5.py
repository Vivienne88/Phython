filename = "GURADA.txt"
filename2 = "GURADA2.txt"
import pickle

roles = []
rolenum = 0
with open(filename,"r") as fp, open(filename2,"wb+") as pk :
    for i in fp :
        (role, message) = i.strip().split(":",1)
        roles.append(role)
    pickle.dump(roles,pk)

with open(filename2,"rb") as fp :
    result = pickle.load(fp)
    print(result)

           

