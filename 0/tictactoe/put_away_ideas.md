    state = Node(state=board, action=None, parent=None)
    moves = []
    p = player(state.state)
    for action in actions(state.state):
        state = Node(state=result(state.state, action), action=action, parent=state)
        if p == O:
            state.util = MIN(state).util
        else:
            state.util = MAX(state).util
        moves.append({"action": state.action,
                      "util": state.util})
    
    if p == O:
        util = 2
        for move in moves:
            if move["util"] < util:
                optimal_move = move["action"]

    elif p == X:
        util = -2
        for move in moves:
            if move["util"] > util:
                optimal_move = move["action"]



    return optimal_move



def MIN(state):
    for possibility in state.possibilities:    
        
        new_state = Node(state=result(state.state, possibility), action=possibility, parent=state)
        new_state.parent.children.append(state)
        print(new_state.state, new_state.parent.state, new_state.children)
        util = MAX(new_state).util
        new_state.util = 2
        if util < new_state.util:
            new_state.util = util
        
        if terminal(new_state.state) == True:
            new_state.util = utility(new_state.state)
            return state
        
    if terminal(state.state):
        state.util = utility(state.state) 
        return state
    return MAX(state.parent)
    
    

    
    





def MAX(state):
    for possibility in state.possibilities:    
        
        new_state = Node(state=result(state.state, possibility), action=possibility, parent=state)
        new_state.parent.children.append(state)
        print(new_state.state, new_state.parent.state, new_state.children)
        util = MAX(new_state).util
        new_state.util = -2
        if util > new_state.util:
            new_state.util = util
        
        if terminal(new_state.state) == True:
            new_state.util = utility(new_state.state)
            return new_state
        
    if terminal(state.state):
        state.util = utility(state.state) 
        return state
    return MAX(state.parent)
    





///////////////////////////////////////////////////////////////////////////////////////////








    explored = Frontier()
    frontier = Frontier()
    state_now = Node(state=board, path=None, parent=None)
    frontier.add(state_now)
    state = None
    while frontier.empty() == False:
        state = frontier.remove()
        if terminal(state.state) == False:
            for action in state.action:
                resulting = result(state.state, action)
                if resulting not in frontier.list_states() and resulting not in explored.list_states():
                    node = Node(state=resulting, path=action, parent=state.state)
                    frontier.add(node)
                    explored.add(node)

        elif state.util == None and terminal(state.state) == True:
            state.util = utility(state.state)

    

    p = state.player
    if p == X:
        state.util = MIN(state)

    if p == O:
        state.util = MAX(state)



    return optimal_action





def MIN(state):
    util = 2
    for action in state.action:
        if state.util == None:
            print("MIN")
            state.util = MAX(Node(state=result(state.state, action), parent=state, path=action))
        elif state.util < util:
            util = state.util
    print(f"Util of MIN: {util}")
    return util





def MAX(state):
    util = -2
    for action in state.action:
        if state.util == None:
            print("MAX")
            state.util = MIN(Node(state=result(state.state, action), parent=state, path=action))
        elif state.util > util:
            util = state.util
    print(f"Util of MAX: {util}")
    return util


//////////////////////////////////////////////////////////////////
    if terminal(board):
        return None
    p = player(board)
    state = Node(state=board, action=None, parent=None)
    frontier.add(state)
    while frontier.empty() == False:
        state = frontier.remove()
        for action in actions(state.state):
            resulting = Node(state=result(state.state, action), action=action, parent=state.state)
            if resulting.state not in frontier.list_states() and resulting.state not in explored.list_states():
                frontier.add(resulting)
                explored.add(resulting)
    print(len(explored.list_states()))
    p = player(board)
    if p == O:
        akjs = MIN(state)
    else:
        lkaj = MAX(state)



////////////////////////////////////////////////////////////////////
class Frontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def remove(self):
        node = self.frontier[0]
        self.frontier.remove(node)
        return node

    def empty(self):
        return len(self.frontier) == 0
    
    def list_states(self):
        list = []
        for i in range(len(self.frontier)):
            list.append(self.frontier[i].state)
        return list

