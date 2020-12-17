# https: //www.learnpython.org/en/Pandas_Basics
import pandas as pd
from numpy import random as npr
data = {
    "country": [
        "Brazil",
        "Russia",
        "India",
        "China",
        "South Africa"
    ],
    "capital": [
        "Brasilia",
        "Moscow",
        "New Dehli",
        "Beijing",
        "Pretoria"
    ],
    "area": [
        8.516,
        17.10,
        3.286,
        9.597,
        1.221
    ],
    "population": [
        200.4,
        143.5,
        1252,
        1357,
        52.98
    ]
}

# main method...
if __name__ == "__main__":
    table = pd.DataFrame(data)
    # set index
    print(table)
