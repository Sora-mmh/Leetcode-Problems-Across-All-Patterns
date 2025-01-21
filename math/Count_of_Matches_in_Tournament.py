class Solution:
    def numberOfMatches(self, n: int) -> int:
      # simply return n-1 haha
      if n == 1:
          return 0
      num_matches = 0
      while n != 1:
          if n % 2 == 0:
              n //= 2
              num_matches += n
          else:
              n = (n - 1) // 2
              num_matches += n 
              n += 1
      return num_matches
        
