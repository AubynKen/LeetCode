from collections import Counter

class Solution:
    
    def top_k(self, counts, k):
        # terminal case
        if len(counts) == k:
            return list(map(lambda val_count_pair : val_count_pair[0], counts))
        
        pivot = random.choice(counts)[1]
        left, mid, right = [], [], []
        for val, count in counts:
            if count > pivot:
                left.append((val, count))
            elif count < pivot:
                right. append((val, count))
            else:
                mid.append((val, count))
        if len(left) >= k:
            return self.top_k(left, k)
        if len(left) + len(mid) >= k:
            return self.top_k(left, len(left)) + self.top_k(mid, k - len(left))
        return self.top_k(left, len(left)) + self.top_k(mid, len(mid)) + self.top_k(right, k - len(left) - len(mid))
        
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = list(Counter(nums).items())
        return self.top_k(counts, k)
        