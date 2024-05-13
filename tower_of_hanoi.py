class Solution:
    def toh(self, N, fromm, to, aux):
        moves = [0]  # List to store the number of moves, using a list to allow modification within the recursive function

        def move_disk(disk, from_rod, to_rod):
            print("move disk", disk, "from rod", from_rod, "to rod", to_rod)
            moves[0] += 1  # Increment the total moves count

        def hanoi(n, source, target, auxiliary):
            if n == 1:
                move_disk(n, source, target)
                return
            hanoi(n - 1, source, auxiliary, target)
            move_disk(n, source, target)
            hanoi(n - 1, auxiliary, target, source)

        hanoi(N, fromm, to, aux)
        return moves[0]  # Return the total moves made

# Example usage:
s = Solution()
N = 3
print("Total moves:", s.toh(N, 1, 3, 2))
