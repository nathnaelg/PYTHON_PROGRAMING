Full_name = 'John Smith'
age = 20
is_new = True 

print (Full_name, age, is_new)

#............Receving Input form User......

name = input( 'What is your Name ? ' )
'''we can desplay by two mathods 
    1, print( 'hey ' + name )
    2, print( 'hey' " " + name)
'''
# now we use the second one 

print ( 'Hey' " " + name )

name = input( 'What is Your Name ? ')
favorite_clolr = input('what is your favorite color ? ')

print ( name + ' likes ' + favorite_clolr )

#.... Type Conversion....

birth_year = input( 'Birth Year: ' )

#..... to see types of birth_year
print(type(birth_year))
#.........

age = 2023 - int(birth_year)

#..... to see types of age 
print(type(age))
#......
print (age)

#... convert weight (in pounds), to killogram 

weight_lbs = input('weight (lbs): ')
weight_kg = int(weight_lbs) * 0.45

print (weight_kg)