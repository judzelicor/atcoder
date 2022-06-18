class Solution:
    def solve(self):
        A, B = map(int, input().split())
        power_strip_count = 0
        empty_socket_per_power_strip = 0
        empty_sockets_count = 1

        while empty_sockets_count < B and empty_sockets_count:
            power_strip_count += 1

            if power_strip_count > 1:
                empty_socket_per_power_strip = 1

            empty_sockets_count = (A * power_strip_count) - (empty_socket_per_power_strip * (power_strip_count - 1))

        print(power_strip_count)

solution = Solution()

