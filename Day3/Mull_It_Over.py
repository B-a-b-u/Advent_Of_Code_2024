import re
def calc_mul():
    res = 0
    pattern = "mul\((\d+,\d+)\)"
    with open("1test_input.txt","r") as file:
        for memory in file.readlines():
            print(f"m  :{memory}")
            matches = re.findall(pattern,memory)
            print(f"match : {matches}")
            for exp in matches:
                num1,num2 = map(int,exp.split(","))
                print(f"n1:{num1} n2:{num2}")
                res += num1 * num2
            
    return res




def calc_mul_ins():
    res = 0
    
    pattern = r"(do\(\))|(don't\(\))|mul\((\d{1,3},\d{1,3})\)"
    is_enabled = True

    with open("3_input.txt", "r") as file:
        for input in file.readlines():
            print(f"inp  : {input.strip()}")
            matches = re.findall(pattern, input)
            print(f"match : {matches}")
            
            for match in matches:
                if match[0]:
                    print("Enabling multiplications")
                    is_enabled = True
                elif match[1]:  
                    print("Disabling multiplications")
                    is_enabled = False
                elif match[2]:  
                    if is_enabled:
                        num1, num2 = map(int, match[2].split(","))
                        print(f"Found mul({num1}, {num2}), adding {num1 * num2} to the result.")
                        res += num1 * num2
                        
    return res
print(calc_mul_ins())
