        i = 0 
        occ = {}
        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in occ:
                return [i,occ[remaining]]
            else:
                occ[nums[i]] = i