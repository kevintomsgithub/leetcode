def isToeplitz(arr):
  """
  @param arr: int[][]
  @return: bool
  """
  rows = len(arr)
  check_array = arr[0][:-1]
  for row in range(1, rows):
    for i in range(len(check_array)):
      if check_array[i] != arr[row][i+1]: return False
    check_array = arr[row][:-1]
  return True

a  = [[4,0],[9,4]]
print(isToeplitz(a))