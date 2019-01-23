Item-Catalog
Create a restaurant menu app where users can add, edit, and delete restaurants and menu items in the restaurants.

Setup and run the project
Prerequisites
Python 2.7
Vagrant
VirtualBox

How to Run
Install VirtualBox and Vagrant
Clone this repo
Unzip and place the Item Catalog folder in your Vagrant directory
Launch Vagrant
$ Vagrant up 
Login to Vagrant
$ Vagrant ssh
Change directory to /vagrant
$ Cd /vagrant

Initialize the database
$ Python database_setup.py

Populate the database with some initial data
$ Python menu.py

Launch application
$ Python project.py

Open the browser and go to http://localhost:5000

JSON endpoints
Returns JSON of all restaurants
/restaurants/JSON
Returns JSON of specific menu item
/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON
Returns JSON of menu
/restaurants/<int:restaurant_id>/menu/JSON
