from n_queen_visualization import draw_multiple_solutions

def solve_n_queens(n):
    if n < 4:
        print('No possible solutions. Try n >= 4.')
        return
    marked = [False]*n
    left_diagonal = set()
    right_diagonal = set()
    solutions = []
    solution = [-1]*n

    def is_safe(row, col):
        if marked[col]:
            return False

        if row-col in left_diagonal or row+col in right_diagonal:
            return False

        return True



    def arrange_queens(row):
        nonlocal n, marked, left_diagonal, right_diagonal, solutions, solution
        if row == n:
            solutions.append(solution[:])
            return

        for i in range(n):
            if is_safe(row, i):
                solution[row] = i
                marked[i] = True
                left_diagonal.add(row-i)
                right_diagonal.add(row+i)

                arrange_queens(row+1)

                marked[i] = False
                solution[row] = -1
                left_diagonal.remove(row-i)
                right_diagonal.remove(row+i)

    arrange_queens(0)
    draw_multiple_solutions(n, solutions)
    print('That\'s it.')

def main():
    n = int(input('Enter the size of the chess board: '))
    solve_n_queens(n)

if __name__ == '__main__':
    main()



