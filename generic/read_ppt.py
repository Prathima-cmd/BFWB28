from pyjavaproperties import Properties

p_file=Properties()
p_file.load(open("config.properties"))

value=p_file["ITO"]
print(p_file.items()) # to get the all the values in the dictionaries.


print(value)
print(type(value))