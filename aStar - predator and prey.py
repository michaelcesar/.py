import heapq
import math
import tkinter as tk
import time
from tkinter import Button

#dimensões da matriz
ROW_COUNT = 20
COL_COUNT = 20
CELL_SIZE = 20  #células
ANIMATION_DELAY = 100  #velocidade

#heurística (distância Euclidiana)
def heuristic(node, goal):
    return math.sqrt((node[0] - goal[0])**2 + (node[1] - goal[1])**2)

#encontrar todos os vizinhos, incluindo diagonais
def get_neighbors(node):
    neighbors = []
    row, col = node

    for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_row, new_col = row + i, col + j
        if 0 <= new_row < ROW_COUNT and 0 <= new_col < COL_COUNT:
            neighbors.append((new_row, new_col))

    return neighbors

#astar inverso
def astar_inverso_maior_distancia(start, grid, goal):
    open_set = []
    closed_set = set()

    heapq.heappush(open_set, (0, start))
    came_from = {}

    g_score = {(i, j): float('-inf') for i in range(ROW_COUNT) for j in range(COL_COUNT)}
    g_score[start] = 0

    f_score = {(i, j): float('-inf') for i in range(ROW_COUNT) for j in range(COL_COUNT)}
    
    if goal is not None:
        f_score[start] = -heuristic(start, goal)  # negativo para inverter

    while open_set:
        _, current = heapq.heappop(open_set)

        closed_set.add(current)

        for neighbor in get_neighbors(current):
            if neighbor in closed_set or grid[neighbor[0]][neighbor[1]] == '#':
                continue

            #calcular custo
            if neighbor[0] == current[0] or neighbor[1] == current[1]:
                cost = 1.0  #vertical ou horizontal
            else:
                cost = math.sqrt(2.0)  #diagonal

            tentative_g_score = g_score[current] + cost

            if tentative_g_score > g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                if goal is not None:
                    f_score[neighbor] = -heuristic(neighbor, goal)  #negativo para inverter a busca
                if neighbor not in open_set:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    #pegando ponto mais distante
    max_distance_node = max(g_score, key=g_score.get)

    #recriando caminho até o ponto mais distante
    path = []
    current = max_distance_node
    while current != start:
        path.append(current)
        current = came_from[current]
    path.reverse()

    return path



#A*
def astar(start, goal, grid):
    open_set = []
    closed_set = set()

    heapq.heappush(open_set, (0, start))
    came_from = {}

    g_score = {(i, j): float('inf') for i in range(ROW_COUNT) for j in range(COL_COUNT)}
    g_score[start] = 0

    f_score = {(i, j): float('inf') for i in range(ROW_COUNT) for j in range(COL_COUNT)}
    f_score[start] = heuristic(start, goal)

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        closed_set.add(current)

        for neighbor in get_neighbors(current):
            if neighbor in closed_set or grid[neighbor[0]][neighbor[1]] == '#':
                continue

            #calcular o custo
            if neighbor[0] == current[0] or neighbor[1] == current[1]:
                cost = 1.0  #vertical ou horizontal
            #else:
                #cost = math.sqrt(2.0)  #diagonal

            tentative_g_score = g_score[current] + cost

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                if neighbor not in open_set:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None

#criar e remover paredes
def toggle_wall(event):
    x, y = event.x // CELL_SIZE, event.y // CELL_SIZE  #coordenadas do mouse em coordenadas da matriz
    if 0 <= x < COL_COUNT and 0 <= y < ROW_COUNT:
        if grid[y][x] == '#':
            grid[y][x] = '.'
            canvas.itemconfig(rectangles[y][x], fill='white')
        else:
            grid[y][x] = '#'
            canvas.itemconfig(rectangles[y][x], fill='black')

#iniciar a busca passo a passo
def start_search_step_by_step():
    global start, goal
    if start_set and goal_set:
        path = astar(start, goal, grid)
        if path:
            draw_path(path)
        else:
            print("Não foi possível encontrar um caminho.")
    else:
        print("Defina a posição de partida e chegada antes de encontrar o caminho.")

#desenhar o caminho na interface
def draw_path(path):
    for node in path:
        row, col = node
        if grid[row][col] != 'S' and grid[row][col] != 'C':
            grid[row][col] = '*'
            canvas.itemconfig(rectangles[row][col], fill='blue')
            canvas.create_text((col + 0.5) * CELL_SIZE, (row + 0.5) * CELL_SIZE, text=f'({col}, {row})', fill='white')
            canvas.update()
            time.sleep(ANIMATION_DELAY / 1000)

#posição de partida e chegada
def set_start_or_goal(event):
    global start, goal, start_set, goal_set
    x, y = event.x // CELL_SIZE, event.y // CELL_SIZE  
    if 0 <= x < COL_COUNT and 0 <= y < ROW_COUNT:
        if grid[y][x] == 'S':
            start = None
            start_set = False
            grid[y][x] = '.'
            canvas.itemconfig(rectangles[y][x], fill='white')
        elif grid[y][x] == 'C':
            goal = None
            goal_set = False
            grid[y][x] = '.'
            canvas.itemconfig(rectangles[y][x], fill='white')
        else:
            if not start_set:
                start = (y, x)
                grid[y][x] = 'S'
                canvas.itemconfig(rectangles[y][x], fill='green')
                start_set = True
            elif not goal_set:
                goal = (y, x)
                grid[y][x] = 'C'
                canvas.itemconfig(rectangles[y][x], fill='red')
                goal_set = True

