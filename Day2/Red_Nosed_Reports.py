def calc_safe_count():
    safe_count = 0
    
    with open("2_input.txt","r") as file:
        for report in file.readlines():
            print(f"report : {report}")
            report = list(map(int,report.split()))
            is_safe = True
            is_increasing = False
            is_decreasing = False

            if report[1] > report[0]:
                is_increasing = True
            else:
                is_decreasing = True
                
            # print(f"inc: {is_increasing} dec:{is_decreasing}")
            for i in range(1,len(report)):
                # print(f"r : {report[i]}")
                diff = report[i]-report[i-1]

                if 1 <= abs(diff) <= 3 and ((is_increasing and diff > 0) or (is_decreasing and diff < 0)):
                    continue
                else:
                    # print(f"not safe {diff} r : {report[i]}")
                    is_safe = False
                    break
            if is_safe:
                safe_count += 1
         
    return safe_count

def calc_safe_count_with_tolerance():
    safe_count = 0
    
    with open("2_input.txt","r") as file:
        for report in file.readlines():
            report = list(map(int,report.split()))
            print(f"report : {report}")

            is_safe = True
            is_increasing = False
            is_decreasing = False
            can_tolerate = True

            if report[1] > report[0]:
                is_increasing = True
            else:
                is_decreasing = True
                
            # print(f"inc: {is_increasing} dec:{is_decreasing}")
            i = 1
            while i < len(report):
                # print(f"r : {report[i]}")
                diff = report[i]-report[i-1]
                # print(f"diff : {diff}")
                if 1 <= abs(diff) <= 3 and ((is_increasing and diff > 0) or (is_decreasing and diff < 0)):
                    i += 1
                    # print("Safe")
                    continue
                else:
                    # print(f"not safe {diff} r : {report[i]}")
                    if can_tolerate:
                        can_tolerate = False
                        # print(f"r pop : {report.pop(i)}")
                        continue
                    # print("not safe")
                    is_safe = False
                    break
            if is_safe:
                safe_count += 1
                # print(f"report : {report} safe : {safe_count}")
         
    return safe_count


print(calc_safe_count_with_tolerance())