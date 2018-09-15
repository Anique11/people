# people
A small python utility to keep track of people and the meetings they are invited to.

# background
As a SCRUM master for a multi-focused team that often changes composition (don't ask!), I often found myself needing to figure out who needs to attend which meeting.
For planning these meetings, I want to know how many chairs I need, and get a list of e-mails for sending out the invite.
I used to track this in Excel (o horror of horrors...), but soon found that this was not giving me the information I needed as easily as I wanted it.
Thus, I decided to build myself this small utility.

# requirements
- Python 3 (tested on 3.6.4)

# operation
It is currently meant to be run in an interactive Python session. The Api module provides the storage of data (using pickle).

## starting
On CLI, navigate to the project folder and start a Python session. Then:  
`from api import Api`  
`api = Api()`  
## getting hold of the team object
- first time:
`team = api.initialise()`
- subsequent times:
`team = api.load()`
## working with meetings and people
The interface for this is not complete and will probably change much in the future. Have a peek in the code to see what is currently possible.
Many of the attributes of objects are accessed directly instead of through a getter or setter method. This may change in future.

In general, though, adding meetings or people to the team object will return the newly added meeting or person object, so that you can directly work with it. This behavior is not likely to change.
## saving the team object
On closing the session (by using `exit()`) the team object is stored in a file called 'team.pickle'.
However, don't blindly trust on this happening. Especially after entering a lot of data, use `api.save()` to store the current data.

# NOTES
- If you inadvertently called `api.initialise()` while you have data in an existing 'team.pickle' file, call `api.load()` again to prevent losing that data.
You _will_ probably have lost any changes you made after your last save though. It may be possible to save it by calling `api.save(team)` - unless you stored the return value of `api.initialise()` in `team` - then your unsaved data is really lost. Anyway, no guarantees. Backup your existing picke file first.
- This utility is still under (heavy) development. Some changes to the code may prevent an existing pickle file from loading.
If you do want to use the code as-is to work with any data that is important to you, store the current code state in a separate branch that you don't change anymore, and use that to handle that particular dataset.
(Though there is nothing stopping you from trying to work with updated code and the same data - it may work. Just backup the data first.)
- This utility stores people's names and e-mail addresses. This is personal data, which falls under GDPR.
If you use information from real people in this tool, treat your team.pickle file with care and don't leave it lying around where others can find it.
