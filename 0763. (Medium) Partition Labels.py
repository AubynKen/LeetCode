class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in last:
                last[s[i]] = i

        res = [-1]

        curr = set()
        end = -1
        for i, ch in enumerate(s):
            if ch not in curr:
                curr.add(ch)
                end = max(end, last[ch])
            if i == end:
                res.append(i)
                curr = set()
                end = -1

        return [res[i] - res[i - 1] for i in range(1, len(res))]
