from queue import Queue
from puzzleBoard import Puzzle

def depth_limited_search(initial_state, depth):
    depth_limit = depth
    start_node = Puzzle(initial_state, None, None, 0, 0)
    if start_node.goal_test():
        return start_node.find_solution()
    stack = []
    stack.append(start_node)
    explored = []
    while (stack):
        node = stack.pop()
        explored.append(node.state)
        if (node.path_cost < depth_limit):
            children = node.generate_child()
            for child in children:
                if child.state not in explored:
                    if child.goal_test():
                        return child.find_solution()
                    stack.append(child)
    return