from slackipycore import invite
import csv
import os
import sys


# Error if no file path
if len(sys.argv) != 2:
    print('ERROR!!!')
    print('Please enter the csv file path as a cmd line argument!')
    print('Check the README for more info.')
    sys.exit(-1)
csv_file = sys.argv[1]
csv_file = os.path.expanduser(csv_file)  # Expand the ~

# Error if the file doesn't exist
if not os.path.isfile(csv_file):
    raise FileNotFoundError('The file that you entered cannot be found.')

# Get the emails from the csv file
# Doesn't have any sort of validation that these are emails
# The Slack library will just throw an exception in that case `\_O_/`
names = []
emails = []
with open(csv_file, 'r') as csvfile:
    reader = csv.reader(csvfile)  # Don't include header
    is_header = True
    for row in reader:
        if is_header:
            is_header = False
            continue
        names.append(row[0])   # Col 0 is where names are
        emails.append(row[1])  # Col 1 is where the emails are

# Get API Token from environment variable
if 'SLACK_API_TOKEN' not in os.environ:
    print('ERROR!!!')
    print('Please set the SLACK_API_TOKEN environment variable.')
    print('Check the README for more info.')
    sys.exit(-1)
else:
    slack_api_token = os.environ['SLACK_API_TOKEN']

number_invited = 0
# Invite all people that we can
for name, email in zip(names, emails):
    try:
        invite('ieee-wit', slack_api_token, email)
        print('Invited {} ({})'.format(name, email))
        number_invited += 1
    except Exception as e:
        if email == '':
            print('{} did not list an email.'.format(name))
        else:
            err = e.__class__.__name__
            print('{} ({}) failed with {}.'.format(name, email, err))

print('New people invited: {}'.format(number_invited))
