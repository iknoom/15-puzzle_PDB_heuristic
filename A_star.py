from heapq import *
import pickle
import numpy as np
import time

class Solver():
    def __init__(self, init_state):
        self.__init_state = init_state
        self.__pattern_database_A = None
        self.__pattern_database_B = None
        self.__pattern_database_C = None
        self.__is_loaded = False

    def load_pattern_database(self):
        file = open("A_database", "rb")
        self.__pattern_database_A = pickle.load(file)
        file.close()

        file = open("B_database", "rb")
        self.__pattern_database_B = pickle.load(file)
        file.close()

        file = open("C_database", "rb")
        self.__pattern_database_C = pickle.load(file)
        file.close()

        self.__is_loaded = True # 수정 예정

    def get_heuristic_value(self, cur_state):
        A = [a if a in [1, 2, 3, 5, 6] else 0 for a in cur_state]
        B = [b if b in [4, 7, 8, 11, 12] else 0 for b in cur_state]
        C = [c if c in [9, 10, 13, 14, 15] else 0 for c in cur_state]
        ret = 0
        ret += self.__pattern_database_A[str(A)]
        ret += self.__pattern_database_B[str(B)]
        ret += self.__pattern_database_C[str(C)]
        return ret

    def a_star(self):
        self.load_pattern_database()
        dxs = [1, 0, -1, 0]
        dys = [0, 1, 0, -1]
        start_t = time.time()

        init_state = self.__init_state
        init_step = 0
        init_heur = self.get_heuristic_value(init_state) + init_step

        visited = set()
        hq = [] # heap

        visited.add(str(init_state))
        heappush(hq, (init_heur, init_step, init_state))

        while hq:
            cur_heur, cur_step, cur_state = heappop(hq)
            if cur_heur == cur_step:
                print("answer :", cur_step)
                print("time :", time.time() - start_t)
                print("nodes :", len(visited))
                break

            empty_tile = cur_state.index(0)
            i, j = empty_tile // 4, empty_tile % 4
            for dx, dy in zip(dxs, dys):
                x, y = i + dx, j + dy
                new_state = np.array(cur_state).reshape(4, 4)
                if 0 <= x < 4 and 0 <= y < 4:
                    new_state[i, j], new_state[x, y] = new_state[x, y], new_state[i, j]
                    new_state = new_state.flatten().tolist()
                    if str(new_state) not in visited:
                        new_step = cur_step + 1
                        new_huer = self.get_heuristic_value(new_state) + new_step
                        visited.add(str(new_state))
                        heappush(hq, (new_huer, new_step, new_state))

    def solve(self, search_algorithm = "astar"):
        if search_algorithm == "astar":
            self.a_star()


if __name__ == "__main__":
    #init_input = list(map(int, "0 12 9 13    15 11 10 14    3 7 2 5    4 8 6 1".split())) # 80 step impossible
    #init_input = list(map(int, "0 12 10 13    15 11 14 9    3 7 2 5    4 8 6 1".split())) # 80 step impossible
    #init_input = list(map(int, "0 15 8 3    12 11 7 4    14 10 6 5    9 13 2 1".split())) # 70 step impossible
    #init_input = list(map(int, "6 5 9 13    2 1 10 14    3 7 0 15    4 8 12 11".split())) # 72 step impossible
    #init_input = list(map(int, "15 14 1 6    9 11 4 12    0 10 7 3    13 8 5 2".split())) # 52 step 94sec
    #init_input = list(map(int, "1 10 15 4    13 6 3 8    2 9 12 7    14 5 0 11".split())) # 35 step 0.4sec

    init_input = list(map(int, input("15-슬라이딩 퍼즐을 입력하세요.(ex : 1 10 15 4 13 6 3 8 2 9 12 7 14 5 0 11):\n-> ").split()))
    test = Solver(init_input)
    test.solve()
