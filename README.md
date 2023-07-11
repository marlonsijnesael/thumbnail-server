# thumbnail-server
Proof of concept for a image server using Django REST API and Pillow. 

## Features:

- [x] Store images endpoint
- [x] Get images endpoint
- [x] Create thumbnails
- [x] Store thumbnails
- [x] Get thumbnails
- [ ] Add credentials / users
- [ ] Make thumbnail size variable
- [ ] Generate renditions on-demand at any size

## Example:
### Original:
![alt text](https://img.freepik.com/free-photo/beautiful-milky-way-night-sky_53876-139825.jpg?w=2000&t=st=1689100095~exp=1689100695~hmac=01e859dbcd61a5b97a6b10f97bdec977b77c937958d0a1ea12d798e35564c1b7)

### Thumbnail:
![Screenshot](beautiful-milky-way-night-sky_thumb.jpg)

## how to run

1. Create virtual env
2. Pip install -r requirements.txt
3. Postgresql: create database
4. Set Database url in settings.py
5. run: python manage.py migrate
6. run: python manage.py runserver
