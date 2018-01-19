# Invite-People-Slack
Grab all users from our attendance sheet and invite them to join the ieee-wit.slack.com team.

**NEVER CHECK IN THE SLACK API TOKEN INTO THIS REPOSITORY. THAT IS A VERY BAD IDEA.**

## How to Use
1. You need to acquire a [Slack API token](https://api.slack.com/custom-integrations/legacy-tokens). You can only get this if you are logged in as an admin of the team (aka e-board).
2. Download the attendance sheet from Google Sheets as a csv. Make sure you are on the sheet that has the emails of the people you want to add (usually the most recent semester).
3. `export SLACK_API_TOKEN="<paste the slack api token here>"`
4. `pip install -r requirements.txt`
5. `python slack.py <path to the csv attendance file here>`

## Notes
* This program requires python 3 due to the library that it uses. That also means you must use pip3. If you are using a standard linux/macOS machine, your commands may be `pip3` and `python3` above.
