# Nested Dictionary: Nesting Dictionary means putting a dictionary inside another dictionary.
# It's a collection of dictionaries into one single dictionary.

# Create a Nested Dictionary

course={
    'php':{'duration':'2 months','fees':'15000'},
    'python': {'duration':'2 months','fees':'15000'},
    'java':{'duration':'2 months','fees':'15000'}
}
# print(course['java'])
# print(course['java']['fees'])

# print(course)

# update krna -------->>>

course['java']['fees']=20000
course['php']['duration']='5 months'


for k,v in course.items():
    print(k,v['duration'],v['fees'])
