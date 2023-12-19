def calibrate():
  f = open("input/day01.txt", "r")
  lines = f.read().split('\n')

  res = 0
  for idx in lines:
    res += digit_locator(idx)
  
  return res
  

def digit_locator(str):
  res = ""

  i = 0
  flipped = False
  while True:
    temp = str[i]
    if (temp.isnumeric()):
      res += temp

      i = len(str)
      flipped = not flipped
    
    i = i - 1 if flipped else i + 1
    if (len(res) == 2):
      break

  return int(res)
