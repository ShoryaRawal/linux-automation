import subprocess
print("linux-automation 0.0.1")

while True :
    cmd = input("_>")

# terminal commands
    if cmd == "cls" :
        subprocess.call("clear")
    if cmd == "reset" :
        subprocess.call("reset")

    if cmd == "lock" :
        print("Your System is locked.")
        while True :
            usrname = input("Username: ")
            if usrname == "admin" :
                password = input("Password: ")
                if password == "qw" :
                    break
                else :
                    print("\n incorrect password or username try again: ")

    if cmd == "shutdown" :
        bool1 = input("Are you sure[y, n]: ")
        if bool1 == "y" :
            subprocess.call("shutdown")
        elif bool1 == "n" :
            print("process terminated")
        else :
            print("Enter a valid answere.")

    if cmd == "exit":
        break

# basic commands
    if cmd == "dir" :
        subprocess.call("./sh/dir.sh", shell = True)

    if cmd == "creds" :
        subprocess.call("cat txt/cred.txt", shell = True)

    if cmd == "list" :
        subprocess.call("cat txt/list.txt", shell = True)

    if cmd == "cd" :
        path = input("Path:")
        subprocess.call("cd " + path, shell = True)

    if cmd == "calc" :
        no_1 = input("1> ")
        o = input("o>")
        no_2 = input("2> ")

        if o == "+" :
            sum = int(no_1) + int(no_2)
            print(sum)

        if o == "-" :
            diff = int(no_1) - int(no_2)
            print(diff)

        if o == "*" :
            pro = int(no_1) * int(no_2)
            print(pro)

        if o == "/" :
            quo = int(no_1) / int(no_2)
            rem = int(no_1) % int(no_2)

            print("qoutient - " + quo)
            print("remainder - " + rem)


# File Makeing Commands
    if cmd == "make -f" :
        subprocess.call("./sh/make-f.sh", shell = True)

    if cmd == "make -b" :
        subprocess.call("./sh/make-b.sh", shell = True)

    if cmd == "make -rs" :
        subprocess.call("./sh/make-rs", shell = True)

        

# Script Running commands

# System commands
    if cmd == "update -a" :
        subprocess.call("sudo apt-get update && sudo apt upgrade", shell = True)

    if cmd == "install" :
        name = input("Application Name: ")
        subprocess.call("sudo apt-get install " + name, shell = True)

    if cmd == "install -ppa" :
        ppa = input("link of the ppa: ")
        subprocess.call("sudo add-apt-repository ppa:" + ppa, shell = True)
        subprocess.call("sudo apt-get update", shell = True)
        name1 = input("\nApplication name: ")
        subprocess.call("apt-get install " + name1)

    if cmd == "install -de" :
        print("(enter password where-ever needed.)")

        de = input("Desktop Enviroment To Be installed: ")
        if de == "Budgie" or de == "budgie" :
            subprocess.call("sudo add-apt-repository ppa:budgie-remix/ppa", shell = True)
            subprocess.call("sudo apt update", shell = True)
            subprocess.call("sudo apt install ubuntu-budgie-desktop")
            print("process completed.")
        
        elif de == "Pantheon" or de == "pantheon" :
            subprocess.call("sudo add-apt-repository ppa:elementary-os/stable", shell = True)
            subprocess.call("sudo apt update", shell = True)
            subprocess.call("sudo apt install elementary-desktop", shell = True)

        elif de == "Kde" or de == "KDE" or de == "kde" :
            version = input("Version(full, standard, desktop or netbook): ")
            while True :
                if version == "full" or version == "Full" :
                    subprocess.call("sudo apt-get install kde-full", shell = True)
                    break
                
                elif version == "standard" or version == "Standard" :
                    subprocess.call("sudo apt-get install kde-standard", shell = True)
                    break

                elif version == "desktop" or version == "Desktop" :
                    subprocess.call("sudo apt-get install kde-plasma-desktop", shell = True)
                    break

                elif version == "netbook" or version == "Netbook" :
                    subprocess.call("sudo apt-get install kde-plasma-netbook", shell = True)
                    break
                
                else :
                    print("Error, not a version.")
                                    
        elif de == "xfce" or de == "XFCE" or de == "Xfce" :
            subprocess.call("sudo apt-get install xfce4", shell = True)

        elif de == "gnome" or de == "Gnome" :
            subprocess.call("sudo add-apt-repository ppa:gnome3-team/gnome3", shell = True)
            subprocess.call("sudo add-apt-repository ppa:gnome3-team/gnome3-staging", shell = True)
            subprocess.call("sudo apt-get update", shell = True)
            subprocess.call("sudo apt-get install gnome-shell", shell = True)

        elif de == "mate" or de == "Mate" :
            subprocess.call("sudo apt update && sudo apt upgrade", shell = True)
            subprocess.call("sudo apt install ubuntu-mate-desktop", shell = True)

        elif de == "Cinnamon" or de == "cinnamon" :
            subprocess.call("sudo add-apt-repository ppa:embrosyn/cinnamon", shell = True)
            subprocess.call("sudo apt update", shell = True)
            subprocess.call("sudo apt install cinnamon", shell = True)

        elif de == "LXDE" or de == "Lxde" or de == "lxde" :
            subprocess.call("sudo apt-get install lxde", shell = True)

        elif de == "Openbox" or de == "openbox" :
            subprocess.call("sudo apt-get install openbox obconf", shell = True)

        elif de == "i3" or de == "I3" :
            subprocess.call("sudo apt-get install i3", shell = True)
        
        bool2 = input("Restart computer to apply changes?[y, n]: ")
        if bool2 == "y" :
            subprocess.call("restart")
        elif bool2 == "n" :
            print("_______________________________________________")

# Disk Commands
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
