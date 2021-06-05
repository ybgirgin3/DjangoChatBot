# get commands from chatbot and parse it 
# find topic of the command
# response it using that

import random
# import all commands
from commands import helper_commands as hc
from TurkishStemmer import TurkishStemmer
stemmer = TurkishStemmer()
#stemmer.stem("okuldakilerden")

def command_parse(cmd: str) -> str:
    # parse command
    data = cmd.split(" ")

    # if one of the point command list items
    # is exist in command.py
    for pt in data:
        pts = stemmer.stem(pt)
        #return pts
        if pts in hc.keys():
            # if exist return one of the soluitons randomly
            #print(hc.values())
            #return hc[pt]
            print(f"algılanan hata '{pts}'")
            return hc[pts]
            

def main(cmd: str) -> str:
    # parse command
    # returns multiple item dict
    return command_parse(cmd)


"""
ret = command_parse(input("cmd: "))
print(ret)
"""
