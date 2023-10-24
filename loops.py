def calculate_exponent(num, exp):
  result = 1  
  for i in range(exp):
     result = result*num
  return result
  
#print(calculate_exponent(2, 2))

def findLargesrNum(nums):
    sorted_nums= sorted(nums, reverse= True)[0]
    return sorted_nums
#print(findLargesrNum([1,5,9,3]))
    
def findLargesrNum2(nums):
      largestNum = -100
      for ick in nums:
          if ick>largestNum:
              largestNum = ick
      return largestNum
#print(findLargesrNum2([1,5,9,3]))   
def findSmallestNum3(xyz):
    smallesNum = 50
    for sayi in xyz:
        if sayi<smallesNum:
            smallesNum = sayi
    return smallesNum
#print(findSmallestNum3([5,6,8,789]))   

