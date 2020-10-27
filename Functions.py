from Domain import *


def add_score(scores, new_score):
    #Function to add a new score to a new student
    #Date de intrare: scores {String: [int, int, int, ...]}
    #Date de iesire: -
    last_student_number = get_last_student_number(scores)
    new_student_number = last_student_number + 1
    new_student = "elev" + str(new_student_number)
    scores[new_student] = [new_score]


def insert_score(scores, student, new_score):
    #Functie care insereaza un scor nou la un elev existent
    #Date de intrare: scores
    #Date de iesire: -
    if get_number_of_grades(scores, student) == 10:
        #errorMessage("Acest elev are deja 10 note!")
        return
    scores[student].append(new_score)


def delete_score(scores, student):
    #Functie care sterge un scor de la un elev
    #Date de intrare: scores
    #Date de iesire: -
    scores[student] = []


def delete_range(scores, low, high):
    #Functie care sterge scorul de la un interval de elevi
    #Date de intrare: scores, low int, high int
    #Date de iesire: -
    for i in range(low, high + 1):
        scores["elev" + str(i)] = []


def replace(scores, student, position, new_grade):
    #Functie care inlocuieste o nota de la un student
    #Date de intrare: scores
    #                 student String
    #                 position int
    #                 new_grade int
    #Date de iesire: -
    if position > get_number_of_grades(scores, student): 
        #errorMessage("Elevul " + str(student) + " nu are atatea note!")
        return
    scores[student][position - 1] = new_grade 


def lower_than(scores, score):
    #Functie care returneaza o lista a elevilor cu scorurile mai mici ca cel dat
    #Date de intrare: scores, score Int
    #Date de iesire: lista_criterii
    summed_scores = {}
    for i in range(1, len(scores) + 1):
        if student_exists(scores, "elev" + str(i)) and get_summed_score_student(scores, "elev" + str(i)) < score:
            summed_scores["elev" + str(i)] = scores["elev" + str(i)]
    return summed_scores


def makeSenseOfOrderedScores(scores):
    #Functie care aseaza elevii pe locul lor dupa ce au fost sortati
    readableScores = {}
    for index, student in enumerate(scores.keys()):
        currentOrd = scores["elev" + str(index + 1)][-1]
        readableScores["elev" + str(currentOrd)] = scores["elev" + str(currentOrd)][:-1]
        #readableScores["elev" + str(currentOrd)] = readableScores["elev" + str(currentOrd)][:-1]
    return readableScores


def ordered(scores):
    #Functie care returneaza o copie a listei elevilor sortata
    #Date de intrare: scores Dict
    #Date de iesire: scores_temp Dict
    #scores_temp = dict(scores)
    scores_temp = {}
    for key in scores:
        scores_temp[key] = scores[key].copy()
    ord = False

    #Dam un index la toate elementele din dictionar

    for index, student in enumerate(scores_temp.keys()):
        scores_temp[student].append(index + 1)


    while not ord:
        ord = True
        for index in range(1, len(scores_temp) - 1):
            if(get_summed_score_student(scores_temp, "elev" + str(index)) > get_summed_score_student(scores_temp, "elev" + str(index + 1))) and scores_temp["elev" + str(index)] < scores_temp["elev" + str(index + 1)]:
                scores_temp["elev" + str(index)][-1], scores_temp["elev" + str(index + 1)][-1] = scores_temp["elev" + str(index + 1)][-1], scores_temp["elev" + str(index)][-1]
                ord = False

    '''while not ord:
        ord = True
        for index, student in enumerate(scores_temp.keys()):
            if index == len(scores_temp) - 1:
                break
            if (get_summed_score_student(scores_temp, student) > get_summed_score_student(scores_temp, "elev" + str(index + 2))) and scores_temp[student][-1] < scores_temp["elev" + str(index + 2)][-1]:
                scores_temp[student][-1], scores_temp["elev" + str(index + 2)][-1] = scores_temp["elev" + str(index + 2)][-1], scores_temp[student][-1]
                
                ord = False'''
    return makeSenseOfOrderedScores(scores_temp)


def bigger_than(scores, score):
    #Functie care returneaza elevii cu scorul mai mare decat cel dat, si le sorteaza
    #Date de intrare: scores Dict, score int
    #Date de iesire: summed_scores Dict
    summed_scores = {}
    ord_scores = ordered(scores)
    for i in range(1, len(ord_scores) + 1):
        if student_exists(ord_scores, "elev" + str(i)) and get_summed_score_student(ord_scores, "elev" + str(i)) > score:
            summed_scores["elev" + str(i)] = ord_scores["elev" + str(i)]
    return summed_scores



