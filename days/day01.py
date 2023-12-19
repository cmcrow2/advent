import helpers.word_to_num as word_to_num

def calibrate(part):
    f = open("input/day01.txt", "r")
    lines = f.read().split('\n')

    res = 0
    for idx in lines:
        if part == "2":
            idx = translate_word_to_num(idx)
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

def translate_word_to_num(str):
    idx_map = {}
    for entry in word_to_num.dict:
        i = str.index(entry) if entry in str else "-1"
        j = str.rindex(entry) if entry in str else "-1"
        idx_map[i] = entry
        idx_map[j] = entry
      
    if idx_map["-1"]:
        del idx_map["-1"]

    keys = list(idx_map.keys())
    keys.sort()
  
    if len(keys) != 0:
        first_idx = keys[0]
        last_idx = keys[-1]
        str = str.replace(idx_map[first_idx], word_to_num.dict[idx_map[first_idx]], 1)
        str = str.replace(idx_map[last_idx], word_to_num.dict[idx_map[last_idx]], 1)

    return str

  
