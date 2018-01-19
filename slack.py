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
emails = []
with open(csv_file, 'r') as csvfile:
    reader = csv.reader(csvfile)  # Don't include header
    is_header = True
    for row in reader:
        if is_header:
            is_header = False
            continue
        emails.append(row[1])  # Col 1 is where the emails are

# Get API Token from environment variable
if 'SLACK_API_TOKEN' not in os.environ:
    print('ERROR!!!')
    print('Please set the SLACK_API_TOKEN environment variable.')
    print('Check the README for more info.')
    sys.exit(-1)
else:
    slack_api_token = os.environ['SLACK_API_TOKEN']

# Invite all people that we can
for email in emails:
    try:
        invite('ieee-wit', slack_api_token, email)
        print('Invited ' + email)
    except Exception as e:
        print(email + ' failed with ' + e.__class__.__name__ + '.')
