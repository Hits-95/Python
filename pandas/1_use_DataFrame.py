import pandas

mydataset = {
    'students': ['Hitesh', 'PD', 'Suyesh', 'Shubham'],
    'marks': [76, 76, 89, 87],
    'addr': ['Dabli', 'Tehare', 'Malegaon', "Dabli"]
}

myvar = pandas.DataFrame(mydataset)
print(myvar)
