class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_map = {}

        for num in arr:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1

        seen = set()
        for freq in count_map.values():
            if freq in seen:
                return False
            seen.add(freq)

        return True