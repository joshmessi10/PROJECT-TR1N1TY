import re
def validate(num):
    pattern = r'^[456](\d){15}$'
    pattern2 = r'^[456](\d){3}\-(\d){4}\-(\d){4}\-(\d){4}$'
    pattern3 = r'(?!.*([0-9])(\1){3})'
    ok1 = bool(re.match(pattern, num))
    ok2 = bool(re.match(pattern2, num))
    num = num.replace("-", "")
    ok3 = bool(re.match(pattern3, num))
    if (ok1 or ok2) and ok3:
        print("Valid")
    else:
        print("Invalid")

for _ in range(int(input())):
    num = input()
    validate(num)
