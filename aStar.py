import heapq
import math
import tkinter as tk
import time

rows = 20
colums = 20
tam = 20
delay = 200

#distância Euclidiana
def heuristic(node, goal):
    return math.sqrt((node[0] - goal[0])**2 + (node[1] - goal[1])**2)

#encontrar os vizinhos
def neighbors(node):
    neighbors = []
    row, col = node

    for i in range(-1, 2):
        for j in range(-1, 2):
            new_row, new_col = row + i, col + j
            if 0 <= new_row < rows and 0 <= new_col < colums:
                neighbors.append((new_row, new_col))

    neighbors.remove((row, col))
    return neighbors

def aStar(start, goal, grid):
    open_set = []
    closed_set = set()

    heapq.heappush(open_set, (0, start))
    came_from = {}

    g_score = {(i, j): float('inf') for i in range(rows) for j in range(colums)}
    g_score[start] = 0

    f_score = {(i, j): float('inf') for i in range(rows) for j in range(colums)}
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

        for neighbor in neighbors(current):
            if neighbor in closed_set or grid[neighbor[0]][neighbor[1]] == '#':
                continue

            tentative_g_score = g_score[current] + (1.0 if abs(neighbor[0]-current[0])==1 and abs(neighbor[1]-current[1])==1 else math.sqrt(2))

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                if neighbor not in open_set:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None

#adicionar ou remover paredes
def addWall(event):
    x, y = event.x // tam, event.y // tam
    if 0 <= x < colums and 0 <= y < rows:
        if grid[y][x] == '#':
            grid[y][x] = '.'
            canvas.itemconfig(rectangles[y][x], fill='white')
        else:
            grid[y][x] = '#'
            canvas.itemconfig(rectangles[y][x], fill='black')

def startSearch():
    global start, end
    if start_set and end_set:
        path = aStar(start, end, grid)
        if path:
            draw(path)
        else:
            print("Não foi possível encontrar um caminho.")
    else:
        print("Defina a posição de partida e chegada antes de encontrar o caminho.")

def draw(path):
    for node in path:
        row, col = node
        if grid[row][col] != 'S' and grid[row][col] != 'C':
            grid[row][col] = '*'
            canvas.itemconfig(rectangles[row][col], fill='blue')
            canvas.create_text((col + 0.5) * tam, (row + 0.5) * tam, text=f'({col}, {row})', fill='white')
            canvas.update()
            time.sleep(delay / 1000)

def positions(event):
    global start, end, start_set, end_set
    x, y = event.x // tam, event.y // tam # mouse
    if 0 <= x < colums and 0 <= y < rows:
        if grid[y][x] == 'S':
            start = None
            start_set = False
            grid[y][x] = '.'
            canvas.itemconfig(rectangles[y][x], fill='white')
        elif grid[y][x] == 'C':
            end = None
            end_set = False
            grid[y][x] = '.'
            canvas.itemconfig(rectangles[y][x], fill='white')
        else:
            if not start_set:
                start = (y, x)
                grid[y][x] = 'S'
                canvas.itemconfig(rectangles[y][x], fill='green')
                start_set = True
            elif not end_set:
                end = (y, x)
                grid[y][x] = 'C'
                canvas.itemconfig(rectangles[y][x], fill='red')
                end_set = True

def clearAll():
    global start, end, start_set, end_set
    start = None
    end = None
    start_set = False
    end_set = False
    for i in range(rows):
        for j in range(colums):
            grid[i][j] = '.'
            canvas.itemconfig(rectangles[i][j], fill='white')

start = None
end = None
start_set = False
end_set = False

#criar matriz
grid = [['.' for _ in range(colums)] for _ in range(rows)]

#interface
root = tk.Tk()
root.title("Desafio A*")

#canvas
canvas = tk.Canvas(root, width=colums * tam, height=rows * tam)
canvas.pack()

rectangles = []
for i in range(rows):
    row_rectangles = []
    for j in range(colums):
        rect = canvas.create_rectangle(j * tam, i * tam, (j + 1) * tam, (i + 1) * tam, fill='white')
        row_rectangles.append(rect)
    rectangles.append(row_rectangles)

canvas.bind("<Button-1>", addWall)
canvas.bind("<Button-3>", positions)

start_search_button = tk.Button(root, text="Iniciar Busca Passo a Passo", command=startSearch)
start_search_button.pack()

clear_button = tk.Button(root, text="Limpar Tudo", command=clearAll)
clear_button.pack()

root.mainloop()