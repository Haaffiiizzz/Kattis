

class Problem(object):
    """The abstract class for a formal problem. A new domain subclasses this,
    overriding `actions` and `results`, and perhaps other methods.
    The default heuristic is 0 and the default action cost is 1 for all states.
    When yiou create an instance of a subclass, specify `initial`, and `goal` states 
    (or give an `is_goal` method) and perhaps other keyword args for the subclass."""

    def __init__(self, initial=None, goal=None, **kwds): 
        self.__dict__.update(initial=initial, goal=goal, **kwds) 
        
    def actions(self, state):        raise NotImplementedError
    def result(self, state, action): raise NotImplementedError
    def is_goal(self, state):        return state == self.goal
    def action_cost(self, s, a, s1): return 1
    def h(self, node):               return 0
    
    def __str__(self):
        return '{}({!r}, {!r})'.format(
            type(self).__name__, self.initial, self.goal)
    

class Node:
    "A Node in a search tree."
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.__dict__.update(state=state, parent=parent, action=action, path_cost=path_cost)

    def __repr__(self): return '<{}>'.format(self.state)
    def __len__(self): return 0 if self.parent is None else (1 + len(self.parent))
    def __lt__(self, other): return self.path_cost < other.path_cost
    
    
failure = Node('failure', path_cost=math.inf) # Indicates an algorithm couldn't find a solution.
cutoff  = Node('cutoff',  path_cost=math.inf) # Indicates iterative deepening search was cut off.
    
    
def expand(problem, node):
    "Expand a node, generating the children nodes."
    s = node.state
    for action in problem.actions(s):
        s1 = problem.result(s, action)
        cost = node.path_cost + problem.action_cost(s, action, s1)
        yield Node(s1, node, action, cost)
        

def path_actions(node):
    "The sequence of actions to get to this node."
    if node.parent is None:
        return []  
    return path_actions(node.parent) + [node.action]


def path_states(node):
    "The sequence of states to get to this node."
    if node in (cutoff, failure, None): 
        return []
    return path_states(node.parent) + [node.state]

class CountCalls:
    """Delegate all attribute gets to the object, and count them in ._counts"""
    def __init__(self, obj):
        self._object = obj
        self._counts = Counter()
        
    def __getattr__(self, attr):
        "Delegate to the original object, after incrementing a counter."
        self._counts[attr] += 1
        return getattr(self._object, attr)
    

def breadthfirst(problem):
    node = Node(problem.initial)
    if problem.is_goal(problem.initial):
        return node
    frontier = FIFOQueue([node])
    reached = {problem.initial}
    while frontier:
        node = frontier.pop()
        for child in expand(problem, node):
            s = child.state
            if problem.is_goal(s):
                return child
            if s not in reached:
                reached.add(s)
                frontier.appendleft(child)
    return -1 #fails
class MazeProblem(Problem):
    
    def __init__(self, initial, goal, maze):
        """Define a Maze problem. Maze is a grid of 1s and 0s, where 1s are blocked."""
        super().__init__(initial, goal)
        self.maze = maze

    def actions(self, state):
        """Return actions available from the current state."""
        actions = []
        x, y = state
        if y > 0 and self.maze[x][y-1] == 0: actions.append("Up")
        if y < len(self.maze[0]) - 1 and self.maze[x][y+1] == 0: actions.append("Down")
        if x > 0 and self.maze[x-1][y] == 0: actions.append("Left")
        if x < len(self.maze) - 1 and self.maze[x+1][y] == 0: actions.append("Right")
        return actions

    def result(self, state, action):
        """Return the resulting state from taking an action at the current state."""
        x, y = state
        if action == "Up": return (x, y-1)
        if action == "Down": return (x, y+1)
        if action == "Left": return (x-1, y)
        if action == "Right": return (x+1, y)

# Define a simple maze as a list of lists where 0 is open and 1 is a wall
maze = [[0, 0, 0, 0, 1],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]]

# Create a MazeProblem instance
initial_state = (0, 0)  # Start at the top-left corner
goal_state = (4, 4)     # Goal is the bottom-right corner
maze_instance = MazeProblem(initial_state, goal_state, maze)