import pandas

mydataset = {
    'students': ['Hitesh', 'PD', 'Suyesh', 'Shubham'],
    'marks': [76, 76, 89, 87],
    'addr': ['Dabli', 'Tehare', 'Malegaon', "Dabli"],
    'age': [22, 22, 28, 21]
}

myvar = pandas.DataFrame(mydataset)
print(myvar)
