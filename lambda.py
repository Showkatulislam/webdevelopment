people=[
    {'name':'jayed','house':'satkania'},
    {'name':'mukter','house':'Rangunia'},
    {'name':'shuvo','house':'patikcori'}
]
# def f(person):
#     return person['name']
# people.sort(key=f)
people.sort(key=lambda person:person['name'])
print(people)