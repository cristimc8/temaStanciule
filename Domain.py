def get_scores_student(scores, student):
    return scores[student]


def get_last_student_number(scores):
    #Functie care returneaza numarul ultimului elev din lista
    #Date de intrare: Lista de scoruri
    #Date de iesire: number int
    if len(scores) > 0:
        return int(list(scores)[-1][-1])
    return 0


def get_last_student_name(scores):
    if len(scores) > 0:
        return str(list(scores)[-1])
    return None


def get_number_of_grades(scores, student):
    return len(get_scores_student(scores, student))


def student_exists(scores, student):
    if student in scores.keys(): return True
    return False


def get_scores_for_range(scores, low, high):
    scores_to_return = {}
    for i in range(low, high + 1):
        if student_exists(scores, "elev" + str(i)):
            scores_to_return["elev" + str(i)] = scores["elev" + str(i)]
    return scores_to_return


def get_summed_score_student(scores, student):
    #Functie care returneaza suma scorurilor studentului
    sum = 0
    for score in get_scores_student(scores, student):
        sum += score
    return sum