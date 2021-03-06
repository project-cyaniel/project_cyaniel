# <h2>Project_Cyaniel</h2>

<h2>LARP Manager Application Built in Flask</h2>

<h3>Setting up a Working Dev Environment</h3>

1. Update [Python](https://www.python.org/downloads/release/python-361/) version to 3.6
2. Update [Pip](https://packaging.python.org/installing/) to latest version
3. Use [this](http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/) trusty guide to install Python Virtual Environment
4. Choose your IDE of choice. [Pycharm](https://www.jetbrains.com/pycharm/specials/pycharm/pycharm.html?&gclid=CJeg6fvXktMCFYGTfgodmcEHHw&gclsrc=aw.ds.ds&dclid=CMifiPzXktMCFRWMYgodj94CcQ) is great and has integrated VCS. Watch out for those pycache files though. 
   Pretty sure they shouldn't commit to the project though, as they're in .gitignore. Someone who is better with git stuff should probably fix this.
5. Clone the project, change directory to the project root, and then start your virtual environment by running:</br>
   `source project_cyaniel_venv/bin/activate`</br>
   You should now see your command prompt prefaced by the name of the virtual environment. This will contain all modules and/or packages needed for the project. Feel free to drop whatever
   you need in here. We can do cleanup later, but will eventually need to establish a requirements.txt file to populate whatever app server we're going use with these requisite libraries/modules, etc...
6. Run the following commands to set up the requisite environment variables:</br>
   `export FLASK_APP=run.py`</br>
   `export FLASK_CONFIG=development`
7. To run the app, simply change directory to `project_cyaniel/project_cyaniel` and then run:</br>
   `flask run`</br>
   If there are any errors, you will notice right away, otherwise, navigate to `localhost:5000` in your browser.
   
<h3>Database Connection Details</h3>

1. All database connection information can be found in the project google doc. Please request a share if you need it.
   The dev database is hosted via AWS and is MySQL. You will need to hand over your IP so I can assign it to the db security group.
2. For testing purposes please make your own development database, as the `larpworks_db` needs to be the stable version we use for testing. Please
   refer to the google doc and MySQL documentation on how to do this.
3. Once you've created your own db, set up your connection string in the `/instances/config.py` file. Change directory to
   `project_cyaniel/project_cyaniel/` and then run:</br>
   `flask db migrate`</br>
   `flask db upgrade`
4. At the MySQL console, run:</br>
   `use <database name>`</br>
   `show tables;`
5. You should see all project tables (as listed in models.py) in your new database. Please *DO NOT* make changes to the larpworks_db without
   first going through code review. Thanks.