    #Variables auxiliares
TRAP_STATE = -1
RESULT_TRAP = "RESULT_TRAP"
RESULT_ACCEPTED = "ACCEPTED"
RESULT_NOT_ACCEPTED = "NOT ACCEPTED"


    #Función transición
def delta(state, caracter):
    #{q0, "m" , q1}
    if state== 0 and caracter == "m":
        return 1
    
    #{q1, "o" , q2}
    if state == 1 and caracter == "o":
        return 2
    
    #{q2, "s" , q3}
    if state == 2 and caracter == "s":
        return 3
    
    #{q3, "t" , q4}
    if state == 3 and caracter == "t":
        return 4
    
    #{q4, "r" , q5}
    if state == 4 and caracter == "r":
        return 5
    
    #{q5, "a" , q6}
    if state == 5 and caracter == "a":
        return 6
    
    #{q6, "r" , qf}
    if state == 6 and caracter == "r":
        return 7
    
    return TRAP_STATE
    
    
    #Autómata mostrar
def automata_mostrar(input):
    state = 0
    final = 7
        
    for caracter in input:
        next_state = delta(state, caracter)
        #print(("transicion", state, caracter, next_state))
        state = next_state

    if state == final:
        #print( input, "pertenece a la cadena")
        return RESULT_ACCEPTED
    
    if state != TRAP_STATE:
        #print (input, "aun no pertenece al lenguaje")
        return RESULT_NOT_ACCEPTED
    
    #print (input, "no pertenece al lenguaje")
    return RESULT_TRAP


    #Tests
#assert (automata_mostrar("mostrar") == RESULT_ACCEPTED)
#print(" ")
#assert(automata_mostrar("mostr") == RESULT_NOT_ACCEPTED)
#print(" ")
#assert (automata_mostrar("ostrar") == RESULT_TRAP)