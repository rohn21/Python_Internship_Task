# Python_Internship_Task

Its a simple web application using Python-Django.The project involves creating a basic HTML/CSS web page with a header, navigation menu, main content area where I have generated quotes.

A Python web server is created using Django, to serve the page, handle GET requests, and include appropriate routing. 

Dynamic content is added using a Python function or route, and a form is created to collect user data. Data persistence is also incorporated, potentially storing submissions in a database.


## Tech Stack

**Backend:** Python

**Css and JS:** Bootstrap, Javascript

**Server:** Django


## Installation

1) Clone the project with git :

```bash
 git clone https://github.com/rohn21/Python_Internship_Task.git
```

2) Setup virtual environment :


( i ) Install virtual environment using pip ( if not already installed )

```bash
pip install virtualenv
```

( ii ) Create virtual environment 

```bash
virtualenv <environment_name>
```

( iii ) activate virtual environment 

```bash
<environment_name>\Scripts\activate
```

3) Install required packages


```bash
pip install -r requirements.txt
```
## Running the server

To start the server, run the following command

```bash
  cd webapp_task
```

```bash
 python manage.py runserver
```

Paste this url

```bash
 http://127.0.0.1:8000/index/
```
## Features

- I have generated random quotes for the body content.(using dictionary)

- For the Form handling excercise, navigate to 'Pages' tab on navbar and then User details

- It will redirect to collect user data form and after submitting the form it will redirect to another page for displaying user entered data.

