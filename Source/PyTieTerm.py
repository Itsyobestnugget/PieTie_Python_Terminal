import os

while True:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    cmd = input("C:/user/PyTie.exe : ")
    if cmd == "help":
        print("PyTie is CASE SENSITIVE!!!!!!!! \n \n help - Displays all commands \n")
    
    elif cmd == "dir":
        print("Displaying directorys...\n \n")
        directory = dir_path
        directorys = os.path.dirname
        for root, dirs, files in os.walk(directory):
            for subFile in files:
                print (os.path.join(root, subFile, directorys))

    elif cmd == "cd ..":
        print("error going back")

    elif cmd == "mkfile":
        print("This feature is currently in development, please wait for it to be released")
#        print("Welcome to MKFile (make file) function which makes a text file. \n \n lets make a new file. first select a name")
#        Filename = "/workspaces/PieTie_Python_Terminal/Source/text.txt".join((input("Enter a name: ")))
#        Content = input("now lets insert some data. type it here: ")
#        filemake = open(Filename, "x")
#        filething = open(Filename)
#        filemake.write(Content)
#        f = open(Filename, "r")
#        print(f.read())

        # Method 1
#f = open("Path/To/Your/File.txt", "w")   # 'r' for reading and 'w' for writing
#f.write("Hello World from " + f.name)    # Write inside file 
#f.close()                                # Close file 

# Method 2
#with open("Path/To/Your/File.txt", "w") as f:   # Opens file and casts as f 
#    f.write("Hello World form " + f.name)       # Writing
    # File closed automatically


    elif cmd == "readfile":
        
        fileopen = open(input("File.. with dir eg /workspaces/PieTie_Python_Terminal/Source/File.txt   : "), "r")
        print(fileopen.read())

    elif cmd == "placeholdercommand":
        print("Placeholder")

    elif cmd == "placeholdercommand":
        print("Placeholder")

    elif cmd == "placeholdercommand":
        print("Placeholder")

    elif cmd == "placeholdercommand":
        print("Placeholder")

    elif cmd == "placeholdercommand":
        print("Placeholder")

    elif cmd == "placeholdercommand":
        print("Placeholder")

    elif cmd == "placeholdercommand":
        print("Placeholder")

    elif cmd == "placeholdercommand":
        print("Placeholder")

    elif cmd == "placeholdercommand":
        print("Placeholder")

    elif cmd == "placeholdercommand":
        print("Placeholder")

    elif cmd == "placeholdercommand":
        print("Placeholder")

    elif cmd == "placeholdercommand":
        print("Placeholder")

    elif cmd == "placeholdercommand":
        print("Placeholder")

    elif cmd == "placeholdercommand":
        print("Placeholder")

    elif cmd == "placeholdercommand":
        print("Placeholder")


