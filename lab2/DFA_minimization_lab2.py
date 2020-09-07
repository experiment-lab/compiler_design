# minimization of dfa 
#  assuming that this dfa does not contain any non-reachable state
# input format
#  6,0 <---- no. of states and inital state 
#  input symbol can be any two char or int , here we are taking a and b by default
#  1,2,4  <---- final states
# state  $(state,a)  $(state,b)   <---- transition of a and b of state
#   0         1           3
#   1         5           2 
#   2         5           2
#   3         4           0
#   4         5           2
#   5         5           5

# ------------ DFA minimization by equivalence theorm ---------------

# inputs
M = lambda : map(int, input().split())
print("Enter No. of state, inital state (space separeted) : ",end="")
n,start = M()
print("Enter final states : ",end="")
final_states = list(M())
print("Enter state  $(state,a)  $(state,b) : ")

# partitions
final_state_transitions = {}      # set of final states
non_final_state_transitions = {}  # set of non final states

for _ in range(n):
    trans = list(M())
    key = trans[0]
    if key in final_states:
        value = trans[1:]
        final_state_transitions.setdefault(key,value)
    else:
        value = trans[1:]
        non_final_state_transitions.setdefault(key,value)
   
# check if we can remove dublicate states from non final set

check_non_final_state = []
key_non_final_state = []
remove_non_final_state = []

for key,value in non_final_state_transitions.items():
    a = str(value[0]) + str(value[1])
    if a not in check_non_final_state:
        check_non_final_state.append(a)
        key_non_final_state.append(key)
    else:
        if key==start:
            state = key_non_final_state[check_non_final_state.index(a)]
            remove_non_final_state.append(state)
        else:
            remove_non_final_state.append(key)

# check if we can remove dublicate states fron final state set
 
check_final_state  =  []
key_final_state = []
remove_final_state = []

for key,value in final_state_transitions.items():
    a = str(value[0]) + str(value[1])
    if a not in check_final_state:
        check_final_state.append(a)
        key_final_state.append(key)
    else:
        if key==start:
            state = key_final_state[check_final_state.index(a)]
            remove_final_state.append(state)
        else:
            remove_final_state.append(key)

# finding minimun no. of states required for dfa
remove_state = remove_non_final_state + remove_final_state
print("Minimum no. of states are : ",(n-len(remove_state)))

print("state  $(state,a)  $(state,b)")

# output
for i in non_final_state_transitions:
    if i not in remove_state:
        print(i,"        ",non_final_state_transitions[i][0],"        ",non_final_state_transitions[i][1])

for i in final_state_transitions:
    if i not in remove_state:
        print(i,"        ",final_state_transitions[i][0],"        ",final_state_transitions[i][1])
