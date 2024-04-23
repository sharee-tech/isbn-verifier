def is_valid(isbn):
  nums = list(isbn.replace("-", ""))
  if len(nums)!=10: return False
  if nums[-1] == "X": 
      nums[-1] = "10"
  if not all([c.isdigit() for c in nums]): 
      return False
  return sum(int(x)*y for x,y in zip(nums, range(10, 0, -1)))%11 == 0

# Test the function
print(is_valid("3-598-21507-X"))   # True
print(is_valid("3-598-21508-8"))   # True
print(is_valid("359821507X"))      # True
print(is_valid("3598215088"))      # True
print(is_valid("1234567890"))      # False

