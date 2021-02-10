	#Variables auxiliares
TRAP_STATE = -1
RESULT_TRAP = "RESULT_TRAP"
RESULT_ACCEPTED = "ACCEPTED"
RESULT_NOT_ACCEPTED = "NOT ACCEPTED"
characters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]

	#Función transición
def delta_id(state, caracter):
		#{q0, ["a",...,"z"/ "A",...,"Z"], q1f}
	if state == 0 and caracter in characters:							 
		return 1

		#{q1, ["a",...,"z"/ "A",...,"Z"], q1f}
	if state == 1 and caracter in characters:
		return 1

		#{q1, ["0",...,"9"], q1f}
	if state == 1 and caracter in numbers:
		return 1

	return TRAP_STATE


	#Autómata id
def automata_id(input):
	state = 0
	final = 1

	for caracter in input:
	 	next_state = delta_id(state, caracter)
	 	#print(("transicion", state, caracter, next_state))
	 	state = next_state		

	if state == final:
		#print(input, "pertenece al lenguaje") 	
		return RESULT_ACCEPTED

	#print(input, "no pertenece al lenguaje")
	return RESULT_TRAP
	

	#Tests
#print(" ")
#assert(automata_id("}") == RESULT_TRAP)
#print(" ")
#assert(automata_id("H") == RESULT_TRAP)
#print(" ")
#assert(automata_id("x") == RESULT_ACCEPTED)
#print(" ")
#assert(automata_id("asd123") == RESULT_ACCEPTED)
#print(" ")
#assert(automata_id("DSA321") == RESULT_ACCEPTED)
#print(" ")
#assert(automata_id("hola") == RESULT_ACCEPTED)
#print(" ")
#assert(automata_id("HOLA") == RESULT_ACCEPTED)
#print(" ")
#assert(automata_id("1998") == RESULT_TRAP)