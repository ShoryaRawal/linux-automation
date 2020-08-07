from nltk.chat.util import Chat, reflections

pairs =[
    [
        r"hi|hello|hey",
        ["Hi", "Hello there",]
    ],
    [
        r"thanks (.*)",
        ["Alawys happy to help",]
    ],
    [
        r"(.*) password|username (.*) lock ?",
        ["Username = admin, Password = qw", "Username = admin, Password = qw",]
    ],
    [
        r"(.*) commands ?",
        ["There's a command 'list', you can use it to browse a list of commands.",
          "Use 'list' command to browse a list of commands",]
    ],
    [
        r"(.*) dumbBot|dumbbot ?",
        ["You can try talking with dumbbot, but I'm warning you, he's annoying.", "You can try talking with dumbbot, but I'm warning you, he's annoying.",]
    ],
    [
        r"(.*) basic commands ?",
        ["Those just perform some basic commands.", "Use those to perform basic functions",]
    ],
    [
        r"(.*) file commands ?",
        ["Use those to manage files",]
    ],
    [
        r"(.*) desktop enviroments ?",
        ["You can use them to modify your current GUI.",]
    ],
    [
        r"(.*) dependencies|dependency ?",
        ["You will be needed to download some dependencies for python for smooth functionality.\nJust open another terminal and give 'sudo apt-get install python3-(dependency name)' and it will start the download.",
         "You will be needed to download some dependencies for python for smooth functionality.\nJust open another terminal and give 'sudo apt-get install python3-(dependency name)' and it will start the download.",]
    ],
    [
        r"dependencies|dependency (.*) ?",
        ["You will be needed to download some dependencies for python for smooth functionality.\nJust open another terminal and give 'sudo apt-get install python3-(dependency name)' and it will start the download.",
         "You will be needed to download some dependencies for python for smooth functionality.\nJust open another terminal and give 'sudo apt-get install python3-(dependency name)' and it will start the download.",]
    ],
    [
        r"(.*) windows ?",
        ["This program is only made to be run on bash,\nwrite to the creater for a cmd release too\nYou can find how to contact him on creds page",]
    ],
    [
        r"missing (.*)",
        ["Try re-cloning the project, any file must have been missing.",]
    ],
    [
        r"quit",
        ["Bye, hope you got the solution you needed",]
    ]
]

def helpbot() :
    print("(Please use lowercase english only)\n(type quit to exit)\nHello, What might your problem be?")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__" :
    helpbot()