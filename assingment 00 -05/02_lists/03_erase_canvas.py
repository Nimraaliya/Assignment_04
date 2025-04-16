import tkinter as tk  # ✅ Import at the top

CELL_SIZE = 20
ROWS, COLS = 20, 30  # Grid dimensions
ERASER_SIZE = 40

class EraserCanvasApp:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=COLS*CELL_SIZE, height=ROWS*CELL_SIZE, bg='white')  # ✅ tk.Canvas
        self.canvas.pack()
        self.cells = {}  # Store references to cell rectangles
        
        self.draw_grid()
        self.create_eraser()

        self.canvas.bind("<B1-Motion>", self.move_eraser)
        self.canvas.bind("<Button-1>", self.move_eraser)

    def draw_grid(self):
        for row in range(ROWS):
            for col in range(COLS):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill='blue', outline='white')
                self.cells[rect] = (x1, y1, x2, y2)

    def create_eraser(self):
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, outline='black', width=2)

    def move_eraser(self, event):
        x1 = event.x - ERASER_SIZE // 2
        y1 = event.y - ERASER_SIZE // 2
        x2 = x1 + ERASER_SIZE
        y2 = y1 + ERASER_SIZE

        self.canvas.coords(self.eraser, x1, y1, x2, y2)

        # Erase any blue cells the eraser touches
        for rect_id, (rx1, ry1, rx2, ry2) in self.cells.items():
            if self._intersects(x1, y1, x2, y2, rx1, ry1, rx2, ry2):
                self.canvas.itemconfig(rect_id, fill='white')

    def _intersects(self, x1, y1, x2, y2, rx1, ry1, rx2, ry2):
        return not (x2 <= rx1 or x1 >= rx2 or y2 <= ry1 or y1 >= ry2)

def main():
    root = tk.Tk()
    root.title("Canvas Eraser Tool")
    app = EraserCanvasApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

