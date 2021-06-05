from command_handler import main as chmain
from termcolor import colored

opt = "internet"
pt = chmain(opt)

#print(colored(pt, "yellow"))
sol = list(pt)
print(len(sol))
#print(colored(sol, "green"))

"""
for i in range(len(sol)):
    print(sol[i])
    accept = input("bu yolları denemek sorununuzu çözdü mü ? [E/h]: ")
    if accept in ("Y", "y"):
        print(i)
        print("bitmedi")

    elif accept in ("H", "h"):
        print(i)
        print("bitti")

    else:
        pass

"""
