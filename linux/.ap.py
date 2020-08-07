import subprocess
import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 150)

print("linux-automation 0.0.1")

while True :
    cmd = input("_>")

# terminal commands
    if cmd == "cls" :
        engine.say("Clearing Terminal")
        engine.runAndWait()
        subprocess.call("clear")
    if cmd == "reset" :
        engine.say("Re-setting Terminal")
        engine.runAndWait()
        subprocess.call("reset")

    if cmd == "lock" :
        engine.say("Your System is locked.")
        engine.runAndWait()
        while True :
            usrname = input("Username: ")
            if usrname == "admin" :
                password = input("Password: ")
                if password == "qw" :
                    break
                else :
                    engine.say("incorrect password or username try again")
                    engine.runAndWait()

    if cmd == "shutdown" :
        engine.say("Are you sure, y for yes. n for no.")
        engine.runAndWait()
        bool1 = input("Are you sure[y, n]: ")
        if bool1 == "y" :
            engine.say("Shutting down after one minute.")
            engine.runAndWait()
            subprocess.call("shutdown")
        elif bool1 == "n" :
            engine.say("process terminated")
            engine.runAndWait()
        else :
            engine.say("Enter a valid answer.")
            engine.runAndWait()

    if cmd == "restart" :
        engine.say("Are you sure about that, y for yes. n for no.")
        engine.runAndWait()
        bool3 = input("Are You Sure?[y, n]: ")
        if bool3 == "y" :
            engine.say("Restarting the system.")
            engine.runAndWait()
            subprocess.call("restart", shell = True)
        elif bool3 == "n" :
            engine.say("Process terminates")
            engine.runAndWait()
        else :
            engine.say("Enter a valid answere.")
            engine.runAndWait()

    if cmd == "exit":
        engine.say("Exiting the voice script")
        engine.runAndWait()
        break

    if cmd == "hi dumbbot" :
        engine.say("Starting Dumb bot.")
        engine.runAndWait()
        subprocess.call("python3 .dumbbot.py", shell = True)

    if cmd == "help" :
        engine.say("Starting Help bot.")
        engine.runAndWait()
        subprocess.call("python3 .helpbot.py", shell = True)

# basic commands
    if cmd == "dir" :
        engine.say("The directories in the present location are shown below.")
        engine.runAndWait()
        subprocess.call("./sh/dir.sh", shell = True)

    if cmd == "creds" :
        subprocess.call("cat txt/cred.txt", shell = True)

    if cmd == "list" :
        engine.say("The available commands are shown below")
        engine.say("Enter them as shown below.")
        engine.runAndWait()
        subprocess.call("cat txt/list.txt", shell = True)

    if cmd == "cd" :
        engine.say("Enter the path to the desired location below")
        engine.runAndWait()
        path = input(":")
        subprocess.call("cd " + path, shell = True)

    if cmd == "calc" :
        engine.say("Enter the first number")
        engine.runAndWait()
        no_1 = input(":")
        engine.say("Enter the operator")
        engine.runAndWait()
        o = input(":")
        engine.say("Enter the second number")
        engine.runAndWait()
        no_2 = input(":")

        if o == "+" :
            sum = int(no_1) + int(no_2)
            engine.say("The sum would be " + sum)
            engine.runAndWait()
            print(sum)

        if o == "-" :
            diff = int(no_1) - int(no_2)
            engine.say("the difference would be " + diff)
            engine.runAndWait()
            print(diff)

        if o == "*" :
            pro = int(no_1) * int(no_2)
            engine.say("The product would be " + pro)
            engine.runAndWait()
            print(pro)

        if o == "/" :
            quo = int(no_1) / int(no_2)
            rem = int(no_1) % int(no_2)

            engine.say("the quotient is " + quo)
            engine.say("The remainder will be " + rem)
            engine.runAndWait()

            print("qoutient - " + quo)
            print("remainder - " + rem)


