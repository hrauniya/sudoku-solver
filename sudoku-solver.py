# Austin Alcancia and Harsha Rauniyar
# 11/15/21
# This algorithm takes an input of sudoku puzzles and outputs the solution

array = []
row = []
constraints = []
from collections import deque
import copy

# return the correct 3x3 square to add as constraints for a given node
def return3x3squarevalues(array,row,col):
    square= set()
    if row>=0 and row<3 and col>=0 and col<3:
        for i in range(0,3):
            for y in range(0,3):
                if i != row and y != col:
                    square.add((i, y))

    elif row>=3 and row<6 and col>=0 and col<3 :
        for i in range(3,6):
            for y in range(0, 3):
                if i != row and y != col:
                    square.add((i, y))

    elif row>=6 and row<9 and col>=0 and col<3 :
        for i in range(6,9):
            for y in range(0, 3):
                if i != row and y != col:
                    square.add((i, y))

    elif row>=0 and row<3 and col>=3 and col<6 :
        for i in range(0,3):
            for y in range(3, 6):
                if i != row and y != col:
                    square.add((i, y))                    

    elif row>=3 and row<6 and col>=3 and col<6 :
        for i in range(3,6):
            for y in range(3, 6):
                if i != row and y != col:
                    square.add((i, y)) 

    elif row>=6 and row<9 and col>=3 and col<6 :
        for i in range(6,9):
            for y in range(3, 6):
                if i != row and y != col:
                    square.add((i, y))

    elif row>=0 and row<3 and col>=6 and col<9 :
        for i in range(0,3):
            for y in range(6, 9):
                if i != row and y != col:
                    square.add((i, y))

    elif row>=3 and row<6  and col>=6 and col<9 :
        for i in range(3,6):
            for y in range(6, 9):
                if i != row and y != col:
                    square.add((i, y))

    elif row>=6 and row<9 and col>=6 and col<9 :
        for i in range(6,9):
            for y in range(6, 9):
                if i != row and y != col:
                    square.add((i, y))
    return square

# return the column constraints for a given node
def colconstraint(array, row, col):
    if row == 0:
        for i in range(1,9):
            array[row][col].constraints.add((i, col));
            
    if row == 1:
        for i in range(0,1):
            array[row][col].constraints.add((i, col));
        for i in range(2,9):
            array[row][col].constraints.add((i, col));
            
    if row == 2:
        for i in range(0,2):
            array[row][col].constraints.add((i, col));
        for i in range(3,9):
            array[row][col].constraints.add((i, col));
            
    if row == 3:
        for i in range(0,3):
            array[row][col].constraints.add((i, col));
        for i in range(4,9):
            array[row][col].constraints.add((i, col));
            
    if row == 4:
        for i in range(0,4):
            array[row][col].constraints.add((i, col));
        for i in range(5,9):
            array[row][col].constraints.add((i, col));
            
    if row == 5:
        for i in range(0,5):
            array[row][col].constraints.add((i, col));
        for i in range(6,9):
            array[row][col].constraints.add((i, col));
            
    if row == 6:
        for i in range(0,6):
            array[row][col].constraints.add((i, col));
        for i in range(7,9):
            array[row][col].constraints.add((i, col));
            
    if row == 7:
        for i in range(0,7):
            array[row][col].constraints.add((i, col));
        for i in range(8,9):
            array[row][col].constraints.add((i, col));
            
    if row == 8:
        for i in range(0,8):
            array[row][col].constraints.add((i, col));

# return the row constraints for a given node
def rowconstraint(array, row, col):
    if col == 0:
        for i in range(1,9):
            array[row][col].constraints.add((row, i));
            
    if col == 1:
        for i in range(0,1):
            array[row][col].constraints.add((row, i));
        for i in range(2,9):
            array[row][col].constraints.add((row, i));
            
    if col == 2:
        for i in range(0,2):
            array[row][col].constraints.add((row, i));
        for i in range(3,9):
            array[row][col].constraints.add((row, i));
            
    if col == 3:
        for i in range(0,3):
            array[row][col].constraints.add((row, i));
        for i in range(4,9):
            array[row][col].constraints.add((row, i));
            
    if col == 4:
        for i in range(0,4):
            array[row][col].constraints.add((row, i));
        for i in range(5,9):
            array[row][col].constraints.add((row, i));
            
    if col == 5:
        for i in range(0,5):
            array[row][col].constraints.add((row, i));
        for i in range(6,9):
            array[row][col].constraints.add((row, i));
            
    if col == 6:
        for i in range(0,6):
            array[row][col].constraints.add((row, i));
        for i in range(7,9):
            array[row][col].constraints.add((row, i));
            
    if col == 7:
        for i in range(0,7):
            array[row][col].constraints.add((row, i));
        for i in range(8,9):
            array[row][col].constraints.add((row, i));
            
    if col == 8:
        for i in range(0,8):
            array[row][col].constraints.add((row, i));

