# this is based on an algorithm called A-* search, which I have learned
# in the Udacity intro to AI course.
class Node:
    """each node represents an intermediate step in a path in the maze.
    loc: position of the node
    path: path so far to reach this node
    cost: len(path) + helper const func h() (see below)
    """
    up = (-1, 0)
    down = (1, 0)
    right = (0, 1)
    left = (0, -1)
    dirs = (up, down, right, left)
    dir_str = {up:'N', down:'S', right:'E', left:'W'}

    def __init__(self, loc, path, cost, parent=None, children=None):
        self.loc = loc
        self.path = path
        self.cost = cost
        if parent:
            self.parent = parent
        else:
            self.parent = None
        if children:
            self.children = children
        else:
            self.children = []

    def moved(self, dir):
        return (self.loc[0] + dir[0], self.loc[1] + dir[1])

class Tree:
    def __init__(self, map, root, goal):
        self.map = map
        self.root = root
        self.goal = goal
        self.frontier = [root]
        self.shortest_path = None
        self.been_here_before = {}
        for i in range(12):
            for j in range(12):
                self.been_here_before[(i, j)] = []

    def is_pit(self, loc):
        return self.map[loc[0]][loc[1]]

    def expand(self):
        """expand the search tree at the node with the lowest cost
        by length 1
        """
        # pick node with lowest cost from frontier
        self.frontier.sort(key=lambda x: x.cost)
        node = self.frontier[0]
        # check all 4 directions from the node to see if tree can be
        # expanded
        for dir in Node.dirs:
            # location of the new node.
            pos = node.moved(dir)
            # new node is good only if it does not go back to parent node
            # and the loc is not pit
            if pos != node.loc and self.is_pit(pos) == 0:
                # create new node
                child = Node(pos, node.path + Node.dir_str[dir],
                             len(node.path) + 1 + h(node.loc, pos),
                             parent=node)
                # however, if the new loc has been visited by another
                # path with even lower cost, then this node is useless
                # so ignore it.
                cost_check = [child.cost >= p.cost 
                              for p in self.been_here_before[pos]]
                if any(cost_check):
                    continue
                # this new node is good. add to bookkeeping data.
                node.children.append(child)
                self.frontier.append(child)
                self.been_here_before[child.loc].append(child)
                # if the new node happens to be the goal:
                # record it if it's the shortest so far.
                # don't quit algorithm here though, you might find
                # a better solution later. so keep searching untill
                # there is no frontier.
                if child.loc == self.goal:
                    if self.shortest_path:
                        if len(self.shortest_path) > len(child.path):
                            self.shortest_path = child.path
                    else:
                        self.shortest_path = child.path
        # once all possiblities for expanding this node is exhausted,
        # this node is not frontier anymore.
        self.frontier.remove(node)

    def search_route(self):
        """searches the shortest path to the goal.
        algorithm ends when there is no more frontier nodes.
        which means, no room for paths to expand.
        the shortest path found by then is returned.
        """
        while self.frontier != []:
            self.expand()
        return self.shortest_path

def debugprint(cond, x):
    if cond:
        print(x)

def h(loc1, loc2):
    """a helper auxiliary cost function to find the shortest path.
    it is just cartesian distance to the goal ignoring pits.
    it serves as a A-* cost for this algorithm
    """
    return abs(loc2[0] - loc1[0]) + abs(loc2[1] - loc1[1])

def checkio(map):
    start = (1, 1)
    goal = (10, 10)
    # for the root node (which is the start), path length is obiously 0,
    # so total cost is just helper function value to the goal.
    root = Node(start, '', h(start, goal))
    tree = Tree(map, root, goal)
    return tree.search_route()

test_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

test_map2 = [[1,1,1,1,1,1,1,1,1,1,1,1],[1,0,0,0,0,0,0,0,0,0,0,1],[1,0,1,1,1,1,1,1,1,1,1,1],[1,0,1,0,0,0,0,0,0,0,0,1],[1,0,0,0,1,1,1,1,1,1,0,1],[1,1,1,1,1,0,0,0,0,1,0,1],[1,1,1,1,1,1,0,0,1,1,0,1],[1,1,1,1,1,0,0,1,0,1,0,1],[1,1,1,1,1,1,0,0,0,1,0,1],[1,1,1,1,1,1,1,1,1,1,0,1],[1,1,1,1,1,1,0,0,0,0,0,1],[1,1,1,1,1,1,1,1,1,1,1,1]]

if __name__ == '__main__':
    print(checkio(test_map2))