def set_caçador_start(event):
    global caçador, caçador_start
    x, y = event.x // CELL_SIZE, event.y // CELL_SIZE  
    if 0 <= x < COL_COUNT and 0 <= y < ROW_COUNT:
        caçador_start = (y, x)
        if not caçador:
            caçador = caçador_start
        else:
            grid[caçador[0]][caçador[1]] = '.'
            canvas.itemconfig(rectangles[caçador[0]][caçador[1]], fill='white')
        grid[y][x] = 'C'
        canvas.itemconfig(rectangles[y][x], fill='orange')
        caçador = caçador_start

def set_presa_start(event):
    global presa, presa_start
    x, y = event.x // CELL_SIZE, event.y // CELL_SIZE  
    if 0 <= x < COL_COUNT and 0 <= y < ROW_COUNT:
        presa_start = (y, x)
        if not presa:
            presa = presa_start
        else:
            grid[presa[0]][presa[1]] = '.'
            canvas.itemconfig(rectangles[presa[0]][presa[1]], fill='white')
        grid[y][x] = 'P'
        canvas.itemconfig(rectangles[y][x], fill='yellow')
        presa = presa_start

def mover_presa():
    global presa, caçador, goal

    if presa and caçador:
        path = astar_inverso_maior_distancia(tuple(presa), grid, caçador)

        if path and len(path) > 1:

            next_position = list(path[1])

            if grid[next_position[0]][next_position[1]] == '.':
              
                grid[presa[0]][presa[1]] = '.'
                canvas.itemconfig(rectangles[presa[0]][presa[1]], fill='white')

                presa = next_position
                grid[presa[0]][presa[1]] = 'P'
                canvas.itemconfig(rectangles[presa[0]][presa[1]], fill='yellow')

        if presa == caçador:
            print("O caçador alcançou a presa!")


#movimento
def simulate_movement():
    mover_presa()
    mover_caçador()

    if caçador == presa:
        print("O caçador alcançou a presa!")
        return 

    root.after(1000, simulate_movement)


def mover_caçador():
    global caçador
    if caçador and presa:
        path = astar(tuple(caçador), tuple(presa), grid)  #tuplas
        if path and len(path) > 2:
            #refresh da posição do caçador para seguir o caminho em direção para a presa
            caçador = list(path[2])  #andar dois quadrados por vez
            grid[caçador[0]][caçador[1]] = 'C'
            canvas.itemconfig(rectangles[caçador[0]][caçador[1]], fill='orange')

def clear_all():
    global start, goal, start_set, goal_set, caçador_start, presa_start, caçador, presa
    start = None
    goal = None
    start_set = False
    goal_set = False
    caçador_start = None
    presa_start = None
    if caçador:
        grid[caçador[0]][caçador[1]] = '.'
        canvas.itemconfig(rectangles[caçador[0]][caçador[1]], fill='white')
    if presa:
        grid[presa[0]][presa[1]] = '.'
        canvas.itemconfig(rectangles[presa[0]][presa[1]], fill='white')
    caçador = None
    presa = None
    for i in range(ROW_COUNT):
        for j in range(COL_COUNT):
            grid[i][j] = '.'
            canvas.itemconfig(rectangles[i][j], fill='white')

start = None
goal = None
start_set = False
goal_set = False

#caçador e a presa
caçador = None
presa = None

#mouse
caçador_start = None
presa_start = None

#matriz vazia
grid = [['.' for _ in range(COL_COUNT)] for _ in range(ROW_COUNT)]

#janela
root = tk.Tk()
root.title("Caçador e Presa 4")

#exibir a matriz
canvas = tk.Canvas(root, width=COL_COUNT * CELL_SIZE, height=ROW_COUNT * CELL_SIZE)
canvas.pack()

rectangles = []
for i in range(ROW_COUNT):
    row_rectangles = []
    for j in range(COL_COUNT):
        rect = canvas.create_rectangle(j * CELL_SIZE, i * CELL_SIZE, (j + 1) * CELL_SIZE, (i + 1) * CELL_SIZE, fill='white')
        row_rectangles.append(rect)
    rectangles.append(row_rectangles)


canvas.bind("<Button-1>", toggle_wall)  #esquerdo para paredas
canvas.bind("<Button-3>", set_start_or_goal)  #direito para caçador e presa

canvas.bind("<Double-Button-1>", set_caçador_start) 
canvas.bind("<Button-3>", set_presa_start) 

clear_button = tk.Button(root, text="Limpar Tudo", command=clear_all)
clear_button.pack()

iniciar_caca_button = Button(root, text="Iniciar Caça", command=simulate_movement)
iniciar_caca_button.pack()

#interface gráfica
root.mainloop()