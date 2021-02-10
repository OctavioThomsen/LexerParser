    #Variables auxiliares
TRAP_STATE = -1
RESULT_TRAP = "RESULT_TRAP"
RESULT_ACCEPTED = "ACCEPTED"
RESULT_NOT_ACCEPTED = "NOT ACCEPTED"
numeros = ["0","1","2","3","4","5","6","7","8","9"]


    #Función transición
def delta(state, caracter):
    #{q0, ["0",...,"9"], q1f}
    if state == 0 and caracter in numeros:
        return 1

    #{q1f, ["0",...,"9"], q1f}
    if state == 1 and caracter in numeros:
        return 1

    #{q1f, ".", q2}
    if state == 1 and caracter == ".":
        return 2

    #{q2, ["0",...,"9"], q3f}
    if state == 2 and caracter in numeros:
        return 3

    #{q3, ["0",...,"9"], q3f}
    if state == 3 and caracter in numeros:
        return 3
      
    return TRAP_STATE
        

    #Automata numeros
def automata_num(input):
    state = 0
    final = [1,3]
       
    for caracter in input:
        next_state = delta(state, caracter)
        #print(("transicion", state, caracter, next_state))
        state = next_state

    if state in final:
        #print( input, "pertenece al lenguaje")
        return RESULT_ACCEPTED

    if state != TRAP_STATE:
        #print( input, "aún no pertenece al lenguaje")
        return RESULT_NOT_ACCEPTED
        
    #print(input, "no pertenece al lenguaje")   
    return RESULT_TRAP


    #Tests
#assert(automata_num("222222")== RESULT_ACCEPTED)
#print (" ")
#assert(automata_num("124712986") == RESULT_ACCEPTED)
#print(" ")
#assert(automata_num("412.6171.6717")== RESULT_TRAP)
#print(" ")
#assert(automata_num("42069")== RESULT_ACCEPTED)
#print (" ")
#assert(automata_num("23432,234") == RESULT_TRAP)
#print(" ")
#assert(automata_num("24.76")== RESULT_ACCEPTED)
#print(" ")
#assert(automata_num("xdxdxdxd") == RESULT_TRAP)
#print(" ")
#assert(automata_num("87.") == RESULT_NOT_ACCEPTED)