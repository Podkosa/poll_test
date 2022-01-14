Poll test app for "Фабрика Решений"

Local installation and basic functionalities guide:

1) Make sure the latest Python 3 version is installed
2) (Optionally) create a virtual environment
3) Set environmental variable SECRET_KEY to a suitable key
4) From command line in the root directory, run the following commands:
pip install -r requirements.txt  #installs the needed dependancies
python manage.py createsuperuser #follow the prompts to set a user, which will be used for admin login page  
python manage.py runserver       #runs the server on localhost:8000 
4) The following urls are available:
5) 
http://localhost:8000/ #intentionally left blank

http://localhost:8000/admin/ #admin site login page
provides poll management functionality (create, read, update, delete)

http://localhost:8000/polls/ #polls application URL

http://localhost:8000/polls/active #returns a list of active polls

http://localhost:8000/polls/vote #vote functionality URL, accepts POST HTTP requests, expects 3 arguments: user_id, poll (specific poll id), answers ({question:answer} as a string!)

http://localhost:8000/polls/vote/user-votes #displays polls that the user finished
