class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        pas, res = 0, 0
        for b in buses:
            cp = capacity
            while cp > 0 and pas < len(passengers) and passengers[pas] <= b:
                if pas == 0 or passengers[pas] - 1 != passengers[pas - 1]:
                    res = passengers[pas] - 1
                pas += 1
                cp -= 1
            if cp > 0 and (pas == 0 or passengers[pas - 1] != b):
                res = b

        return res