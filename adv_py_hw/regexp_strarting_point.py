import re

# come up with one regexp pattern that matches all of these and only
# these
test_list1 = ['Last Name', \
              'Last name', \
              'last name', \
              'Lastname', \
              'lastname', \
              ]

# you should test that your pattern does NOT match any of these:
bad_list = ['last', \
            'name', \
            'LN', \
            'LName', \
            'first name', \
            'First Name', \
            'firstname', \
            'Firstname', \
            ]
