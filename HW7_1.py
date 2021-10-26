#решение 1 (работает плохо, при выводе матрицы в методе __add__ запускает init, запрашивает новую матрицу, выводит новую
# (запрошенную) и суммарную матрицу, пыталась выводить просто sum_matrix, но тогда он не выводит в виде строки
# а выводит в виде списка списков (это и понятно, sum_matrix в таком случае не является объектом классам Matrix
# как это исправить, не знаю)
class Matrix:

    def __init__(self, columns, lines, mtr):
        self.mtr = mtr
        self.columns = columns
        self.lines = lines
        for self.i in range(self.lines):
            self.list1 = []
            for self.j in range(self.columns):
                self.list1.append(int(input()))
            self.mtr.append(self.list1)

    def __str__(self):
        return '\n'.join('\t'.join(str(number) for number in line) for line in self.mtr)

    def __add__(self, other):
        sum_matrix = []
        for k in range(len(self.mtr)):
            list_sum = []
            for m in range(len(self.mtr[0])):
                sum_numbers = int(other.mtr[k][m]) + int(self.mtr[k][m])
                list_sum.append(sum_numbers)
            sum_matrix.append(list_sum)
        return sum_matrix


matrix_data1 = Matrix(2, 2, [])
matrix_data2 = Matrix(2, 2, [])
print(matrix_data1)
print(matrix_data2)
print(matrix_data1 + matrix_data2)


#решение 2 (работает нормально, вроде)

class Matrix:

    def __init__(self, mtr):
        self.mtr = mtr

    def __str__(self):
        return '\n'.join('\t'.join(str(number) for number in line) for line in self.mtr)

    def __add__(self, other):
        sum_matrix = []
        for k in range(len(self.mtr)):
            list_sum = []
            for m in range(len(self.mtr[0])):
                sum_numbers = int(other.mtr[k][m]) + int(self.mtr[k][m])
                list_sum.append(sum_numbers)
            sum_matrix.append(list_sum)
        return Matrix(sum_matrix)


matrix_data1 = Matrix([[1, 2], [3, 4]])
matrix_data2 = Matrix([[1, 2], [3, 4]])
print(matrix_data1)
print(matrix_data2)
print(matrix_data1 + matrix_data2)
