import subprocess

print("Welcome to linux automation script")
print("Made by shorya Rawal, press any key to start(only start if you have enough internet): ")
input()

subprocess.call("sudo apt-get update", shell = True)
subprocess.call("sudo apt-get upgrade", shell = True)

print("starting to install the rquired applications for ease of use.")
while True :
    print("This can take 1gb internet, continue[y, n]: ")
    bool1 = input()
    if bool1 == "y" :
        subprocess.call("sudo apt-get install build-essential", shell = True)
        subprocess.call("sudo apt-get install wine-stable", shell = True)
        break
    elif bool1 == "n" :
        break
    else :
        print("Enter a valid answer.")

while True :
    print("Install Budgie Desktop on your system, this can also take 500 - 800mb of internet [y, n]: ")
    bool2 = input()
    if bool2 == "y" :
        subprocess.call("sudo add-apt-repository ppa:budgie-remix/ppa", shell = True)
        subprocess.call("sudo apt update", shell = True)
        subprocess.call("sudo apt-get install ubuntu-budgie-desktop", shell = True)

        print("The budgie desktop is installed, restart to apply changes?[y, n]: ")
        bool3 = input()
        
        if bool3 == "y" :
            subprocess.call("restart", shell = True)
            break

        elif bool3 == "n" :
            print("Aborting restart...")
            break

        else :
            print("Enter a valid answer.")
            
    elif bool2 == "n" :
        break
    else :
        print("Enter a valid answer.")

pritn("Exiting Script.")