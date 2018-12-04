# Carta-PortfolioAPI

Lara Corkrey
laracorkrey@gmail.com
https://github.com/laracork

Instructions (NOTE: This repo requires Python3.7)

Clone the repo into a local directory by typing
   `git clone https://github.com/laracork/Carta-PortfolioAPI` into the command line (without the quotes)

Before cd’ing into the cloned repo, set up a virtual environment with virtualenv ([virtualenv installation guide](http://docs.python-guide.org/en/latest/dev/virtualenvs/) - note you may need to use sudo with the installation like `sudo pip install virtualenv`)

After installing a virtualenv, run ‘virtualenv -p python3 envname’ (replace envname with the name of your local directory). This will ensure Python3.7 is running in your environment.

Activate the virtual environment by typing ‘source envname/bin/activate’ into the command line (without the quotes and with the correct directory name)

CD into the cloned repo (cd Carta-PortfolioAPI).

Run pip install pipenv in the command line

Run pipenv install requests in the command line to install the dependencies. More information here.

In the terminal, type ‘cd portfolioAPI’ (without the quotes) then hit enter twice. Type ‘ls’ and you should see ‘manage.py’

Start your server by typing python manage.py runserver in the command line

Navigate to the API in the browser (http://localhost:8000/investments)
Enjoy!
________________________________________________________________________________________________________________________
Note: If there is trouble installing the dependencies, it is most likely because Python3.7 is not running. There is one additional step that can be run BEFORE initiating the above. This step is likely redundant for most setups.

First create a directory for a virtual environment with Python3.7.

CD into the directory and type python3 -m venv /path/to/new/virtual/environment in the command line.
Instructions can be found here.
_______________________________________________________________________________________________________________________
Discussion
	I used the following technologies:
Python3.7
Django 2.1
Django REST Framework
Django Filters
SQLite

Requirements
“””
Create an API endpoint that returns the state of all investments on a given date in the investment timeline. If no date is passed, assume we want investments data as of today.
“””
I’ve used Python and the Django REST Framework to create this API. Data is listed chronologically with the most recent investment listed first. In order to view older investments, click on the filter button in the top right corner to sort by either the buy, sell, or updated dates.

‘’’’
We will also need endpoints to create new investments, and to update existing investments as we buy/sell shares (updating the quantity and cost values for that point onward).
“””
The Django REST framework provides one endpoint for creating, updating, and deleting investments.

To create a new investments, simply scroll to the bottom of Investments List, enter the requested information and click POST.

To edit an investment, click on the hyperlinked url above any of the listed company names. You will be taken to a detailed view of the investment where you can scroll to the bottom, change the information you want updated and click PUT.

To return to the list of investments, click on Investments List in the top left corner after Api root.

Further Considerations
“””
Company: the company we invested in (set only on creation)
“””
Creating the company_name field as a read-only will not allow the company name to be edited upon creation. Model fields can only be configured as editable only upon creation but read-only after creation when using the Developer version of Django. This has been an ongoing issue that Django finally updated five months ago but only for the Developer version.

I did find a library that provides a work around, however it seems only compatible with PostgreSQL and not SQLite. I choose SQLite to limit the scope of the project in order to focus on quality.

“””
Bonus:
Sometimes users input data incorrectly, or forget to input data in the system when they make an investment. Allow a user to update an investment for a date in the past, and separately keep track of the date that the actual data was entered. The updated data model should support querying the state of investments on both date dimensions at once, to answer questions like: "What was the state of my portfolio on 2016-01-01 with the data that I entered up to 2017-01-01."
“””
There are many validation and database consistency considerations for this issue that are better managed by PostgreSQL than SQLite. I choose SQLite to limit the scope of the project in order to focus on quality.
