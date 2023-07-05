import ezgmail, os

# Initialize connection to gmail use api

os.chdir(r'C:\path\to\credentials_json_file')
ezgmail.init()

# To remember whis gmail adress is in use, initialize with ezgmail.init() first.

ezgmail.EMAIL_ADDRESS
# Returns  <<youremailaddress>>@gmail.com
