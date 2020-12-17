import os

try:
    os.rmdir("./file/temp")
 except Exception as e:
    print(e)
