import heapq

def manhattan_distance(state, goal_state):
    distance = 0
    for i in range(9):
        val = state[i]
        if val != 0:
            goal_idx = goal_state.index(val)
            curr_r, curr_c = divmod(i, 3)
            goal_r, goal_c = divmod(goal_idx, 3)
            distance += abs(curr_r - goal_r) + abs(curr_c - goal_c)
    return distance

def get_neighbors(state):
    neighbors = []
    zero_idx = state.index(0)
    r, c = divmod(zero_idx, 3)
    
    # Possible movements for the empty tile (0): up, down, left, right
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            n_idx = nr * 3 + nc
            new_state = list(state)
            new_state[zero_idx], new_state[n_idx] = new_state[n_idx], new_state[zero_idx]
            neighbors.append(tuple(new_state))
            
    return neighbors

def solve_8_puzzle(start_state, goal_state=(1,2,3,8,0,4,7,6,5)):
    # Priority queue stores tuples: (f_score, g_score, state, path)
    open_list = []
    h_init = manhattan_distance(start_state, goal_state)
    heapq.heappush(open_list, (h_init, 0, start_state, [start_state]))
    
    g_scores = {start_state: 0}
    closed_set = set()
    
    while open_list:
        f, g, current, path = heapq.heappop(open_list)
        
        if current == goal_state:
            return path
            
        if current in closed_set:
            continue
        closed_set.add(current)
        
        for neighbor in get_neighbors(current):
            if neighbor in closed_set:
                continue
                
            tentative_g = g + 1
            if tentative_g < g_scores.get(neighbor, float('inf')):
                g_scores[neighbor] = tentative_g
                f_score = tentative_g + manhattan_distance(neighbor, goal_state)
                heapq.heappush(open_list, (f_score, tentative_g, neighbor, path + [neighbor]))
                
    return None

# Example initial state (0 represents the blank space)
# Solvable configuration:
initial_board =  (2,8,3,
                  1,6,4,
                  0,7,5)

solution_path = solve_8_puzzle(initial_board)

if solution_path:
    print(f"Total steps to solve: {len(solution_path) - 1}")
    for step, board in enumerate(solution_path):
        print(f"Step {step}:")
        print(board[0:3])
        print(board[3:6])
        print(board[6:9])
        print()
else:
    print("No solution found.")