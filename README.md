# 15-puzzle_PDB_heuristic
[Additive pattern database heuristic](https://www.aaai.org/Papers/JAIR/Vol22/JAIR-2209.pdf)에서 5-5-5 Statically-Partitioned Additive Database Heuristic을 이용한 A* 알고리즘을 구현

### 실행 방법
1. [pattern_generater.py](https://github.com/iknoom/15-puzzle_PDB_heuristic/blob/master/pattern_generater.py)를 실행해서 5-5-5 PDB를 생성
2. [A_star.py](https://github.com/iknoom/15-puzzle_PDB_heuristic/blob/master/A_star.py) 실행 후 15-puzzle의 초기상태 입력
3. 실행 결과를 확인

### 결과

1 10 15 4
<br>13 6 3 8
<br>2 9 12 7
<br>14 5 0 11
<br>=> 35 step : 0.4sec

15 14 1 6
<br>9 11 4 12
<br>0 10 7 3
<br>13 8 5 2
<br>=> 52 step : 94sec

6 5 9 13
<br>2 1 10 14
<br>3 7 0 15
<br>4 8 12 11
<br>=> 72 step : impossible

### 발표 자료
[발표 자료](https://www.slideshare.net/secret/kPoQR25JDZfn7H)
