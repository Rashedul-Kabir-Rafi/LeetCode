class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in image:
            i.reverse()
        return [[1 if element == 0 else 0 for element in row]for row in image]