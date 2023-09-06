# def permute(nums):
#         def backtrack(curr):
#             if len(curr) == len(nums):
#                 ans.append(curr[:])
#                 return
        
#             for num in nums:
#                 if num not in curr:
#                     curr.append(num)
#                     backtrack(curr)
#                     curr.pop()
            
#         ans = []
#         backtrack([])
#         return ans

    
def permute(nums):
    ans = []
    curr = []
    if len(curr) == len(nums):
        ans.append(curr[:])
        return
        
    for num in nums:
        if num not in curr:
            curr.append(num)
            backtrack(curr)
            curr.pop()
    return ans