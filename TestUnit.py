from Functions import *
from Domain import *


def test_add_new_score(scores):
    add_score(scores, 8)
    assert(get_scores_student(scores, get_last_student_name(scores)) == [8])


def test_insert_score(scores, student, new_score):
    insert_score(scores, student, new_score)
    assert(get_scores_student(scores, student) == [10, 7])


def test_delete_score(scores, student):
    delete_score(scores, student)
    assert(get_scores_student(scores, student) == [])
    

def test_delete_range(scores, low, high):
    delete_range(scores, low, high)
    assert(get_scores_for_range(scores, low, high) == {'elev1': [], 'elev2': [], 'elev3': []})


def test_replace(scores, student, position, new_grade):
    replace(scores, student, position, new_grade)
    assert(get_scores_student(scores, student)[position - 1] == new_grade)


def test_lower_than(scores, score):
    returned_list = lower_than(scores, score)
    assert(returned_list == {'elev1': [], 'elev2': [], 'elev3': [], 'elev4': [1, 7], 'elev6': [8]})


def test_ordered(scores):
    scores_ordered = ordered(scores)
    assert(scores_ordered == {'elev1': [], 'elev2': [], 'elev3': [], 'elev4': [1, 7], 'elev6': [8], 'elev5': [5, 10]})


def test_bigger_than(scores, score):
    returned_list = bigger_than(scores, score)
    assert(returned_list == {'elev5': [5, 10]})


def test_media(scores, low, high):
    media = scores_range(scores, low, high)
    assert(media == 2.0)


def test_minimum(scores, low, high):
    try:
        min = minimum(scores, low, high)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "Nu exista scor minim pe intervalul selectat!\n")


def test_multiple_of_10(scores, low, high):
    studs = multiple_of_10(scores, low, high)
    assert(studs == {'elev3': [10]})


def test_filter(scores, score):
    filter(scores, score)
    assert(scores == {'elev1': [], 'elev2': [], 'elev3': [10], 'elev4': [], 'elev5': [5, 10], 'elev6': []})


def test_filter_less_than(scores, score):
    filter_less_than(scores, score)
    assert(scores == {'elev1': [], 'elev2': [], 'elev3': [10], 'elev4': [], 'elev5': [], 'elev6': []})


def runAllTests():
    #Functia care ruleaza toate testele
    testing_scores_list = {"elev1": [1, 4, 5, 6], "elev2": [1, 5, 3], "elev3": [10], "elev4": [1, 5], "elev5": [5, 10]}
    test_add_new_score(testing_scores_list)
    test_insert_score(testing_scores_list, "elev3", 7)
    test_delete_score(testing_scores_list, "elev1")
    test_delete_range(testing_scores_list, 1, 3)
    test_replace(testing_scores_list, "elev4", 2, 7)
    test_lower_than(testing_scores_list, 9)
    test_ordered(testing_scores_list)
    test_bigger_than(testing_scores_list, 10)
    test_media(testing_scores_list, 1, 4)
    test_minimum(testing_scores_list, 1, 2)
    insert_score(testing_scores_list, "elev3", 10)
    test_multiple_of_10(testing_scores_list, 1, 3)
    test_filter(testing_scores_list, 5)
    test_filter_less_than(testing_scores_list, 11)


runAllTests()