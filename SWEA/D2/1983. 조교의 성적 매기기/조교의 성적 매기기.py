T = int(input())
grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for t in range(1, T+1):
    n, k = map(int, input().split())
    total = []

    for i in range(n):
        m_term, f_term, ass = map(int, input().split())
        tt = (m_term * 0.35) + (f_term * 0.45) + (ass * 0.2)
        total.append(tt)

    K_score = total[k-1]

    total.sort(reverse=True)
    K_total = total.index(K_score) // (n // 10)

    print(f'#{t}', grades[K_total])