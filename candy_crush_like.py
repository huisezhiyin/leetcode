import random


class Borad(object):

    def check_board(self, board):
        # 检查器
        for row in board:
            if self.check_list(row):
                return False
        for i in range(len(board[0])):
            col = [row[i] for row in board]
            if self.check_list(col):
                return False
        return True

    @staticmethod
    def check_list(lst):
        # 行列检查器
        return any(lst[i] == lst[i + 1] and lst[i] == lst[i + 2] for i in range(len(lst) - 2))

    def init_board(self):
        board = [[] for x in range(9)]
        board[0] = self.one_dimensional_array()
        board[1] = self.one_dimensional_array()
        for count_index_col in range(2, 9):
            # 初始化
            board[count_index_col] = [None for x in range(9)]
            for count_index_row in range(9):
                board[count_index_col][count_index_row] = self.one_num(board, count_index_col, count_index_row)
        return board

    @staticmethod
    def one_num(board, col, row):
        # col: > 1 row: 0-8
        # 一个个按顺序的生成数字
        tmp_list = [1, 2, 3, 4]
        if col <= 1:
            raise Exception("error")
        # 此数字竖向不能有三连
        if board[col - 1][row] == board[col - 2][row]:
            tmp_list.remove(board[col - 1][row])
        if row > 1:
            # 横向上如果此数字前面超过两个数字 那横向不能有三辆
            if (board[col][row - 1] == board[col][row - 2]) and (board[col][row - 1] in tmp_list):
                tmp_list.remove(board[col][row - 1])
        return random.choice(tmp_list)

    @staticmethod
    def one_dimensional_array():
        # 生成合法的随机一维数组
        array = [None for x in range(9)]
        array[0] = random.choice([1, 2, 3, 4])
        array[1] = random.choice([1, 2, 3, 4])
        for index_count in range(2, 9):
            tmp_num = random.choice([1, 2, 3, 4])
            if tmp_num == array[index_count - 1] and tmp_num == array[index_count - 2]:
                tmp_list = [1, 2, 3, 4]
                tmp_list.remove(tmp_num)
                tmp_num = random.choice(tmp_list)
            array[index_count] = tmp_num
        return array


if __name__ == '__main__':
    a = Borad()
    t = a.init_board()
    if a.check_board(t):
        print("success")
