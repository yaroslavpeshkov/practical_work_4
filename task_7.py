score_k, score_ar, score_s = map(int, input().split())

if score_k > score_ar and score_k > score_s:
    print(score_k)
elif score_ar > score_k and score_ar > score_s:
    print(score_ar)
else:
    print(score_s)
