def get_scores_student(scores, student):
    #Functie care returneaza scorurile unui student specific
    #Date de intrare: scores Dict
    #                 student String
    #Date de iesire: scores List<Int>
    return scores[student]


def get_last_student_number(scores):
    #Functie care returneaza numarul ultimului elev din lista
    #Date de intrare: Lista de scoruri
    #Date de iesire: number int
    if len(scores) > 0:
        return int(list(scores)[-1][-1])
    return 0


def get_last_student_name(scores):
    #Functie care returneaza numele ultimului student din lista
    #Date de intrare: scores Dict
    #Date de iesire: nume String
    if len(scores) > 0:
        return str(list(scores)[-1])
    return None


def get_number_of_grades(scores, student):
    #Functie care returneaza numarul de note pe care un student le are
    #Date de intrare: scores Dict
    #                 student String
    #Date de iesire: lungime Int
    return len(get_scores_student(scores, student))


def student_exists(scores, student):
    #Functie care verifica daca un student exista pe baza numelui
    #Date de intrare: scores Dict
    #                 student String
    #Date de iesire: exista Boolean
    if student in scores.keys(): return True
    return False


def get_scores_for_range(scores, low, high):
    #Functie care returneaza scorurile studentiilor dintr-un interval
    #Date de intrare: scores Dict
    #                 low Int
    #                 high Int
    #Date de iesire: scores_to_return Dict
    scores_to_return = {}
    for i in range(low, high + 1):
        if student_exists(scores, "elev" + str(i)):
            scores_to_return["elev" + str(i)] = scores["elev" + str(i)]
    return scores_to_return


def get_summed_score_student(scores, student):
    #Functie care returneaza suma scorurilor studentului
    #Date de intrare: scores Dict
    #                 student String
    #Date de iesire: sum Int
    sum = 0
    for score in get_scores_student(scores, student):
        sum += score
    return sum


def get_summed_score_student_for_sorting(scores, student):
    #Functie care returneza suma scorurilor studentului, minus ultimul numar, care este, in sortare doar un indice
    #Date de intrare: scores Dict
    #                 student String
    #Date de iesire: sum Int
    sum = 0
    for index, score in enumerate(get_scores_student(scores, student)):
        if index == len(get_scores_student(scores, student)) - 1: break
        sum += score
    return sum