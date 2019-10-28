from collections import deque
import numpy as np
import pickle

class Pattern_generater():
    def __init__(self, A_pattern, B_pattern, C_pattern): # 가능하면 최대 패턴 입력 갯수 수정하기
        self.__A_pattern = A_pattern
        self.__B_pattern = B_pattern
        self.__C_pattern = C_pattern

    def generate_bfs(self, init_pattern):
        pattern_database = dict()     # str state : int count_moves / visited 배열이면서 database
        dxs = [1, 0, -1, 0]
        dys = [0, 1, 0, -1]
        pattern_numbers = [n for n in init_pattern if n != 0]

        queue = deque([(init_pattern, 0)])
        pattern_database[str(init_pattern)] = 0

        while queue:
            cur_state, cur_moves = queue.popleft()

            for pattern_number in pattern_numbers:
                move_tile = cur_state.index(pattern_number)
                i, j = move_tile // 4, move_tile % 4 # 크기 4를 객체에서 받도록 수정하기
                for dx, dy in zip(dxs, dys):
                    x, y = i + dx, j + dy
                    new_state = np.array(np.array(cur_state).reshape(4, 4))
                    if 0 <= x < 4 and 0 <= y < 4 and new_state[x, y] == 0:
                        new_state[i, j], new_state[x, y] = new_state[x, y], new_state[i, j]
                        new_state = new_state.flatten().tolist()
                        if str(new_state) not in pattern_database:
                            queue.append((new_state, cur_moves + 1))
                            pattern_database[str(new_state)] = cur_moves + 1
        return pattern_database

    def generate_pattern(self):
        print("start generating ...")

        A_pattern_database = self.generate_bfs(self.__A_pattern) # 성공 실패여부 출력하기
        database = open("A_database", "wb")
        pickle.dump(A_pattern_database, database)
        database.close()
        print("A_database generated")

        B_pattern_database = self.generate_bfs(self.__B_pattern)
        database = open("B_database", "wb")
        pickle.dump(B_pattern_database, database)
        database.close()
        print("B_database generated")

        C_pattern_database = self.generate_bfs(self.__C_pattern)
        database = open("C_database", "wb")
        pickle.dump(C_pattern_database, database)
        database.close()
        print("C_database generated")


if __name__ == "__main__":
    A = list(map(int, "1 2 3 0 5 6 0 0 0 0 0 0 0 0 0 0".split()))
    B = list(map(int, "0 0 0 4 0 0 7 8 0 0 11 12 0 0 0 0".split()))
    C = list(map(int, "0 0 0 0 0 0 0 0 9 10 0 0 13 14 15 0".split())) # 입력 받도록 수정
    test_generater = Pattern_generater(A, B, C)
    test_generater.generate_pattern()