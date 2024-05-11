from django.test import TestCase

# Create your tests here.
my_variable = 1
variable_name = 'my_variable'

if variable_name in globals():
    print(f"The variable {variable_name} exists.")
else:
    print(f"The variable {variable_name} does not exist.")
