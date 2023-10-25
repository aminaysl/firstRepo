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

def differentNum(numss):
    smallest = sorted(numss)[0]
    biggest =  sorted(numss)[-1]
    return biggest-smallest
#print(differentNum([12,45,78,89,56]))

def differentNum2(numss):
    
    biggestNum = 200
    smallestNum =5
    for lol in numss:
        if lol>smallestNum:
            smallestNum = lol     
        
    for col in numss:    
        if col<biggestNum:
            biggestNum = col
    return  biggestNum - smallestNum
#print(differentNum2([12,45,78,89,56]))
  
def get_sum_of_elements(lst):
    numbero =sum(lst)
    return numbero
#print(get_sum_of_elements([1,5,7]))

def get_sum_of_element2(list):
    total = 0
    for num in list:
        total =total+ num
    
    return total
#print(get_sum_of_element2([1,5,7]))

def num_to_dashes(loopnum):
    dashes = ""
    for x in range(loopnum):
        dashes = dashes + "-"
        print(dashes)
    return dashes
#num_to_dashes(9)
    
#write function that takes an integer and returns a string
def how_many_times(num):
    str1 = "Ed"
    str2 = ""
    str3 = "bit"
    for x in range(num):
        str2 = str2 + "a"
    return str1 + str2 + str3 
#print(how_many_times(9))    

def all_truthy(*args):
     result = True
     for arg in args:
         if arg != True:
             result = False
     return result
#print(all_truthy(True, 5, True))





def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Shift the letter by 'shift' positions (wrap around the alphabet)
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            encrypted_text += encrypted_char
        else:
            # If it's not a letter, keep it as it is
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            # Shift the letter back by 'shift' positions (wrap around the alphabet)
            if char.islower():
                decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            else:
                decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            decrypted_text += decrypted_char
        else:
            # If it's not a letter, keep it as it is
            decrypted_text += char
    return decrypted_text

# Example usage:
message = "Hello, World!"
shift = 3
encrypted_message = encrypt(message, shift)
#print("Encrypted:", encrypted_message)
decrypted_message = decrypt(encrypted_message, shift)
#print("Decrypted:", decrypted_message)

def last_ind(lst):
    last_character = None
    for char in lst:
        last_character = char
    return char
print(last_ind([1,2,5,4,7,8,9]))   

             
         
         
