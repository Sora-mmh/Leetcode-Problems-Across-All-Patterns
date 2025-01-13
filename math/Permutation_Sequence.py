class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Solution1:
        def fact(m):
            if m == 1:
                return 1
            return m * fact(m - 1)
        def get_sequence(n,k):
            seq = []
            k = k - 1
            for i in range(n-1,0,-1):
                quotient,remainder = k // fact(i), k % fact(i)
                seq.append(quotient)
                k = remainder
            return seq
        sequene = get_sequence(n,k)
        res = ''
        array = [str(i) for i in range(1,n+1)]
        while sequene :
            index = sequene.pop(0)
            res += array[index]
            del array[index]
        res += array[0]
        return res 
        
        # Solution2
        # import itertools
        # if n == 1:
        #     return "1"
        # if n == 2:
        #     return ["12", "21"][k - 1]
        # else:
        #     k_rng = fact(n)
        #     grp_rng = k_rng // n
        #     grps = list(range(1, k_rng, grp_rng)) + [k_rng + 1]
        #     for idx in range(1, len(grps)):
        #         if grps[idx - 1] <= k < grps[idx]:
        #             grp = idx
        #             break
        #     nums = list(range(1, n + 1))
        #     nums.remove(grp)
        #     str_nums = "".join(list(map(str, nums)))
        #     combinations = ["".join(p) for p in list(itertools.permutations(str_nums))]
        #     comb = combinations[k % grp_rng - 1]
        #     return str(grp) + comb
