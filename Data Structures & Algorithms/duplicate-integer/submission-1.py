class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Initialising a Hashset
        hashset = set()   

        #go through each number in nums
        for n in nums:  
            #check if n is in a hashset                                      
            if n in hashset:                                   
                return True
            hashset.add(n)                                     
        return False

