# No OK

n = 5
prices = [35, 40, 101, 59, 63]

coupons = 0
used_coupons = []
total_cost = 0

for i in range(n):
    if prices[i] >= 100:
        coupons += prices[i] // 100
        used_coupons.append(i + 1)
        total_cost += prices[i] - 100 * (prices[i] // 100)
    else:
        total_cost += prices[i]

if coupons > n - coupons:
    unused_coupons = coupons - (n - coupons)
else:
    unused_coupons = 0

print(total_cost)
print(unused_coupons, len(used_coupons))
for day in used_coupons:
    print(day)
