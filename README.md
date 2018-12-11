# password_manager

This is my recuitment task

## Instalation

In order to install project you have type thos commands in your console simple:

	1. git clone https://github.com/mzoladki/password_manager.git
	2. pip install -r requirements.txt
	3. python generate_key.py (please remember to run it only when you're in api/ directory)
	4. python manage.py migrate
	5. python manange.py runserver


And now you can have fun with project.

## Usage

Please remember to create account - go to ` /signup/ ` endpoint an fullfill forms.
Just after that proccess you can easily start using pass-manager.

## About

I strongly believe that apps that we're creating should just fit our needs.
An because of that I decided to:

	1. Use SQLite instead of Postgresql (for an example).
	Despite for the fact that postgresql is much stronger than sqlite, in this case using postgres is not needed.
	2. Use sometimes function based views instead of class-based views. 
	When all that view has to do is render HTML file there is no need to take much fatter classes.
	3. I decided to use RSA cryptosystem because it's easy to implement (especially with python librerys) and secure.

## What to fix


<<<<<<< HEAD
11.12.2018 - 

I think that the thing that should be fixed is adding/changing/deleting passwords without reloading the page.
It's easy to do, and looks better for users.
=======
11.12.2018 -

I think that the thing that should be fixed is adding/changing/deleting passwords without rel$
It's easy to do, and looks better for users.

>>>>>>> 6b1173a87e78032dfd05655f05c527e8ffc662c9
