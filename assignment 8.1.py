import os

msg = "Lets's work with files \n"
print(msg)

def main():
    directory = input("Enter the directory that you want to save the file : ")
    filename = input("Enter the filename : ")
    name = input("Enter your name : ")
    address = input("Enter your address : ")
    phone_number = input("Enter your phone number : ")


    if os.path.isdir(directory):
        writeFile = open(os.path.join(directory,filename),'w')
        writeFile.write(name+', '+address+', '+phone_number+'\n')
        writeFile.close()
        print(f"The {filename} file now contains the following information:")
        readFile = open(os.path.join(directory,filename),'r')

        for line in readFile:
            print(line)
        readFile.close()
    else:
            print(f"Sorry the directory {directory} does not exists...")

main()
input('Press ENTER to exit')
