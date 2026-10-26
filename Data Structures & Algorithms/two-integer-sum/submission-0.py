class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #initialise an empty hashmap
        hashmap = {}

        for i, n in enumerate(nums): # n is the values at different indices
            diff = target - n  #diff to check if we already has it in the hashmap
            if diff in hashmap: #check if it is in hashmap
                return [hashmap[diff], i] #return the indices
            hashmap[n] = i #if not then update hashmap, so we can say that this n is in the index i 
        return