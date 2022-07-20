"""Work with addition chains."""

# N = 370 count is too long 2-3 min
'''
def prepend(n, seq):
    return [n] + seq

def check_seq(pos, seq, n, min_len):
    if pos > min_len or seq[0] > n:
        return min_len, 0
    if seq[0] == n:
        return pos, 1
    if pos < min_len:
        return try_perm(0, pos, seq, n, min_len)
    return min_len, 0

def try_perm(i, pos, seq, n, min_len):
    if i > pos:
        return min_len, 0

    res1 = check_seq(pos + 1, prepend(seq[0] + seq[i], seq), n, min_len)
    res2 = try_perm(i + 1, pos, seq, n, res1[0])

    if res2[0] < res1[0]:
        return res2
    if res2[0] == res1[0]:
        return res2[0], res1[1] + res2[1]
    raise Exception("try_perm exception")

def init_try_perm(x):
    return try_perm(0, 0, [1], x, 12)

def find_brauer(num):
    res = init_try_perm(num)
    print()
    print("N = ", num)
    print("Minimum length of chains: L(n) = ", res[0])
    print("Number of minimum length Brauer chains: ", res[1])

# main
nums = [7, 14, 21, 29, 32, 42, 64, 47, 79, 191, 382, 379]
for i in nums:
    find_brauer(i)
'''

# Faster method
def bauer(n):
    chain = [0]*n
    in_chain = [False]*(n + 1)
    best = None
    best_len = n
    cnt = 0

    def extend_chain(x=1, pos=0):
        nonlocal best, best_len, cnt

        if x<<(best_len - pos) < n:
            return

        chain[pos] = x
        in_chain[x] = True
        pos += 1

        if in_chain[n - x]:  # found solution
            if pos == best_len:
                cnt += 1
            else:
                best = tuple(chain[:pos])
                best_len, cnt = pos, 1
        elif pos < best_len:
            for i in range(pos - 1, -1, -1):
                c = x + chain[i]
                if c < n:
                    extend_chain(c, pos)
        
        in_chain[x] = False
        
    extend_chain()
    return best + (n,), cnt

for n in [7, 14, 21, 29, 32, 42, 64, 47, 79, 191, 379, 382]:
    best, cnt = bauer(n)
    print(f'L({n}) = {len(best) - 1}, count of minimum chain: {cnt}/ne.g.: {best}\n')
