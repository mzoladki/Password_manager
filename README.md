#password_manager

This is my recuitment task

## Instalation

In order to install project you have to follow few simple steps:

	1. ` git clone https://github.com/mzoladki/password_manager.git `
	2. ` python manage.py migrate `
	3. ` python manange.py runserver `

And up from this time you can easily have fun with project.

## Usage

Please remember to create account - go to ` /signup/ ` endpoint an fullfill forms.
Just after that proccess you can easily start using pass-manager.

## About

I strongly believe that apps that we're creating should just fit our needs.
An because of that I decided to:
	- use SQLite instead of Postgresql (for an example). Despite for the fact that postgresql is much stronger than sqlite, in this case using postgres is not needed.
	- use sometimes function based views instead of class-based views. When all that view has to do is render HTML file there is no need to take much fatter classes.