def scores_range(scores, low, high):
    #Functie care returneaza media scorurilor pe un interval dat
    #Date de intrare: scores Dict, low Int, high Int
    #Date de iesire: media Int
    media = 0
    number_of_studs = 0
    for index in range(low, high + 1):
        if student_exists(scores, "elev" + str(index)):
            for score in get_scores_student(scores, "elev" + str(index)):
                media += score
            number_of_studs += 1
    media /= number_of_studs
    return media


def minimum(scores, low, high):
    #Functie care returneaza scorul minim dintr-un interval de elevi
    #Date de intrare: scores Dict, low Int, high Int
    #Date de iesire: (minName String, minGrade Int) Tuplet
    minGrade = 11
    minName = ''
    for index in range(low, high + 1):
        if student_exists(scores, "elev" + str(index)):
            if get_summed_score_student(scores, "elev" + str(index)) < minGrade and get_summed_score_student(scores, "elev" + str(index)) != 0:
                minGrade = get_summed_score_student(scores, "elev" + str(index))
                minName = "elev" + str(index)

    if minGrade == 11:
        raise Exception("Nu exista scor minim pe intervalul selectat!\n")
    return minName, minGrade


def multiple_of_10(scores, low, high):
    #Functie care returneaza elevii care au scorul multiplii de 10
    #Date de intrare: scores Dict, low Int, high Int
    #Date de iesire: students Dict
    students = {}
    for index in range(low, high + 1):
        if student_exists(scores, "elev" + str(index)):
            if get_summed_score_student(scores, "elev" + str(index)) % 10 == 0 and get_number_of_grades(scores, "elev" + str(index)) != 0:
                students["elev" + str(index)] = scores["elev" + str(index)].copy()
    if students == {}:
        raise Exception("Nu au fost gasiti studenti cu note multiplu de 10!")
    return students


def filter(scores, score):
    #Functie care sterge notele tuturor elevilor ce nu au scorul multiplu de un numar dat
    #Date de intrare: scores Dict, score Int
    #Date de iesire: -
    for student in scores.keys():
        if get_summed_score_student(scores, student) % score != 0:
            scores[student] = []


def filter_less_than(scores, score):
    #Functie care sterge notele tuturor elevilor care au scorul mai mare decat scorul dat
    #Date de intrare: scores Dict, score Int
    #Date de iesire: -
    for student in scores.keys():
        if get_summed_score_student(scores, student) > score:
            scores[student] = []


def createCopyOfCurrentGrades(scores):
    #Functie care returneaza o copie a scorurilor pentru a fi stocate
    #Date de intrare: scores Dict
    #Date de iesire: cpyScores Dict
    cpyScores = {}
    for key in scores:
        cpyScores[key] = scores[key].copy()
    return cpyScores


def deleteLastElementOfList(list_of_scores):
    #Functie care sterge ultimul dictionar dintr-o lista de dictionare
    #Date de intrare: list_of_scores List[Dicts]
    #Date de iesire: -
    tempScores = []
    for index, key in enumerate(list_of_scores):
        if index == len(list_of_scores) - 1: break
        tempScores.append(key)
    list_of_scores.clear()
    list_of_scores[:] = tempScores


def undo(scores, list_of_scores_along_time):
    #Functie care readuce lista de scoruri la modul in care era inainte de ultima actiune
    #Date de intrare: scores Dict, list_of_scores_along_time List[Dicts]
    #Date de iesire: scores Dict
    scores.clear()
    tempScores = createCopyOfCurrentGrades(list_of_scores_along_time[-2])
    deleteLastElementOfList(list_of_scores_along_time)
    return createCopyOfCurrentGrades(tempScores)


def update_list_of_scores_along_time(scores, list_of_scores_along_time):
    #Functie care actualizeaza lista de scoruri de-a lungul timpului
    #Date de intrare: scores Dict, list... List[Dicts]
    #Date de iessire;: -
    list_of_scores_along_time.append(createCopyOfCurrentGrades(scores))


def check_for_eligibility(command, scores, list_of_scores_along_time):
    #Functie care verifica daca trebuie actualizata lista de scoruri, in caz ca da o actualizeaza
    #Date de intrare: command String, scores Dict, list... List(Dicts)
    #Date de iesire: -
    if command in ["adauga_scor", "insereaza_scor", "sterge_scor", "sterge_interval", "inlocuieste", "filtrare", "filtrare_mai_mic"]:
        update_list_of_scores_along_time(scores, list_of_scores_along_time)