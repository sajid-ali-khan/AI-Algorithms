import tkinter as tk

def draw_chessboard_with_queens(n, solution):
    root = tk.Tk()
    root.title(f"N-Queens Solution for N={n}")

    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()

    cell_size = 400 // n

    # Draw the chessboard
    for row in range(n):
        for col in range(n):
            color = "white" if (row + col) % 2 == 0 else "black"
            canvas.create_rectangle(col * cell_size, row * cell_size,
                                    (col + 1) * cell_size, (row + 1) * cell_size,
                                    fill=color)

    # Draw queens
    for row in range(n):
        col = solution[row]
        canvas.create_text((col + 0.5) * cell_size, (row + 0.5) * cell_size,
                           text='♛', font=('Arial', int(cell_size * 0.4)), fill='red')

    root.mainloop()

# Example usage
if __name__ == "__main__":
    n = 4  # Size of the chessboard (4x4)
    solution = [1, 3, 0, 2]  # A sample solution for N=4
    draw_chessboard_with_queens(n, solution)
