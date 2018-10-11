# __GB-INSTAGRAM__
[GB-instagram](www.gbinstagram.herokuapp.com)
 is an application that allows users to post their photos and other people with different profiles are able to comment on the picture and even like them.

### __prerequisites__
The app runs on django==1.11 and works with both bootstrap4
and runs currently on python3.6 ubuntu 16.04

### __installation__
For the application to work you need some basic installations.
1. install a virtualenv in your root folder
  * sudo apt-get install python3-pip
  * sudo pip3 install virtualenv
  * virtualenv venv
  *after the above process make sure you activate the virtual by writing source virtual/bin/activate*

2. To start a django app you have to install django e.g ***python3.6 -m pip install django==1.11***

3. Then start a django project  -  django-admin startproject projectname
4. Inside the django project start a django-app -  django-admin startapp appname
5. for more info please read the [django documentation](https://docs.djangoproject.com/en/2.1/releases/1.11/)

### __Emerging Errors__
1. ***Error:*** - No module named django. ***Soln:*** install django in this format *python3.6 -m pip install django==1.11*

2. ***Error:***  - Programming Error. ***soln:*** make sure you migrate your database after you make changes ***python3.6 manage.py makemigrations*** and then ***python3.6 manage.py migrate***

> ***__programming is prone to errors therfore make sure ou install everything required in the requirements.txt and you do this by typing *python3.6 pip install -r requirements.txt *__***
### __Running Tests__
> after passing in diferrent functions in this application, one has to write tests
> some of the functions include:

1. save_image() - Save an image to the database.
2. delete_image() - Delete image from the database.
3. update_caption() - Update image caption in the database.

***note tests have to be assigned in the tests.py module***

### __Technologies Used__
1. posgresql
2. django==1.11
3. python3.6
4. bootstrap4
5. javascript


### __Deployment to Heroku__
> for deployment in heroku please click on this link and follow the steps very keenly [deployment](https://www.codementor.io/jamesezechukwu/how-to-deploy-django-app-on-heroku-dtsee04d4)


### __Authors__
***BRIGHTON ASUMANI***
* For anyproblem please contact at asumanibrighton@gmail.com

### __Licence__
This project is licensed under the MIT License - see the LICENSE.md file for details
