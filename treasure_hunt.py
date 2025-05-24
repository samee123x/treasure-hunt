import random
from collections import deque

# Constants
GRID_SIZE = 5
EMPTY = "."
TREASURE = "T"
TRAP = "X"
OBSTACLE = "O"
POWER_UP = "P"
PLAYER_SYMBOLS = ["A", "B"]
STARTING_HEALTH = 5
MAX_HEALTH = 7

def create_empty_grid(size):
    return [[EMPTY for _ in range(size)] for _ in range(size)]

def place_items(grid, symbol, count):
    placed = 0
    while placed < count:
        r, c = random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)
        if grid[r][c] == EMPTY:
            grid[r][c] = symbol
            placed += 1

def print_grid(grid, players):
    for row in grid:
        print(" ".join(row))
    for p in players:
        print(f"Player {p['symbol']} Health: {p['health']}")
    print()

def find_player(grid, symbol):
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            if grid[r][c] == symbol:
                return (r, c)
    return (None, None)

def find_treasure(grid):
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            if grid[r][c] == TREASURE:
                return (r, c)
    return None

def binary_search_grid(grid, index, axis='row'):
    def bs_helper(arr, low, high):
        if low > high:
            return False
        mid = (low + high) // 2
        if arr[mid] in (TREASURE, POWER_UP):
            return True
        return bs_helper(arr, low, mid-1) or bs_helper(arr, mid+1, high)

    if axis == 'row':
        return bs_helper(grid[index], 0, GRID_SIZE-1)
    else:
        col = [grid[r][index] for r in range(GRID_SIZE)]
        return bs_helper(col, 0, GRID_SIZE-1)

def bfs(grid, start, target):
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        (r, c), path = queue.popleft()
        if (r, c) == target:
            return path
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < GRID_SIZE and 0 <= nc < GRID_SIZE:
                if grid[nr][nc] != OBSTACLE and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    queue.append(((nr,nc), path+[(nr,nc)]))
    return []

def dfs(grid, current, target, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    if current == target:
        return path + [current]
    visited.add(current)
    r, c = current
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr, nc = r+dr, c+dc
        if 0 <= nr < GRID_SIZE and 0 <= nc < GRID_SIZE:
            if grid[nr][nc] != OBSTACLE and (nr,nc) not in visited:
                result = dfs(grid, (nr,nc), target, visited, path+[current])
                if result:
                    return result
    return []

def give_hint(pos):
    if not pos:
        return "No treasure on the grid."
    r, c = pos
    if random.choice([True, False]):
        return f"Hint: treasure in row {r+1}."
    else:
        return f"Hint: treasure in column {c+1}."

def move_player(grid, player, direction, players):
    row, col = find_player(grid, player['symbol'])
    if row is None:
        return player['health'], False

    dr = dc = 0
    if direction=="up":    dr=-1
    elif direction=="down": dr=1
    elif direction=="left": dc=-1
    elif direction=="right":dc=1
    else:
        print("Invalid direction.")
        return player['health'], False

    nr, nc = row+dr, col+dc
    if not (0<=nr<GRID_SIZE and 0<=nc<GRID_SIZE):
        print("Cannot move outside the grid.")
        return player['health'], False
    if grid[nr][nc]==OBSTACLE:
        print("Obstacle in the way.")
        return player['health'], False
    for o in players:
        if o!=player and find_player(grid,o['symbol'])==(nr,nc):
            print("Another player is there.")
            return player['health'], False

    cell = grid[nr][nc]
    grid[row][col]=EMPTY
    grid[nr][nc]=player['symbol']

    if cell==TREASURE:
        print(f"Player {player['symbol']} found the treasure. Game over.")
        return player['health'], True
    if cell==TRAP:
        player['health']-=1
        print(f"Player {player['symbol']} stepped on a trap. Health: {player['health']}")
        if player['health']<=0:
            print(f"Player {player['symbol']} eliminated.")
            grid[nr][nc]=EMPTY
            return player['health'], True
    if cell==POWER_UP:
        if random.choice([True, False]):
            gain = min(MAX_HEALTH-player['health'], 2)
            player['health']+=gain
            print(f"Player {player['symbol']} gained {gain} health.")
        else:
            print(f"Player {player['symbol']} got a hint. {give_hint(find_treasure(grid))}")

    return player['health'], False

def player_turn(grid, player, players):
    print(f"Player {player['symbol']}'s turn ({player['health']} HP).")
    cmd = input("Command: ").strip().lower().split()
    if not cmd:
        return False, False

    if cmd[0]=="move" and len(cmd)==2:
        h, over = move_player(grid, player, cmd[1], players)
        player['health']=h
        return True, over
    if cmd[0]=="bs" and len(cmd)==3:
        idx = int(cmd[2])-1
        found = binary_search_grid(grid, idx, cmd[1])
        print("Binary search:", "found" if found else "not found")
        return True, False
    if cmd[0]=="bfs":
        path = bfs(grid, find_player(grid,player['symbol']), find_treasure(grid))
        print("BFS path:", " -> ".join(f"({r+1},{c+1})" for r,c in path) or "none")
        return True, False
    if cmd[0]=="dfs":
        path = dfs(grid, find_player(grid,player['symbol']), find_treasure(grid))
        print("DFS path:", " -> ".join(f"({r+1},{c+1})" for r,c in path) or "none")
        return True, False

    print("Invalid command.")
    return False, False

def setup_game():
    grid = create_empty_grid(GRID_SIZE)
    place_items(grid, TREASURE, 1)
    place_items(grid, TRAP, 3)
    place_items(grid, OBSTACLE, 3)
    place_items(grid, POWER_UP, 2)
    players=[]
    for sym in PLAYER_SYMBOLS:
        while True:
            r,c = random.randint(0,GRID_SIZE-1), random.randint(0,GRID_SIZE-1)
            if grid[r][c]==EMPTY:
                grid[r][c]=sym
                players.append({'symbol':sym,'health':STARTING_HEALTH})
                break
    return grid, players

def play_game():
    grid, players = setup_game()
    print("Welcome to Treasure Hunt")
    print_grid(grid, players)
    turn=0
    while True:
        p=players[turn]
        if p['health']>0:
            moved, over = player_turn(grid, p, players)
            print_grid(grid, players)
            if over:
                return
            if moved:
                turn=(turn+1)%len(players)
        else:
            turn=(turn+1)%len(players)

if __name__=="__main__":
    play_game()
