# username = 'jonsnow'
# email = 'jon@snow.com'
# password = 'thenorth'

# if username == 'jonsnow' and password == 'thenorth':
#   print('Access permitted')
# else:
#   print('Not allowed')


# if (username == 'jonsnow' or email == 'jon@snow.com') and password == 'thenorth':
#   print('Access permitted')
# else:
#   print('Not allowed')


# if username == 'jonsnow' or password == 'thenorth':
#   print('Access permitted')
# else:
#   print('Not allowed')


# logged_in = True
# standard_user = False

# if logged_in and not standard_user:
#   print('You can access the admin dashboard')
# else:
#   print('You can only access the standard dashboard')

# List of comparison operators
# == Equality
# != Inequality
# <> Inequality (deprecated)
# >  Greater than
# >= Greater than or equal to
# < Less than
# <= Less than or equal to
#---------------------------------------------------------

# Exercise

# Fill in the below conditional with a compound condition that will print "Success!" if "number" is anything between 1 and 100 (inclusive).

def compound_conditional(number):
    if (number >= 1) and (number <= 100):
        print("Success!")
    else:
        print("Failure...")
        
# username = 'wfontanez'
# email = 'wfontanez@gmail.com'
# pin = 1234
# password = 'isamazing'
# role = 'admin'

# #except username or email
# #pin
# #password
# #if admin it display You are the supreme ruler
# while True:
# 	username = input('username: ')
# 	if (input == 'wfontanez' or input == 'wfontanez@gmail.com'):
# 		print(password)

# 	else:
# 		print('Re-Enter Username:')
		
# 	password = input('Password: ')
# 	if (input == 'isamazing' or input == 1234):
# 		print('Access Permitted')
# 	else:
# 		print('Access Denied')
# 	if input == 'admin':
# 		print('You are the supreme ruler')
# 	else:
# 		print('You are a peasant')