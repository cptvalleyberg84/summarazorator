# Deployment and Payment setup

- The app was deployed with [Heroku](https://www.heroku.com/).
- The database was made with [PostgreSQL from Code Institute](https://dbs.ci-dbs.net/).

- The app can be reached by the [link](https://summarazorator-f7c027b4c8d6.herokuapp.com/).

---

## Local deployment

1. Clone the repository.

    - ```git clone https://github.com/cptvalleyberg84/summarazorator```

2. Go to the ```summarazorator``` directory.

    - ```cd summarazorator```

3. Create a virtual environment.

    - ```python3 -m venv venv```

    - ```source venv/bin/activate```

4. Install all dependencies.

    - ```pip install -r requirements.txt```

5. Create a ```env.py``` file.

    - ```touch env.py```

6. Add the following lines to ```env.py```:

    - ```import os```
    - ```os.environ["DJANGO_SECRET_KEY"]``` = your secret key.
    - ```os.environ["DEVELOPMENT"]``` = "1" for developement or comment this line out for production.
    - ```os.environ["ALLOWED_HOSTS"]``` = your domain name.
    - ```os.environ["DATABASE_URL"]``` = your database url.
    - ```os.environ["CLOUDINARY_CLOUD_NAME"]``` = your cloudinary cloud name.
    - ```os.environ["CLOUDINARY_API_KEY"]``` = your cloudinary api key.
    - ```os.environ["CLOUDINARY_API_SECRET"]``` = your cloudinary api secret.

7. Create and migrate the database.


8. Create the superuser.

    - ```python manage.py createsuperuser```


9. Run the server.

    - ```python manage.py runserver```

10. Access the website by the link provided in terminal. Add ```/admin/``` at the end of the link to access the admin panel.

---

**The app is deployed to Heroku but Heroku has removed its free tier services from November 29 2022**

---

## Heroku Deployment


1. Create a Heroku account if you don't already have one.

2. Create a new app on Heroku.

    1. Go to the [Heroku dashboard](https://dashboard.heroku.com/apps).
    2. Click on the "New" button.
    3. Click on the "Create new app" button.
    4. Choose a name for your app.
    5. Choose a region.
    6. Click on the "Create app" button.

3. In your app, go to the "Settings" tab, press "Reveal Config Vars", and add the following config vars if they are not already set:

    1. ```ALLOWED_HOSTS``` = your heroku domain name.
    2. ```CLOUDINARY_CLOUD_NAME``` = the cloud name you used when creating your cloudinary account.
    3. ```CLOUDINARY_API_KEY``` = the api key you got when created your cloudinary account.
    4. ```CLOUDINARY_API_SECRET``` = the api secret you got when created your cloudinary account.
    5. ```CLOUDINARY_URL``` = the api chian of your api key and your api secret key and your cloud name you got when created your cloudinary account. 
    6. ```DJANGO_SECRET_KEY``` = the secret key you receive from django when creating new app stated at the top of settings.py, i moved it to env.py

5. In your app go to the "Deploy" tab.

    1. If it's already possible, connect your Heroku account to your GitHub account and then click on the "Deploy" button.
    2. If not, you need to copy the Heroku CLI command to connect your heroku app and your local repository.

        - ```heroku git:remote -a <your-heroku-app-name>```

6. Go to your local repository.

7. Login to your Heroku account in your terminal and connect your local repository to your heroku app.

    1. ```heroku login -i``` - Enter all your Heroku credentials it will ask for.
    2. Paste the command you copied from step 5 into your terminal.

8. Create Procfile.

    This project uses Gunicorn to ```web: gunicorn your_app_name.wsgi```

9. Create ```requirements.txt```. This can be done by running the following command:

    - ```pip freeze > requirements.txt```

10. Add and commit all changes.

11. Push your changes to GitHub.

    - ```git push```

12. Check your app's logs in heroku dashboard and ensure everything is working.


To get Cloudinary cloud name, API key, and API secret:

1. Go to the [Cloudinary website](https://cloudinary.com/).

2. Log in to your account or sign up if you don't have an account.

3. Go to the [Cloudinary dashboard](https://cloudinary.com/console/).

4. At the top of the page, you will see your cloud name, API key, and API secret.

5. To reveal API secret, hover over the API key container and click on the button that looks like an eye.

6. Copy these values and paste them into the config vars on Heroku and into your `env.py` file.

---