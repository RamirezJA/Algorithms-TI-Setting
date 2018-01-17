#Question 1
def question1(s,t):
    m = len(s)
    n = len(t)
    if m > n: return false
    target = dict.fromkeys(s,0)
    for c in s: target[c] += 1

    #process initial window
    for i in range(m):
        c = t[i]
        if c in target:
            target[c] -= 1
    discrepancy = sum(abs(target[c]) for c in target)

    #repeatedly check then slide:
    for i in range(m,n):
        if discrepancy == 0:
            return True
        else:
            #first process letter from m steps ago from t
            c = t[i-m]
            if c in target:
                target[c] += 1
                if target[c] > 0: #just made things worse
                    discrepancy +=1
                else:
                    discrepancy -=1
            #now process new letter:
            c = t[i]
            if c in target:
                target[c] -= 1
                if target[c] < 0: #just made things worse
                    discrepancy += 1
                else:
                    discrepancy -=1
    #if you get to this stage:
    return discrepancy == 0

# Test case 1 checking for anagram in subject
print question1("ad", "udacity")
#True
# Test case 2 with empty string
print question1("", "udacity")
#True
# Test case 3 using words in subject but not in order
print question1("uiy", "udacity")
#False
# Test case 4 unusually long
print question1("rove", "stack overflow is really cool")
#True

#Question 2
#creates an empty dictionary
store = {}
def question2(string):
    if string in store.keys():
        return store[string]
    #returns string if its a palindrome
    if string == string[::-1]:
        return string
    else:
        #goes trough string items from left to right
        left = question2(string[:-1])
        right = question2(string[1:])
        iterate = [left, right]
        #finding max using len
        store[string] = max(iterate, key=len) 
        return store[string]

#Test Case 1 
print question2('forgeeksskeegfor')
#Expected output: geeksskeeg
#Test Case 2 unusually long
print question2('alskdjfj laksjd flkajs racecar idk lol')
#Expected output: racecar
#Test Case 3 blank
print question2('')
#Expected output: blank

# http://codegist.net/code/find-longest-palindrome-in-a-store-python/

#Question 3 using Kruskal algorithm
parent = dict()
sort = dict()
#creates a batch of vertices
def create_batch(vert):
    parent[vert] = vert
    sort[vert] = 0
#locates vertices
def locate(vert):
    if parent[vert] != vert:
        parent[vert] = locate(parent[vert])
    return parent[vert]
#creates unions
def union(vert1, vert2):
    root1 = locate(vert1)
    root2 = locate(vert2)
    if root1 != root2:
        if sort[root1] > sort[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if sort[root1] == sort[root2]: sort[root2] += 1

#Using Kruskal algorithm
def question3(G):
    for vert in G['verts']:
        create_batch(vert)

    minspantree = set()
    edges = list(G['edges'])
    edges.sort()
    for edge in edges:
        weight, vert1, vert2 = edge
        if locate(vert1) != locate(vert2):
            union(vert1, vert2)
            minspantree.add(edge)
    return sorted(minspantree)

G = {
        'verts': ['A', 'B', 'C', 'D', 'E'],
        'edges': set([
            (2, 'A', 'B'),
            (3, 'B', 'D'),
            (4, 'D', 'E'),
            (1, 'A', 'C'),
            (3, 'C', 'E')
            ])
        }

print "Test case one"
print(question3(G)) 
#Expected Output [(1, 'A', 'C'), (2, 'A', 'B'), (3, 'B', 'D'), (3, 'C', 'E')]

G = {
        'verts': ['A', 'B', 'C', 'D', 'E'],
        'edges': set([
            (1, 'A', 'B'),
            (1, 'B', 'D'),
            (1, 'D', 'E'),
            (1, 'A', 'C'),
            (1, 'C', 'E')
            ])
        }

print "test case two"
print(question3(G)) 
#Expected Output [(1, 'A', 'B'), (1, 'A', 'C'), (1, 'B', 'D'), (1, 'C', 'E')]


G = {
        'verts': ['A', 'B', 'C', 'D', 'E','F', 'G', 'H', 'I','J','K', 'L', 'N', 'O',],
        'edges': set([
            (1, 'A', 'B'),
            (3, 'A', 'C'),
            (2, 'B', 'E'),
            (5, 'E', 'G'),
            (1, 'G', 'I'),
            (2, 'I', 'K'),
            (4, 'K', 'N'),
            (2, 'N', 'O'),
            (5, 'O', 'L'),
            (1, 'L', 'J'),
            (3, 'J', 'H'),
            (2, 'H', 'F'),
            (1, 'F', 'D'),
            (3, 'D', 'C')
            ])
        }

print "test case three unusually long"
print(question3(G))
"""
Expected Output [(1, 'A', 'B'), (1, 'F', 'D'), (1, 'G', 'I'), (1, 'L', 'J'), (2, 'B', 'E'), (2, 'H', 'F'), (2, 'I', 'K'),
(2, 'N', 'O'), (3, 'A', 'C'), (3, 'D', 'C'), (3, 'J', 'H'), (4, 'K', 'N'), (5, 'E', 'G')]
"""

"""
Attributioon: https://pythonexample.com/code/prim-minimum-spanning-tree-algorithm-python/
              https://gist.github.com/vevurka/539d82eb0ba60c16aa8aa65610c627df  
"""
# A recursive python program to find LCA of two Nodes
# n1 and n2

# Tree Node
class Node:

    # Constructor to create a new Node
    def __init__(self, Data):
        self.Data = Data
        self.left = None
        self.right = None

class BiSTree(object):
    def __init__(self, root):
        #super(BiSTree, self).__init__() should I use this Atom auto populated it?
        self.root = Node(root)

# Tree
def formT(t, n):
    if T and n in T:
        c = T[n]
        for i, cnode in enumerate(c):
            if cnode == 1:
                t.insert(i)
                formT(t, i)

# Function to find LCA of n1 and n2.
def LowestCA(root, n1, n2):

    # Base Case
    if root is None:
        return None

# root greater than n1,n2 left
    if(root.Data > n1 and root.Data > n2):
        return LowestCA(root.left, n1, n2)

# root less than n1,n2 right
    if(root.Data < n1 and root.Data < n2):
        return LowestCA(root.right, n1, n2)

    return root

# Driver program to test above function

# Let us construct the BST shown in the figure
def question4(T, r, n1, n2):

    # tree
    t = BiSTree(r)


    # LowestCA
    return LowestCA(t.root, n1, n2)

# First testcase
T = [[0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [1, 0, 0, 0, 1],
     [0, 0, 0, 0, 0]]
r = 3
n1 = 1
n2 = 4

print question4(T, r, n1, n2).Data
# Should return 3

# EdgeCase one
T = None
r = 1
n1 = 3
n2 = 2

print question4(T, r, n1, n2)
# Should return None

# Third testcase
T = [[0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [1, 0, 0, 1, 0],
     [0, 0, 0, 0, 0],
     [1, 0, 1, 0, 0]]
r = 4
n1 = 1
n2 = 4

print question4(T, r, n1, n2).Data
# Should return 4

# Fourth testcase EdgeCase unusually large
T = [[0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [1, 0, 0, 1, 0],
     [0, 0, 0, 0, 0],
     [1, 0, 1, 0, 0]]
r = 4
n1 = 200
n2 = 200

print question4(T, r, n1, n2)
# Should return None

# This code is contributed by Nikhil Kumar Singh(nickzuck_007) from 
# https://www.geeksforgeeks.org/lowest-common-ancestor-in-a-binary-search-tree/
# http://www.openbookproject.net/thinkcs/python/english2e/ch21.html

