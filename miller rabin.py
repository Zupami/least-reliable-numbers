from collections import Counter

liars = []
liar_cases = []
for n in range(5, 10000, 2):
    if n % 100 == 1:
        print(n) # Progress counter
    composite = False
    prime_claimers = []
    d = n - 1
    s = 1
    while d % 2 == 0:
        d = int(d / 2)
        s += 1
    for a in range(2, n - 1):
        prime_claim = False
        x = a
        for _ in range(d - 1): # Very inefficient mod exponentiation
            x = (x * a) % n
        if x == 1 or x == n - 1:
            prime_claim = True
            prime_claimers.append(a)
        else:
            for _ in range(1, s):
                x = (x * x) % n
                if x == n - 1:
                    prime_claim = True
                    prime_claimers.append(a)
                    break
        if not prime_claim:
            composite = True
    if composite:
        for liar in prime_claimers:
            liars.append(liar)
            liar_cases.append((liar, n))

most_common_liars = Counter(liars).most_common(10)
print("The most common liars are:")
print(most_common_liars)
most_common_liar = most_common_liars[0][0]
print(str(most_common_liar) + " is lying about the following numbers:")
most_common_liar_cases = filter(lambda case: case[0] == most_common_liar, liar_cases)
print(list(map(lambda case: case[1], most_common_liar_cases)))












