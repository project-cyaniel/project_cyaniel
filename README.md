# <h2>Project_Cyaniel</h2>

<h2>LARP Manager Application Built in Flask</h2>

<h3>Setting up a dev environment</h3>

1. Update [Python](https://www.python.org/downloads/release/python-361/) version to 3.6
2. Update [Pip](https://packaging.python.org/installing/) to latest version
3. Use [this](http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/) trusty guide to install Python Virtual Environment
4. Choose your IDE of choice. [Pycharm](https://www.jetbrains.com/pycharm/specials/pycharm/pycharm.html?&gclid=CJeg6fvXktMCFYGTfgodmcEHHw&gclsrc=aw.ds.ds&dclid=CMifiPzXktMCFRWMYgodj94CcQ) is great and has integrated VCS. Watch out for those pycache files though. 
   Pretty sure they shouldn't commit to the project though, as they're in .gitignore. Someone who is better with git stuff should probably fix this.
5. Clone the project, change directory to the project root, and then start your virtual environment by running:
   `source project_cyaniel_venv/bin/activate`
   You should now see your command prompt prefaced by the name of the virtual environment. This will contain all modules and/or packages needed for the project. Feel free to drop whatever
   you need in here. We can do cleanup later, but will eventually need to establish a requirements.txt file to populate whatever app server we're going use with these requisite libraries/modules, etc...
   