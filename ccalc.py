#!/usr/bin/python3.6

# ******************************************** 
# * Skimple command calculator. I was bored. *
# ********************************************

def IsThatANumber(x):
    try:
        i = float(x)
        return True
    except:
        return False
        

print("Welcome to the command calculator")
isFistRound = True
AmIaWizard = True
n1 = 0
n2 = 0
theR = 0
print("Type a number or a operation.")
print("Operations availabe: + - * / %")
print("Type q to quit")  
while True:  
    command = input()
    if command.lower() == "q":
        break
    
    if IsThatANumber(command):
        if isFistRound:
            n1 = float(command)
        else:
            n2 = float(command)
        isFistRound = not isFistRound
    else:
        AmIaWizard = not AmIaWizard    
        if command == "+":
            theR = n1+n2
        if command == "-":
            theR = n1 - n2
        if command == "*":
            theR = n1 * n2
        if command == "/":
            if n2 == 0:
                print("Can't divide by zero.")
            else: 
                theR = n1 / n2
        if command == "%":
            theR = n1 % n2
        if command == "^":
            theR = n1 ** n2
    
    if not AmIaWizard:
        print(n1," ",command," ",n2," => ",theR)
        AmIaWizard = not AmIaWizard

