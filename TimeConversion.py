def is12(s):
    if s[:2] == "12":
        return True
    return False

def isPM(s):
    if s[8:] == "PM":
        return True
    return False

def timeConversion(s):
    # Write your code here
    if not isPM(s) and is12(s):
        return "00" + s[2:8]
    
    if (isPM(s) and is12(s)) or not isPM(s):
        return s[:8]

    if isPM(s):
        return str(int(s[:2])+12)+s[2:8]
