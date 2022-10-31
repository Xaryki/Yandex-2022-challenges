orders = [list(map(int, input().split())) for _ in range(int(input()))]
query = [list(map(int, input().split())) for _ in range(int(input()))]

result_list = [sum(cost for start, _, cost in orders if q_start <= start <= q_end) if q_action == 1 else
sum(end - start for start, end, _ in orders if q_start <= end <= q_end) for q_start, q_end, q_action
in query]
print(*result_list)

