#myfile = open("fruits.txt")
#content = myfile.read()
#myfile.close()

#print(content)
#print(content)

import time
import os
import pandas

while True:
    if os.path.exists("temps_today.csv"):
        data = pandas.read_csv("temps_today.csv")
        print(data.mean()["st2"])
    else: 
        print("File doesn't exist!")

    time.sleep(5)


with open("vegetables.txt", "a+") as writingfile:
    writingfile.write("\nokra")
    writingfile.seek(0)

    vegetables = writingfile.read()
print(vegetables)


