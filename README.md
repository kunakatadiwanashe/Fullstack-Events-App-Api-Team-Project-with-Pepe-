# Fullstack-Events-App-Api-Team-Project-with-Pepe- [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-green.svg)](https://github.com/isakal/create-flask-app/pull/new/master)
Front end was done in react and backend with python

for the backend server, install the packages using pip install -r requirements.txt
to start the server in (env) mode

MS Windows: python -m venv env
Mac: python3 -m venv env

and activate env using 

Flask port of [create-react-app](https://facebook.github.io/create-react-app/) that is used for initializing project structure of your next application.

- [Creating an app](#creating-an-app) - How to create a new app.

Create Flask app works on macOS, Windows and Linux.
If something doesn't work, please [file an issue](https://github.com/isakal/create-flask-app/issues/new).
If you have questions, suggestions or need help, [feel free to open an issue](https://github.com/isakal/create-flask-app/issues/new).

## Quick overview 

```sh
pip install createflaskapp
create-flask-app my-app
cd my-app
# activate venv
python run.py
```
*(use correct version of [pip](https://pip.pypa.io/en/stable/) and [python](https://python.org/) according to your OS and python install)*
Then open [http://localhost:5000](http://localhost:5000) to see your app.
When you are ready to deploy to production, set environment variable `PRODUCTION` to  `True` on your server of choice, clone the project onto your server and spin it up.


## Creating an app

**You'll need to have Python 3.6 or higher on your local development machine** (but it's not required on the server).
To create a new app, you can run :

### bash
```sh
create-flask-app my-app 
```

### python
```sh
python -m create-flask-app my-app
```
It will create a directory called my-app inside the current folder.
Inside that directory, it will generate the initial project structure :
```
backend/
├──env
├── app.py
├── resources.py
├── routes.py   
│   
│   
├── requirements.txt  
└── 
```

No complicated configuration or folder structures, only the files you need to build and deploy your app.
Once the installation is done, you can open your project folder:
```sh
cd my-app
```
Inside the newly created project, you can run some commands:

### `source venv/bin/activate` or `.\venv\Scripts\activate`
Activates the virutal environment required for the project dependency isolation.

[Read more about venv.](https://https://docs.python.org/3/library/venv.html)  

### `pip install -r requirements.txt`
Installs libraries and dependencies listed in `requirements.txt` in active environment.

### `python run.py`
Starts the app in development mode. 
Open [http://localhost:5000](http://localhost:5000) to view it in browser.

The page will automatically reload if you make changes to the code. 
You will see errors in app reload or startup in the console.


## How to Update to New Versions?

Create-Flask-App can be simply upgraded using pip:

```sh
pip install createflaskapp --upgrade
# or
pip install createflaskapp -U
```

## What's Included?

Your environment after installing everything from `requirements.txt` will have everything you need to build simple but modern Flask app:
- Isolated Python environment with fully functional pip.
- [Flask](https://www.palletsprojects.com/p/flask/), lightweight WSGI web application framework.
- A live development server that warns about errors and exceptions.
- [Jinja](https://jinja.palletsprojects.com/en/2.10.x/) template engine that is very fast and has very similar syntax to python.
- [Click](https://click.palletsprojects.com/en/7.x/), composable command line interface toolkit.

Check out [this guide](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) for an overview of how these tools fit toghether.


## Prerequisites

### Install Node JS
Refer to https://nodejs.org/en/ to install nodejs

### Install create-react-app
Install create-react-app npm package globally. This will help to easily run the project and also build the source files easily. Use the following command to install create-react-app

```bash
npm install -g create-react-app
```
## Live Application URL

The Application is deployed in https://aditya-sridhar.github.io/simple-reactjs-app

Click on the link to see the application

## Cloning and Running the Application in local

Clone the project into local

Install all the npm packages. Go into the project folder and type the following command to install all npm packages

```bash
npm install
```

In order to run the application Type the following command

```bash
npm start
```

The Application Runs on **localhost:3000**

## Application design

#### Components

1. **Customers** Component : This Component displays a list of customers. This Component gets the data from a json file in assets folder

2. **CustomerDetails** Component : This Component Displays the details of the selected customer. This Component gets its data from a json file in assets folder as well. This Component is the Child Component of *Customers* Component

#### HTTP client

**axios** library is used to make HTTP Calls

#### URL

The application has just one url /customerlist which ties to *Customers* Component

## Resources

**create-react-app** : The following link has all the commands that can be used with create-react-app
https://github.com/facebook/create-react-app

**ReactJS** : Refer to https://reactjs.org/ to understand the concepts of ReactJS

**React Bootstrap** : Refer to https://react-bootstrap.github.io/getting-started/introduction/ to understand how to use React Bootstrap

