from Functions import *


def show_menu():
    #Functie care afiseaza meniul principal, folosita in loop-ul run()
    #Date de intrare: -
    #Date de iesire: -
    print("*" * 20)
    print("Optiunile tale sunt: ")
    print("\n--- Adaugare ---\n")
    print("adauga_scor <NUMAR> -> Adaugă scor pentru un nou participant (ultimul participant)")
    print("insereaza_scor <NUMAR>(PARTICIPANT) <NUMAR> -> Inserare scor pentru un participant")
    print("--- Modificare & Stergere ---")
    print("sterge_scor <NUMAR> -> Șterge scorul pentru participantul <NUMAR>")
    print("sterge_interval <NUMAR> <NUMAR> -> Șterge scorul pentru un interval de participanți")
    print("inlocuieste <NUMAR>(PARTICIPANT) <NUMAR>(POZITIA) <NUMAR>(NOU) -> Înlocuiește scorul de la un participant")
    print("\n--- Tiparire ---\n")
    print("mai_mic <NUMAR> -> Tipărește participanții care au scor mai mic decât un scor dat")
    print("ordonat -> Tipărește participanții ordonat după scor")
    print("mai_mare <NUMAR> -> Tipărește participanții cu scor mai mare decât un scor dat, ordonat după scor")
    print("\n--- Operații pe un subset de participanți ---\n")
    print("media <NUMAR> <NUMAR> -> Calculează media scorurilor pentru un interval dat")
    print("minim <NUMAR> <NUMAR> -> Calculează scorul minim pentru un interval de participanți dat")
    print("multiplu_10 <NUMAR> <NUMAR> -> Tipărește participanții dintr-un interval dat care au scorul multiplu de 10")
    print("\n--- Filtrare ---\n")
    print("filtrare <NUMAR> -> Filtrare participanți care au scorul multiplu unui număr dat / Restul se elimina")
    print("filrare_mai_mic <NUMAR> -> Filtrare participanți care au scorul mai mic decât un scor dat")
    print("\n--- Altele ---\n")
    print("undo -> reface ultima operatie")
    print("out -> u gettin out?:(")
    print("*" * 20)


def first_contact():
    #This is just for effects
    #Date de intrare: -
    #Date de iesire: -
    print("Bine ai venit, stimabile!\nAlege o optiune din meniu!\n")


def wait_for_input():
    #Functia care asteapta input-ul utilizatorului
    #Date de intrare: -
    #Date de iesire: n String
    n = input("Comanda dumitale este?\n>>> ")
    return n


def print_result(result_from_action):
    #Functia care tipareste rezultatul functiei
    #Date de intrare: result_from_action Dict | String
    print(result_from_action)


def do_action(scores, command, list_of_scores_along_time):
    #Functia care executa comanda utilizatorului
    #Date de intrare: command String
    #Date de iesire: -
    commands_dictionary = {"adauga_scor": add_score, "insereaza_scor": insert_score, "sterge_scor": delete_score, "sterge_interval": delete_range,
    "inlocuieste": replace, "mai_mic": lower_than, "ordonat": ordered, "mai_mare": bigger_than, "media": scores_range, "minim": minimum,
    "multiplu_10": multiple_of_10}
    try:
        cmd_params = split_command(command)
        cmd = cmd_params["cmd"]
        arg1 = cmd_params['arg1']
        arg2 = cmd_params['arg2']
        arg3 = cmd_params['arg3']

        if cmd in commands_dictionary:
            if arg3 is not None:
                print_result(commands_dictionary[cmd](scores, arg1, arg2, arg3))
            elif arg2 is not None:
                print_result(commands_dictionary[cmd](scores, arg1, arg2))
            elif arg1 is not None:
                print_result(commands_dictionary[cmd](scores, arg1))    
            elif arg1 is None:
                print_result(commands_dictionary[cmd](scores))      
        elif cmd == 'undo':
            scores = undo(scores, list_of_scores_along_time)  
            print("Ai dat timpul inapoi!!\n" + str(scores))
        else: 
            print(cmd)
            if cmd != 'out': print("Comanda nu exista!")
        check_for_eligibility(cmd, scores, list_of_scores_along_time)
        print("\n" * 3)
        return scores

        
    except IndexError:
        print("Nu ai scris destule argumente!")
    except ValueError:
        print("Trebuie scrise numere la argumente!!")
    except KeyError:
        print("Acest elev nu exista inca!")


def menuLoop(scores, list_of_scores_along_time):
    #Functia care lasa utilizatorul sa introduca comenzi in program
    #Date de intrare: -
    #Date de iesire: -
    first_contact()
    userInput = ''
    while userInput != 'out':
        show_menu()
        userInput = wait_for_input()
        scores = do_action(scores, userInput, list_of_scores_along_time)
    print("Iti urez o zi!")
