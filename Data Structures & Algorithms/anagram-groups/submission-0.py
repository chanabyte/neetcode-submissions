class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for s in strs:
            sorted_string = "".join(sorted(s))
            mp[sorted_string].append(s)
        op = []
        for k in mp.keys():
            op.append(mp[k])
        return op