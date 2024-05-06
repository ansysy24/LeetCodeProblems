class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        st = set()
        result = []
        for num in nums:
            if num in st:
                result.append(num)
            else:
                st.add(num)
        return result