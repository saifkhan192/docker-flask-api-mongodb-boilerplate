
# Docker, Flask, MongoDB, MYSQL, ReactJS and SwaggerUI Ready-to-use API Project Structure
[![Author](http://img.shields.io/badge/author-@saifkhan192-blue.svg)](https://www.linkedin.com/in/saifullah-khan-02318086/)

A ready-to-use boilerplate for REST API Development with Docker, Flask, MongoDB, MYSQL, ReactJS and SwaggerUI

## Features

-   Light-weight project
-   Basic Authentication, Register/Login pages (http://localhost/login, http://localhost/register)
-   Example endpoints. for example survey collection and user subscription
-   Admin section (http://localhost/admin/) with crud operations
-   Validations included
-   Email helper added just set `SMTP_ACCOUNT` and use
-   Mysql raw query + using second db examples are Included

-   Included Swagger Documenation
-   Two flavours of Swagger Documenation (http://localhost/api/docs1 and http://localhost/api/docs2)
-   Api Documenation is dynamic, just change application/doc/apidoc.yaml and refresh the doc page
-   Test cases with pytest
-   Added support to be deployed to heroku
-   Added make commands to build/run and bash into the containers
-   Vscode launch.json is included to do breakpoint debugging, see the details below 
-   To use the flask debugbar uncomment config `DEBUG_TB_PANELS` and `FLASK_DEBUG=TRUE`

-   TODO: JWT token authorization
-   TODO: Add some MYSQL crud and migrations
-   TODO: Include CORS
-   TODO: API collection for Postman.
-   TODO: Add celery queue for async jobs
-   TODO: Add social logins for example Google, Facebook etc



## Project  structure
```sh
├── application
│   ├── auth_app.py
│   ├── commands.py
│   ├── doc
│   │   ├── apidoc.json
│   │   └── apidoc.yaml
│   ├── exceptions.py
│   ├── flask_app.py
│   ├── flask_app.pyc
│   ├── fontend_app.py
│   ├── forms
│   │   └── auth_forms.py
│   ├── helper.py
│   ├── __init__.py
│   ├── migrations.py
│   ├── models
│   │   ├── admin_models.py
│   │   ├── auth.py
│   │   ├── __init__.py
│   │   └── models.py
│   ├── run_server.py
│   ├── schemas
│   │   ├── __init__.py
│   │   └── UserSchema.py
│   ├── seeders.py
│   ├── tasks
│   │   ├── __init__.py
│   │   └── user_tasks.py
│   ├── tests
│   │   ├── config.py
│   │   ├── conftest.py
│   │   ├── pytest.ini
│   │   ├── test_app.py
│   │   ├── test_subscriber.py
│   │   └── test_survey.py
│   └── wsgi.py
├── coverage
├── docker
│   ├── bash_history.log
│   ├── docker-compose.yml
│   ├── DockerfileApp
│   ├── DockerfileMysql
│   └── DockerfileNode
├── gist.gist
├── gunicorn_starter.sh
├── img
│   ├── Screenshot from 2020-12-10 19-20-16.png
│   ├── Screenshot from 2020-12-10 19-20-50.png
│   ├── Screenshot from 2020-12-10 19-21-38.png
│   └── Screenshot from 2020-12-10 19-35-50.png
├── Makefile
├── Procfile
├── react
│   ├── node_modules
│   ├── package.json
│   ├── package-lock.json
│   ├── src
│   │   ├── App.jsx
│   │   ├── containers
│   │   ├── index.jsx
│   │   └── services
│   │       └── Api.jsx
│   ├── web-dist
│   │   ├── bundle.js
│   │   └── bundle.js.map
│   ├── webpack.config.common.js
│   ├── webpack.config.dev.js
│   └── webpack.config.production.js
├── README.md
├── requirements.txt
├── runtime.txt
├── static
│   ├── dist
│   │   ├── bundle.js
│   │   └── bundle.js.map
│   ├── swaggerui
│   │   ├── css
│   │   │   └── swagger-ui.css
│   │   ├── img
│   │   │   ├── favicon-16x16.png
│   │   │   └── favicon-32x32.png
│   │   └── js
│   │       ├── swagger-ui-bundle.js
│   │       ├── swagger-ui.js
│   │       └── swagger-ui-standalone-preset.js
│   ├── swaggerui2
│   │   └── dist
│   │       ├── css
│   │       │   ├── api-explorer.css
│   │       │   ├── index.css
│   │       │   ├── print.css
│   │       │   ├── reset.css
│   │       │   ├── screen.css
│   │       │   ├── standalone.css
│   │       │   └── typography.css
│   │       ├── lib
│   │       │   ├── backbone-min.js
│   │       │   ├── bootstrap.min.js
│   │       │   ├── handlebars-2.0.0.js
│   │       │   ├── highlight.7.3.pack.js
│   │       │   ├── jquery-1.8.0.min.js
│   │       │   ├── jquery.ba-bbq.min.js
│   │       │   ├── jquery.slideto.min.js
│   │       │   ├── jquery.wiggle.min.js
│   │       │   ├── jsoneditor.js
│   │       │   ├── marked.js
│   │       │   ├── swagger-oauth.js
│   │       │   └── underscore-min.js
│   │       └── swagger-ui.min.js
│   └── theme-1
│       ├── css
│       │   ├── all.min.css
│       │   ├── landing_page_style.css
│       │   └── sb-admin-2.min.css
│       ├── images
│       │   └── landing_page
│       │       ├── 1.jpg
│       │       ├── 2.jpg
│       │       ├── 3.jpg
│       │       ├── 4.jpg
│       │       └── 5.jpg
│       └── js
│           ├── bootstrap.bundle.min.js
│           ├── jquery.easing.min.js
│           ├── jquery.min.js
│           └── sb-admin-2.min.js
└── templates
    ├── auth
    │   ├── layout.html
    │   ├── login.html
    │   ├── messages.html
    │   └── register.html
    ├── landing_page.html
    ├── react_page.html
    ├── swaggerui-theme1.html
    └── swaggerui-theme2.html

```

## Getting started

```make
git clone https://github.com/saifkhan192/docker-flask-api-mongodb-boilerplate.git
cd docker-flask-api-mongodb-boilerplate
make build && make run_app
```



## Deploy on Heroku

1. Create Heroku account for free (https://signup.heroku.com/
2. On the dashboard (https://dashboard.heroku.com/apps), select New -> Create new app:
<img src="./img/Screenshot from 2020-12-10 19-20-16.png" />

3. Goto "Settings" tab, then click "Reveal Config Vars" and add below env vars.
<img src="./img/Screenshot from 2020-12-10 19-35-50.png" />

4. Goto "Deply" tab on app details page and "Connect to GitHub", then select your github repository
<img src="./img/Screenshot from 2020-12-10 19-20-50.png" />

5. Now click "Deploy Branch" and after deploy is completed click "Open app" at top right
<img src="./img/Screenshot from 2020-12-10 19-21-38.png" />

Demo here:
https://docker-flask-api-mongodb.herokuapp.com/


## Debugging
-   In vscode add breakpoint at any line and press F5 to start listening by the debugger
-   Now refresh the page to stop the debugger at the breakpoint

## Tests
### Running  Test Cases

```bash
make run_tests
```

## Usefull Make Commands

```make
make follow_logs #show flask debug output
make bash_app #ssh into the app
make watch_reactjs_files #monitor reactjs files and compile as files changes
make refresh_app #recreate app if flask does not reload on files changes
```


## Bugs or improvements

Feel free to report any bugs or improvements. Pull requests are always welcome.
