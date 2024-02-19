ACCEPT = 1
CONTINUE = 2
ABANDON = 3


class NQueenProblem:
    """
    Implementation of the N Queens problem
    """

    def __init__(self, columns="abcd"):
        self.columns = columns
        self.n_queens = len(self.columns)

    def extend(self, partial_solution):
        """
        Take a partial solution and make different copies.
        Each copy gets a new queen in a different column.
        """
        results = []
        row = len(partial_solution) + 1

        for column in self.columns:
            new_solution = list(partial_solution)
            new_solution.append(column + str(row))
            results.append(new_solution)

        return results

    def examine(self, partial_solution):
        """
        Check whether two queens in a partial solution can attack
        each other or not.
        """
        for i in range(len(partial_solution)):
            for j in range(i + 1, len(partial_solution)):
                if self.attacks(partial_solution[i], partial_solution[j]):
                    return ABANDON

        if len(partial_solution) == self.n_queens:
            return ACCEPT
        else:
            return CONTINUE

    def attacks(self, p1, p2):
        """
        Check if two queens can attack each other.

        Cannot be on:
        - The same row
        - The same column
        - The same diagonal
        """
        column1 = self.columns.index(p1[0]) + 1
        row1 = int(p1[1])

        column2 = self.columns.index(p2[0]) + 1
        row2 = int(p2[1])

        return (
            row1 == row2
            or column1 == column2
            or abs(row1 - row2) == abs(column1 - column2)
        )

    def solve(self, partial_solution=[]):
        """
        Solves the N Queen problem given an initial state.
        empty list is an empty board.
        """
        exam = self.examine(partial_solution)

        if exam == ACCEPT:
            print(partial_solution)
        elif exam != ABANDON:
            for p in self.extend(partial_solution):
                self.solve(p)



if __name__ == "__main__":
    n_queens = NQueenProblem("abcdefgh")

    n_queens.solve([])
