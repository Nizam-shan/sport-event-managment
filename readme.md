Make sure you have installed Python, Django and Virtualenv in your system or Install them by:

        Install Python : 
        1. Go to 'https://www.python.org/downloads/' , download and install latest version on Python.

        Install Django :
        1. Open CMD / Command Prompt
        2. Enter command 'pip install django'

        Install Virtualenv :

        1. Open CMD / Command Prompt
        2. Enter command 'pip install virtualenv'


1. Open CMD / Command Prompt

2. Go to project folder. 

        If the project is in desktop : 
                1. cd desktop
                2. cd 'project folder name' 

3. Create Virtualenv using 'virtualenv env' command.


4. Activate virtualenv by command 'env\Scripts\activate'

    you should see a '(env)' in the starting of command line.
        eg : (env) C:\Users\Name\Desktop\Project_Name>

5. Use 'pip install -r requirements.txt' command to install all packages which is used in this project to your virtualenv.


6. Use 'python manage.py runserver' command to run the project.

7. 'http://127.0.0.1:8000/' go to this link in your browser to see the project.

8. Use 'ctrl+c' to stop the server

Admin Page.

'http://127.0.0.1:8000/newadmin/'

User Name : admin
Password  : admin