# File Commands
    if cmd == "make -f" :
        engine.say("Creating a file")
        engine.runAndWait()
        subprocess.call("./sh/make-f.sh", shell = True)
        engine.say("File created")
        engine.runAndWait()

    if cmd == "make -b" :
        engine.say("Creating a bootable pendrive. no voice instructions for this one.")
        engine.runAndWait()
        subprocess.call("./sh/make-b.sh", shell = True)

    if cmd == "make -rs" :
        engine.say("Creating a run able script.")
        engine.runAndWait()
        subprocess.call("./sh/make-rs", shell = True)

    if cmd == "del" :
        engine.say("Path of the file to be deleted")
        path2 = input(":")
        subprocess.call("rm -r " + path2, shell = True)

        

# Script Running commands

# System commands
    if cmd == "update -a" :
        engine.say("Updating and upgrading your system.")
        engine.runAndWait()
        subprocess.call("sudo apt-get update && sudo apt upgrade", shell = True)

    if cmd == "install" :
        engine.say("Enter the name of the application to be installed below")
        engine.runAndWait()
        name = input(":")
        subprocess.call("sudo apt-get install " + name, shell = True)

    if cmd == "install -ppa" :
        engine.say("Enter the link of the ppa below")
        engine.runAndWait()
        ppa = input(":")
        subprocess.call("sudo add-apt-repository ppa:" + ppa, shell = True)
        subprocess.call("sudo apt-get update", shell = True)
        engine.say("Enter the application name below")
        engine.runAndWait()
        name1 = input(":")
        subprocess.call("apt-get install " + name1)

    if cmd == "install -de" :
        engine.say("Kindly enter password where-ever needed.")
        engine.say("Enter the name of the desktop enviroment to be installed below")
        engine.runAndWait()

        de = input(":")
        if de == "Budgie" or de == "budgie" :
            subprocess.call("sudo add-apt-repository ppa:budgie-remix/ppa", shell = True)
            subprocess.call("sudo apt update", shell = True)
            subprocess.call("sudo apt install ubuntu-budgie-desktop")
            engine.say("Thanks for the wait, process completed.")
            engine.runAndWait()
        
        elif de == "Pantheon" or de == "pantheon" :
            subprocess.call("sudo add-apt-repository ppa:elementary-os/stable", shell = True)
            subprocess.call("sudo apt update", shell = True)
            subprocess.call("sudo apt install elementary-desktop", shell = True)
            engine.say("Thanks for the wait, process completed.")
            engine.runAndWait()

        elif de == "Kde" or de == "KDE" or de == "kde" :
            engine.say("Please choose the version you want.")
            engine.say("full.")
            engine.say("standard.")
            engine.say("desktop.")
            engine.say("netbook, enter the chosen version below")
            engine.runAndWait()
            version = input(":")
            while True :
                if version == "full" or version == "Full" :
                    subprocess.call("sudo apt-get install kde-full", shell = True)
                    engine.say("Thanks for the wait, process completed.")
                    engine.runAndWait()
                    break
                
                elif version == "standard" or version == "Standard" :
                    subprocess.call("sudo apt-get install kde-standard", shell = True)
                    engine.say("Thanks for the wait, process completed.")
                    engine.runAndWait()
                    break

                elif version == "desktop" or version == "Desktop" :
                    subprocess.call("sudo apt-get install kde-plasma-desktop", shell = True)
                    engine.say("Thanks for the wait, process completed.")
                    engine.runAndWait()
                    break

                elif version == "netbook" or version == "Netbook" :
                    subprocess.call("sudo apt-get install kde-plasma-netbook", shell = True)
                    engine.say("Thanks for the wait, process completed.")
                    engine.runAndWait()
                    break
                
                else :
                    engine.say("Error. Please check if the version you entered is the right one.")
                    engine.runAndWait()
                                    
        elif de == "xfce" or de == "XFCE" or de == "Xfce" :
            subprocess.call("sudo apt-get install xfce4", shell = True)
            engine.say("Thanks for the wait, process completed.")
            engine.runAndWait()

        elif de == "gnome" or de == "Gnome" :
            subprocess.call("sudo add-apt-repository ppa:gnome3-team/gnome3", shell = True)
            subprocess.call("sudo add-apt-repository ppa:gnome3-team/gnome3-staging", shell = True)
            subprocess.call("sudo apt-get update", shell = True)
            subprocess.call("sudo apt-get install gnome-shell", shell = True)
            engine.say("Thanks for the wait, process completed.")
            engine.runAndWait()

        elif de == "mate" or de == "Mate" :
            subprocess.call("sudo apt update && sudo apt upgrade", shell = True)
            subprocess.call("sudo apt install ubuntu-mate-desktop", shell = True)
            engine.say("Thanks for the wait, process completed.")
            engine.runAndWait()

        elif de == "Cinnamon" or de == "cinnamon" :
            subprocess.call("sudo add-apt-repository ppa:embrosyn/cinnamon", shell = True)
            subprocess.call("sudo apt update", shell = True)
            subprocess.call("sudo apt install cinnamon", shell = True)
            engine.say("Thanks for the wait, process completed.")
            engine.runAndWait()

        elif de == "LXDE" or de == "Lxde" or de == "lxde" :
            subprocess.call("sudo apt-get install lxde", shell = True)
            engine.say("Thanks for the wait, process completed.")
            engine.runAndWait()
        elif de == "Openbox" or de == "openbox" :
            subprocess.call("sudo apt-get install openbox obconf", shell = True)
            engine.say("Thanks for the wait, process completed.")
            engine.runAndWait()

        elif de == "i3" or de == "I3" :
            subprocess.call("sudo apt-get install i3", shell = True)
            engine.say("Thanks for the wait, process completed.")
            engine.runAndWait()

        engine.say("Restart system to apply changes?")
        engine.say("Y for yes")
        engine.say("N for no")
        engine.runAndWait()
        bool2 = input(": ")
        if bool2 == "y" :
            engine.say("Restarting the system.")
            engine.runAndWait()
            subprocess.call("restart")
        elif bool2 == "n" :
            print("_______________________________________________")

    if cmd == "install -pm" :
        engine.say("Enter the module name")
        engine.runAndWait()
        module = input(">")
        subprocess.call("sudo apt-get install python-pip", shell = True)
        subprocess.call("sudo pip install " + module, shell = True)

    if cmd == "install -pm3" :
        engine.say("Enter the module name")
        engine.runAndWait()
        module1 = input(">")
        subprocess.call("sudo apt-get install python3-pip", shell = True)
        subprocess.call("sudo pip3 install " + module1, shell = True)

    if cmd == "info" :
        engine.say("Information about the system.")
        engine.runAndWait()
        subprocess.call("uname -a", shell = True)

    if cmd == "info -f" :
        engine.say("Path to file")
        engine.runAndWait()
        path1 = input(">")
        subprocess.call("touch info.txt " + path1, shell = True)

    if cmd == "info -a" :
        engine.say("Please enter info -av for voice.")
        engine.runAndWait()
        print("\n")
        subprocess.call("ifconfig", shell = True)
        print("\n ip address: ")
        subprocess.call("ip", shell = True)
        print("\n Disks available: ")
        subprocess.call("lsblk", shell = True)
        print("\n PCI card information: ")
        subprocess.call("lspci", shell = True)

    if cmd == "info -v" :
        subprocess.call("uname -a < txt/Info/info.txt", shell = True)
        filePath = "txt/Info/info.txt"
        f = open(filePath, "r")
        Text = f.read()
        f.close()
        engine.say(str(Text))
        engine.runAndWait()
        #BUG

#Disk Commands
    if cmd == "disk" :
        print("________________________________________________________________")
        subprocess.call("lsblk", shell = True)
        print("________________________________________________________________")


    if cmd == "disk -u" :
        subprocess.call("du", shell = True)

# Superuser commands
    if cmd == "fro":
        pas = "root"
        pas1 = input("Password for fro: ")
        if pas1 == pas:
            while True :
                cmd1 = input("$>")
                if cmd1 == "exit" :
                    break
                #basic fro commands
                if cmd1 == "cls" :
                    subprocess.call("clear", shell = True)
                if cmd1 == "reset" :
                    subprocess.call("reset", shell = True)
                if cmd1 == "hide" :
                    pass
                if cmd1 == "list" :
                    pass
