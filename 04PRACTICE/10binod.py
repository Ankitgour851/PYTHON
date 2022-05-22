import os

def isBinod(filename):
    with open(filename,'r') as f:
        filecontent = f.read()

        #Detect all form of Binod like bInOd
        if "binod" in filecontent.lower():
            return True
        else:
            return False


if __name__ == "__main__":
    #Listing the content of this folder
    dir_contents = os.listdir()

    nBinod = 0
    #For each text file,detect Binod in them
    print(dir_contents)
    for item in dir_contents:
        if item.endswith('txt'):
            print(f"Detecting Binod in {item}")
            flag = isBinod(item)
            if(flag):
                print(f"***************Binod found in {item}!!!!!!!!!!")
                nBinod +=1
            else:
                print(f"Binod is not found in {item}")
    print("*********Binod detctor summmary**********")
    print(f"{nBinod} files found with binod hidden into them")