# thumbnail-server
Proof of concept for a image server using Django. 

## Features:

- [x] Store images endpoint
- [x] Get images endpoint
- [x] Create thumbnails
- [x] Store thumbnails
- [x] Get thumbnails
- [ ] Add credentials / users
- [ ] Make thumbnail size variable
- [ ] Generate renditions on-demand at any size


## how to run

1. Create virtual env
2. Pip install -r requirements.txt
3. Postgresql: create database
4. Set Database url in settings.py
5. run: python manage.py migrate
6. run: python manage.py runserver
