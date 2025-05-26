class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        n = len(distance)
        if n <= 3:
            return False
        else:
            for counter in range(3, n):
                if distance[counter - 2] <= distance[counter] and distance[counter - 1] <= distance[counter - 3]:
                    return True
                if counter >= 4 and distance[counter - 1] == distance[counter - 3] and distance[counter -2] <= distance[counter] + distance[counter - 4]:
                    return True
                if counter >= 5 and distance[counter - 4] <= distance[counter - 2] and distance[counter - 2] <= distance[counter] + distance[counter - 4] and distance[counter - 1] <= distance[counter - 3] and distance[counter - 3] <= distance[counter - 1] + distance[counter - 5]:
                    return True
                counter += 1
            return False
