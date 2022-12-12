'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    15 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    #check if both users follow each other
    if (to_member in social_graph[from_member]['following'] and 
        from_member in social_graph[to_member]['following']):
        return 'friends'
    #check if fromMember follows toMember 
    elif to_member in social_graph[from_member]['following']:
        return 'follower'
    #check if fromMember is followed by toMember 
    elif from_member in social_graph[to_member]['following']:
        return 'followed by'
    #output "no relationship" if neither fromMember or toMember follow each other
    else:
        return 'no relationship'



def tic_tac_toe(board):
    '''Tic Tac Toe. 
    15 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------A
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    #get the size of the board using the len function
    size = len(board)

    # Check rows, columns, and diagonals for a winner
    for i in range(size):
        if all(board[i][j] == board[i][0] for j in range(size)) or \
           all(board[i][j] == board[0][j] for j in range(size)) or \
           all(board[i][i] == board[0][0] for i in range(size)) or \
           all(board[i][size - i - 1] == board[0][size - 1] for i in range(size)):
            return board[i][0]

    # If no winner was found, return "NO WINNER"
    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    20 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see the sample data file in this same folder for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
        
    newkeys = list(route_map.keys())
    firstkeys = [item[0] for item in newkeys]
    secondkeys = [item[1] for item in newkeys]
    newtime = list(route_map.values())
    answer = []
    final = []

# Check if first_stop is in firstkeys
    if first_stop in firstkeys:
    # Get the position of first_stop in firstkeys
        firstposition = firstkeys.index(first_stop)
    else:
    # Return 0 if first_stop is not in firstkeys
        return 0

# Check if second_stop is in secondkeys
    if second_stop in secondkeys:
    # Get the position of second_stop in secondkeys
        secondposition = secondkeys.index(second_stop)
    else:
    # Return 0 if second_stop is not in secondkeys
        return 0
    
    firstposition=firstkeys.index(first_stop)
    secondposition=secondkeys.index(second_stop)
        
    for x in range(len(newtime)):
            answer=answer+list(newtime[x].values())
    
    if first_stop==second_stop:
        return sum(answer)
    elif firstposition==secondposition:
        return answer[firstposition]
    elif firstposition<secondposition:
        final=answer[firstposition:secondposition+1]
        return sum(final)
    elif firstposition>secondposition:
        final=answer[firstposition:]+answer[:secondposition+1]
        return sum(final)


