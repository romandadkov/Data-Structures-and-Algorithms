# python3

EPS = 1e-6
PRECISION = 20

class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row

def ReadEquation():
    size = int(input())
    a = []
    b = []
    for row in range(size):
        line = list(map(float, input().split()))
        a.append(line[:size])
        b.append(line[size])
    return Equation(a, b)

def SelectPivotElement(a, used_rows, used_columns):
    # 1st, select the first free element
    pivot_element = Position(0, 0)
    while used_rows[pivot_element.row]:
        pivot_element.row += 1
    while used_columns[pivot_element.column]:
        pivot_element.column += 1

    # 2nd, amongs free elements, select a pivot with the largest absolute value
    start = pivot_element.row
    max_element = a[start][pivot_element.column]
    for i in range(start, len(a)):
        if abs(a[i][pivot_element.column]) > abs(max_element):
            max_element = a[i][pivot_element.column]
            pivot_element.row = i

    return pivot_element

def SwapLines(a, b, used_rows, pivot_element):
    a[pivot_element.column], a[pivot_element.row] = a[pivot_element.row], a[pivot_element.column]
    b[pivot_element.column], b[pivot_element.row] = b[pivot_element.row], b[pivot_element.column]
    used_rows[pivot_element.column], used_rows[pivot_element.row] = used_rows[pivot_element.row], used_rows[pivot_element.column]
    pivot_element.row = pivot_element.column;

def ScalePivot(a, b, pivot_element):
    # const double divisor = a[pivot_element.row][pivot_element.column];
    # const int size = a.size();

    # for (int j = pivot_element.column; j < size; ++j) {
    #     a[pivot_element.row][j] /= divisor;
    # }

    # b[pivot_element.row] /= divisor;

    divisor = a[pivot_element.row][pivot_element.column]
    for j in range(pivot_element.column, len(a)):
        a[pivot_element.row][j] /= divisor;

    b[pivot_element.row] /= divisor;

def ProcessPivotElement(a, b, pivot_element):
    # const int size = a.size();
    # double multiple{ 0.0 };

    # scale_pivot(a, b, pivot_element);

    # for (int i = pivot_element.row + 1; i < size; ++i) {
    #     multiple = a[i][pivot_element.column];
    #     for (int j = pivot_element.column; j < size; ++j) {
    #         a[i][j] -= (a[pivot_element.row][j] * multiple);
    #     }
    #     b[i] -= (b[pivot_element.row] * multiple);
    # }
    ScalePivot(a, b, pivot_element)
    #start = pivot_element.row + 1
    for i in range(len(a)):
        if i == pivot_element.row:
            continue
        multiple = a[i][pivot_element.column]
        for j in range(pivot_element.column, len(a)):
            a[i][j] -= (a[pivot_element.row][j] * multiple)
        b[i] -= (b[pivot_element.row] * multiple);


def MarkPivotElementUsed(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True

def SolveEquation(equation):
    a = equation.a
    b = equation.b
    size = len(a)
    used_columns = [False] * size
    used_rows = [False] * size
    for step in range(size):
        pivot_element = SelectPivotElement(a, used_rows, used_columns)
        SwapLines(a, b, used_rows, pivot_element)
        ProcessPivotElement(a, b, pivot_element)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)

    return b

def PrintColumn(column):
    size = len(column)
    for row in range(size):
        print("%.20lf" % column[row])

if __name__ == "__main__":
    equation = ReadEquation()
    solution = SolveEquation(equation)
    PrintColumn(solution)
    exit(0)

    # size = 4
    # a = [[1, 0, 0, 0],
    #     [0, 1, 0, 0],
    #     [0, 0, 1, 0],
    #     [0, 0, 0, 1]]
    # b = [1,5,4,3]

    # size = 2
    # a = [[1, 1],
    #     [2, 3]]
    # b = [3, 7]