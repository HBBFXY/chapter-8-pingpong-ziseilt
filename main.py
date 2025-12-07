import random

def simulate_single_game(p):
    """模拟单局比赛，p为球员A每分获胜的概率"""
    score_a, score_b = 0, 0
    while True:
        # 模拟1分的争夺
        if random.random() < p:
            score_a += 1
        else:
            score_b += 1
        
        # 判断单局胜负（11分且领先2分）
        if (score_a >= 11 or score_b >= 11) and abs(score_a - score_b) >= 2:
            return 1 if score_a > score_b else 0

def simulate_match(p):
    """模拟整场比赛（7局4胜），返回1表示A获胜，0表示B获胜"""
    win_a, win_b = 0, 0
    while win_a < 4 and win_b < 4:
        result = simulate_single_game(p)
        if result == 1:
            win_a += 1
        else:
            win_b += 1
    return 1 if win_a == 4 else 0

def analyze_competition(p, num_simulations=1000):
    """批量模拟并统计结果"""
    a_win_count = 0
    for _ in range(num_simulations):
        if simulate_match(p) == 1:
            a_win_count += 1
    return f"球员A每分胜率{p}时，{num_simulations}场比赛中获胜{round(a_win_count/num_simulations*100,2)}%"

# 示例：测试不同胜率的结果
print(analyze_competition(0.5))  # 双方实力相当
print(analyze_competition(0.55)) # 球员A略强
print(analyze_competition(0.6))  # 球员A明显强
