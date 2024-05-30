class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        length = len(arr)
        for i in range(length):
            left_arrays_count= i + 1
            right_arrays_count= length - i
            total_subarrays = left_arrays_count * right_arrays_count
            odd_subarrays = (total_subarrays + 1) // 2
            
            total += arr[i] * odd_subarrays
            
        return total