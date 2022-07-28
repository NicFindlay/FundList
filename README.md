# Installation in Django Python



## Initial Setup

`yarn install`  						
-> This would install all the required dependencies in the node_modules folder.

`gulp`  						
-> 	Runs the project locally, starts the development server and watches for any changes in your code, including your HTML, javascript, sass, etc. The development server is accessible at http://localhost:8000.

`python -m venv fundlist`  		
-> Create Virtual Environment on linux & mac OS

`source fundlist/bin/activate`    
-> Activate Environment on Linux & mac OS

`pip3 install django`	__				
-> Install Django on linux & mac OS

`python3 manage.py runserver	`	  		
-> Run App on linux & mac OS


## Install few libraries

`pip install django-allauth`  
`pip install django-embed-video`  
`pip install django-crispy-forms`  
`pip install django-embed-video` 
`pip install django-otp`  
`pip install django-allauth-2fa`   


### Installing virtualenv	
 
`python3 -m pip install --user virtualenv`  
`python3 -m venv environment_name`  
`source environment_name/bin/activate`  

 

DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.#databaseservername#',  
        'NAME': 'Your Database Name',  
        'USER' : 'Database User Name',  
        'PASSWORD' : 'Your Password',  
        'HOST' : "Write down Host",  
        'PORT' : 'Write down port',   
    }  
}  

### To create superuser 

python3 manage.py createsuperuser  
python3 manage.py migrate  

### Database Changes
Change your models (in models.py).
Run `python manage.py makemigrations` to create migrations for those changes
Run `python manage.py migrate` to apply those changes to the database.

### To load Static Files:

Go to /setings.py  
-Add following command:-  
    
STATIC_URL = '/static/'  
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]  
STATIC_ROOT= os.path.join(BASE_DIR,'assets')  

Run Command In Terminal  
`python manage.py collectstatic`  

### Authentication Configuration

`pip3 install Django-Verify-Email`  

Goto settings.py of Main Directory
    
-SMTP CONFIGURATION  
	EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  
	EMAIL_HOST = 'smtp.gmail.com'  
	EMAIL_PORT = 587  
	EMAIL_USE_TLS = True  
	EMAIL_HOST_USER = '#####YOUR EMAIL ADDRESS########'  
	EMAIL_HOST_PASSWORD = '#####YOUR HOST Password########'  
	DEFAULT_FROM_EMAIL = '#####YOUR EMAIL ADDRESS########'  
	SERVER_EMAIL = '#####YOUR EMAIL ADDRESS########'  
	 
	 
# Run the project

`python3 manage.py runserver`