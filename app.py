
from random import choice


option = input("Debes escribir una de las siguientes opciones: rock, paper o scissors. Presiona Enter para continuar...\n")

optionMachine = choice(["rock", "paper", "scissors"])

match(option.lower()):
    case "rock":
        if optionMachine == "rock":
            print("Empate")
        elif optionMachine == "paper":
            print("Perdiste")
        else:  
            print("Ganaste")
    case "paper":
        if optionMachine == "rock":
            print("Ganaste")
        elif optionMachine == "paper":
            print("Empate")
        else:  
            print("Perdiste")
    case "scissors":
        if optionMachine == "rock":
            print("Perdiste")
        elif optionMachine == "paper":
            print("Ganaste")
        else:  
            print("Empate")
    case _:
        print("Opción no válida")
print(f"La máquina eligió: {optionMachine}")