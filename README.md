### Project Name
# The Motivational Minute
#### Author
### Stephen Ndele

## Description
The Motivational Minute is a platform that connects different kinds people who motivate each other in different articles. The Aim of the project is to make sure people share articles that give others hope in life. The only platform also allows users to add articles and motivate other too.

## Live Link (feel free to experiment all features)
[View Site](https://motivations.herokuapp.com/)

## Screenshots

![Alt text](/django1/assets/Screenshot-main.png?raw=true "Main Page")


![Alt text](/django1/assets/Screenshot2.png?raw=true "Motivationals")

## Setup Instructions:
### Requirements

##### 1. Clone the repository
Clone the the repository by running 

   ```bash
   git clone https://github.com/stephenndele/django-1.git
   ```
 or download a zip file of the project from github
 

Navigate to the project directory
```bash
cd django-1
```

##### 2. Create a virtual environment
 Install `Virtualenv` 

   ```prettier
   pip install virtualenv
   ```

To create a virtual environment named `virtual`, run

   ```prettier
   virtualenv virtual
   ```
To activate the virtual environment we just created, run

   ```bash
   source virtual/bin/activate
   ```

##### 3. Create a database or you can use sqlite provided by django framework
You'll need to create a new postgress database, Type the following command to access postgress
   ```bash
    $ psql
   ```
   Then run the following query to create a new database named ```your db``` 
   ```prettier
   $ CREATE DATABASE your db
   ```


#####  4.Install dependencies
To install the requirements from `requirements.txt` file,

   ```prettier
   pip install -r requirements.txt
   ```

#####  5.Create Database migrations
Making migrations on postgres using django

```prettier
python3 manage.py makemigrations articles
```

 
then run the command below;

 ```bash
 python3 manage.py migrate
 ```

##### 6.Run the app
To run the application on your development machine, 

    python3 manage.py runserver

### Running Tests
>To run tests;

    python3 manage.py test

## Technologies Used
* Django
* Python
* Html
* Css
* Javascript
* Bootstrap


## User stories
>As a user of the application I should be able to:

- [X] View different motivational articles.
- [X] Click on the article title and read more details of the article.
- [X] Can sign up to the application. 
- [X] Can sign in to the application.
- [X] Can also create a motivational articles and post for others to see
- [X] Can sign out of the application.



## Bugs
There are no know bugs at the moment

## License
[![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](http://opensource.org/licenses/MIT)
>MIT license &copy;  2019 Victor
 
## Collaboration Information
* Clone the repository
* Make changes and write tests
* Push changes to github
* Create a pull request

## Contacts
Reach me on:
>Email:  stephenndele093@gmail.com
