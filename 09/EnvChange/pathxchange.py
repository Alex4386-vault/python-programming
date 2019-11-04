import os
homeDir = os.path.expanduser("~/Assets/python_modules")

import sys
sys.path.append(homeDir)

try:
    import calc as c

    a,b = 10,5
    print("add =", c.add(a,b))
    print("sub =", c.sub(a,b))
    print("mul =", c.mul(a,b))
    print("div =", c.div(a,b))
except:
    print()
