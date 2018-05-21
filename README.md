# Global-Health-Impact
Get your GHI project up and running on local machine.

# Environment setup for python and flask.

•	Install Sublime text (or editor of your own choice).

•	Install Python (above version 2.7).

•	Install Flask.

•	Install pandas (check the commands as per windows, LINUX or Mac).

	python -m pip install pandas
	
•	Install openpyxl.

	pip3 install --user openpyxl


# Start with project - 

Clone the GitHub project 
• 	Download the latest version of the project. (Please clone it from the GitHub on your local directory).
Follow the below document for cloning from GitHub. 

https://help.github.com/articles/cloning-a-repository/ 

After cloning the project and python setup, now make changes in flask_app.py to connect to the database.

•	Go to file flask_app.py 

•	Line number 47, change the path as per your machine to connect to sqllite3.

`def connect_db():`

`print("in connect_db")`
   
`return sqlite3.connect('F:\GHI\ghi2\mysite\ghi.db')`


Now you are all set to run the project on your local machine.

•	If you are on LINUX machine follow below command to run the application.

`$ export FLASK_APP=flask_app.py`

`$ flask run`

•	If you are on Windows machine follow below command to run the application.


`$ set FLASK_APP=flask_app.py`

`$ flask run`

You can find your localhost URL after flask run – Example http://127.0.0.1:5000/  

Here you go, your application is up and running. 
