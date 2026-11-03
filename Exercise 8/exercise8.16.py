#greet.py
def greet_user():
    """Print a simple greeting."""
    print("Hello!")
    
#main.py
# 1. import module_name
import greet
greet.greet_user()

# 2. from module_name import function_name
from greet import greet_user
greet_user()

# 3. from module_name import function_name as fn
from greet import greet_user as gu
gu()

# 4. import module_name as mn
import greet as g
g.greet_user()

# 5. from module_name import *
from greet import *
greet_user()