# Item Catalog

## Description
This project is part of [https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd0044](Udacity Full Stack Developer Nanodegree.)
Item Catalog is a web application that provides a list of items within a variety of categories and integrate third party user registration and authentication. Authenticated users have the ability to post, edit, and delete their own items. 

## How to run

- Install [https://www.vagrantup.com/downloads.html](Vagrant)
- Install [https://www.virtualbox.org/wiki/Downloads](VirtualBox)
- Install [https://git-scm.com/downloads](Git Bash)
- Download Vagrant configuration file from [https://github.com/udacity/fullstack-nanodegree-vm](fullstack-nanodegree-vm repository)
- Inside your VM directory run `vagrant up`
- Use `vagrant ssh` to login to VM 
- Navigate to the project directory
- Run `python database_setup.py` to setup the database_setup
- Run `python populate.py` to populate the database with data
- Run `application.py`
- Visit [http://localhost:8000](localhost:8000) to use the application

## Project overview

### Home page
Visiting `http://localhost:8000` show all categories and latest items
#img

### Edit item
`http://localhost:8000/category/<int:category_id>/items/<int:item_id>/edit`
### Login
`http://localhost:8000/login`
	ttps://developers.google.com/identity/images/btn_google_signin_dark_normal_web.png
### JSON endpoints
### Show all categories 
`http://localhost:8000/categories/JSON`

### Show items in a category
`http://localhost:8000//category/<int:category_id>/items/JSON`

### Show one item
`http://localhost:8000//category/<int:category_id>/items/<int:item_id>/JSON`

