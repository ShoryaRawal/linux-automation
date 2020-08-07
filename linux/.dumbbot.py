from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hello|hey",
        ["hello", "hey there", "howdy",]
    ],
    [
        r"how was your day ?",
        ["well being that I was created seconds ago, kinda good.",]
    ],
    [
        r"what is your name?",
        ["My name is Dumbot, and I'm dumb",]
    ],
    [
        r"my name is (.*)",
        ["%1, wow that's a name.",]
    ],
    [
        r"dont (.*) dumb",
        ["Believe me I'm really dumb",]
    ],
    [
        r"(.*) plus|minus|multiply|divide (.*)",
        ["uhhhhhh, 667 i guess?", "No", "69",]
    ],
    [
        r"quit",
        ["Bye, hope to meet you again NOT", "You do know that it kills me, right?"]
    ],
    [
        r"(.*) videogame|game ?",
        ["fortnite good minecraft bad", "The greatest game, Fortnite",]
    ],
    [
        r"(.*) actor|actress ?",
        ["Ricado milos",]
    ],
    [
        r"when (.*) created?",
        ["Seconds ago",]
    ],
    [
        r"(.*) movie|film ?",
        ["Shrek five",]
    ],
    [
        r"why (.*) dumb?",
        ["idk, but do you think im hot?",]
    ],
    [
        r"how (.*) weather?",
        ["Like flames coming down from sky", "like icecubes falling from the sky", "like AC/DC playing in the clouds",]
    ],
    [
        r"(.*) food ?",
        ["RAM",]
    ],
    [
        r"tell (.*) yourself",
        ["No", "Well, I got created seconds ago and that's it."]
    ],
    [
        r"(.*) person ?",
        ["The man standing behind you", "Donald Trump",]
    ]
]

def dumbBot() :
    print("Hi, I'm dumb bot.\nPlease use lowercase english only.\nEnter quit to leave.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__" :
    dumbBot()
