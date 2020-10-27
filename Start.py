from TestUnit import runAllTests
from UI import menuLoop

def run():
    #Functia principala a programului, tine loop-ul in viata
    #Date de intrare: -
    #Date de iesire: -
    runAllTests()
    scores = {}
    list_of_scores_along_time = [scores.copy()]
    menuLoop(scores, list_of_scores_along_time)