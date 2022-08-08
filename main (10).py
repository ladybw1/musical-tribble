import os
def main():
    directory = input("Enter the directory that you want to save the file :")
    filename = input("Enter the filename : ")
    name = input("Enter your name : ")
    address = input("Enter your address : ")
    phone_number = input("Enter your phone number : ")
    #checking if the directory exists
    if os.path.isdir(directory): 
        #creating and opening the file to write 
        writeFile = open(os.path.join(directory,filename), 'w')
        #writing the data by comma separated
        writeFile.write(name+','+address+','+phone_number+'\n')
        #close the file after wiriting is done
        writeFile.close()
        print("File contents:")
        readFile = open(os.path.join(directory,filename), 'r')
        for line in readFile: 
            print(line)
        readFile.close()
    else:
        print("Directory exists...")
main()