# adds all constraints to global list variable constraints
def cspconstraints(array, row, col):
    for i in array[row][col].constraints:
        constraints.append(((row, col) , i))

# checks to make sure value in current domain is not in constraint domain
def Revise(array, current, constraint):
    revised = False
    for x in current.domain:
        satisfied = False
        for y in constraint.domain:
            if x != y:
                satisfied = True
        if not satisfied:
            current.domain.remove(x)
            revised = True
    return revised

# checks to see if the puzzle is finished, all domains are 0 or 1
def complete(array):
    for i in range(0,len(array)):
        for y in range(0,len(array)):
            if len(array[i][y].domain) != 0 or len(array[i][y].domain) !=1:
                return False
    return True

# AC3 function
def AC3(array):
    arcs = deque()
    for x in constraints:
        arcs.appendleft(x)
    while arcs:
        constraintpair = arcs.pop()
        x, y = constraintpair[0][0], constraintpair[0][1]
        a, b = constraintpair[1][0], constraintpair[1][1]        
        node0 = array[x][y]
        node1 = array[a][b]
        if Revise(array, node0, node1):
            if len(node0.domain) == 0:
                return False
            for c in node0.constraints:
                arcs.appendleft((c, constraintpair[0]))
    return True

# return the length of the assignment
def lengthassignment(assignment):
    count = 0
    r = 0
    for row in assignment:
        r = r + 1
        for index in row:
            if index != ".":
                if index > 0 and index < 10:
                    count = count + 1
    return count

# select node with smallest domain and return the node and its location
def SelectUnassignedVariable(array, assignment):
    min = Node(None)
    min.domain = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(0,len(array)):
        for y in range(0,len(array)):
            if len(array[i][y].domain) < len(min.domain) and len(array[i][y].domain) > 1:
                        min = array[i][y]
                        min.domain = array[i][y].domain
                        tuple = (i, y)
    return min, tuple      

# sort domain values in order of increasing values and return
def OrderValues(array, var):
    var.domain.sort()
    return var.domain

# checks to see if length of domain is 0, if so return false, else return true
def domainlength(newarray):
    for i in range(0,len(newarray)):
        for y in range(0,len(newarray)):
            if len(newarray[i][y].domain) == 0:
                return False
    return True

# update assignment with the new values selected by backtracking and AC3
def updateassignment(array):
    assignment = []
    for i in range(0,len(array)):
        row = []
        assignment.append(row)
        for y in range(0,len(array)):
            if array[i][y].data == "." and len(array[i][y].domain) == 1:
                var = array[i][y].domain[0]
                row.append(var)
            else:
                if array[i][y].data != ".":
                    row.append(int(array[i][y].data))
                else:
                    row.append(array[i][y].data)
    return assignment

# backtracking search function
def BacktrackingSearch(array):
    assignment = updateassignment(array)
    if lengthassignment(assignment)==81:
        return assignment
    var, tuple = SelectUnassignedVariable(array, assignment)
    order = OrderValues(array, var)
    for value in order:
        assignment[tuple[0]][tuple[1]] = value
        array[tuple[0]][tuple[1]].domain = [value]
        newassignment = copy.deepcopy(assignment)
        newarray = copy.deepcopy(array)
        AC3(newarray)
        assignment = updateassignment(newarray)
        if domainlength(newarray):
            result = BacktrackingSearch(newarray)
            if result is not None:
                return result
    return None

# create domain for each node in the 2d array
def domain(array, row, col):
    for x, y in array[row][col].constraints:
        if array[x][y].data != ".": 
            if int(array[x][y].data) > 0 and int(array[x][y].data) < 10:
                if int(array[x][y].data) in array[row][col].domain:
                    array[row][col].domain.remove(int(array[x][y].data))

# creates class node and its attributes
class Node:
    def __init__(self, data):
        self.data = data
        self.constraints = set()
        self.domain = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# prompt user for input
x = input("Input a filename to solve puzzles: ")

# open file, for each line in file, append data to 2d array as nodes in their corresponding row
with open(x) as file:            
    for line in file.readlines():
        count = 0
        l = line.strip()
        for data in l:
            count = count + 1
            node = Node(data)
            row.append(node)
            if count%9==0:          
                array.append(row)
                row = []
                count = 0
        
        #Create the csp using the 2d array and initiate its values
        for i in range(0,len(array)):
            for y in range(0,len(array)):
                rowconstraint(array, i, y)
                colconstraint(array, i, y)
                possiblevals=return3x3squarevalues(array,i,y)
                array[i][y].constraints.update(possiblevals)
                cspconstraints(array, i, y)
                domain(array, i, y)
        
        # run AC3 and backtracking search on the 2d array
        AC3(array)
        back = BacktrackingSearch(array)
        
        # print sudoku puzzle
        for i in range(0,len(back)):
            for y in range(0,len(back)):
                print(back[i][y] , end="")
                
        array = []
        row = []
        constraints = []
        print()
        print()

                     