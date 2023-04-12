# This is an implementation of the intuitive backtracking 
# search algorithm to solve the CSP(Constraint Satisfaction Problem):
# The Map Coloring Probem

R = 'red'
G = 'green'
B = 'blue'
state = {} # Contains the final variables assignments.Eg: {x1: R, x2: G}
variables = ['WA', 'NT', 'SA', 'QL', 'NSA', 'V', 'T']
domain = {R,G,B} # The domain of the variables
# Constraints: The adjacent states graph.
constraints = [('WA', 'NT'), ('WA','SA'), ('NT','QL'),('NT','SA'),('SA', 'NSA'),('SA','V'), ('NSA', 'V')] 
FAIL = None

test = {'WA':'g', 'NT':'b', 'SA':'r', 'QL':'g', 'NSA':'b', 'V':'g'}

def check_constraint(state:dict)->bool:
  # Check whether the assignment in the state have no conflict
  # Two adjacent states don't have the same color
  global constraints
  for tup in constraints:
    try:
      if state[tup[0]] == state[tup[1]]:
        # => Two adjacent states have the same color
        return False
    except:
      pass
  return True

def get_unassigned_var(state:dict)->tuple:
  # Return an unassigned variable
  # Return None if not found
  global variables
  for var in variables:
    if var not in state.keys():
      return var
  return None # Can be removed (by default it returns None)

def assign_value(state:dict, var:str,val:str):
  # Assign the given var the given val
  # and add it to the state
  state[var] = val
  return state

  
def check_goal(state:dict)->bool:
  # Check if the all variables have been assigned
  global variables
  if len(state.keys()) == len (variables):
    return True
  return False
  
def backtrackingRec(state:dict)->dict:
  # Searches for a possible solution and return it
  # Return the variable assignments in the state format (dict)
  if check_goal(state):
    return state
  var = get_unassigned_var(state)
  for c in domain:
    temp_state = assign_value(state,var,c)
    if check_constraint(temp_state):
      state = backtrackingRec(temp_state)
      if state != FAIL:
        return state
      # else remove the assignment
      del state[var]
  return FAIL # No assignment found for this iteration


res = backtrackingRec(state)
print(res)
