import tkinter as tk

def draw_multiple_solutions(n, solutions):
    root = tk.Tk()
    root.title(f"All Solutions for N={n}")

    # Create a scrollable frame for large numbers of solutions
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=1)

    canvas = tk.Canvas(main_frame)
    scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    scroll_frame = tk.Frame(canvas)
    scroll_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    # Adjust board size for each small chessboard
    cell_size = min(400 // n, 50)  # Smaller size for multiple boards

    for idx, solution in enumerate(solutions):
        # Create a frame for each board and display it in a grid
        frame = tk.Frame(scroll_frame, padx=5, pady=5)
        frame.grid(row=idx // 3, column=idx % 3, padx=10, pady=10)  # 3 boards per row

        canvas_board = tk.Canvas(frame, width=n * cell_size, height=n * cell_size)
        canvas_board.pack()

        # Draw the chessboard
        for row in range(n):
            for col in range(n):
                color = "white" if (row + col) % 2 == 0 else "black"
                canvas_board.create_rectangle(col * cell_size, row * cell_size,
                                              (col + 1) * cell_size, (row + 1) * cell_size,
                                              fill=color)

        # Draw the queens for the current solution
        for row in range(n):
            col = solution[row]
            canvas_board.create_text((col + 0.5) * cell_size, (row + 0.5) * cell_size,
                                     text='♛', font=('Arial', int(cell_size * 0.6)), fill='red')

    root.mainloop()


