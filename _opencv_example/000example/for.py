import numpy as np

waist =  float(input('허리 둘레를 입력해라'))
if waist < 27:
    print("smnall")
elif waist < 30:
    print("medium")
else:
    print("large")