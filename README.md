# CrudRayed
crud rayed
- Clone repo dan venv
    - cd PYTHON_FOLDER
    - git clone https://github.com/ArisDjango/ArisHotelSite.git
    - cd ArisHotelSite
    - python -m venv venv
    - Set-ExecutionPolicy Unrestricted -Scope Process
    - & d:/TUTORIAL/PYTHON/CrudRayed/venv/Scripts/Activate.ps1

- Instalasi Django
    - python.exe -m pip install --upgrade pip
    - pip install django

- Struktur django
    - admin-conf
        - django-admin startproject core
        - rename 'core' menjadi 'crudApp'
        - cd crudApp
        - python manage.py migrate
        - python manage.py createsuperuser
        - python manage.py runserver
        - 127.0.0.1:8000/admin, login sebagai superuser --> tes koneksi django
    - App:
        - cd crudApp
        - python manage.py startapp theme 
        - python manage.py startapp books_cbv
        - python manage.py startapp books_fbv
        - python manage.py startapp books_fbv_user

            ```
                theme 
                books_cbv
                books_fbv
                books_fbv_user
            ```
    - static
        - copas jika sudah ada, jika belum buat folder --> theme/static/css:
        - folder css,scss,fonts,img,js
        - folder static_root

    - Membuat file requirements.txt
        - buat requirements.txt
        - pip freeze > requirements.txt
- Model
    - books_cbv/models.py
    - books_fbv/models.py
    - books_fbv_user/models.py
    - python manage.py makemigrations
    - python manage.py migrate

- Templates
    - theme/templates/
        - base.html
        - home.html
    - books_fbv/templates/books_cbv:
        - book_confirm_delete.html
        - book_form.html
        - book_list.html
    - books_cbv/templates/books_fbv
        - book_confirm_delete.html
        - book_form.html
        - book_list.html
    - books_cbv/templates/books_fbv_user
        - book_confirm_delete.html
        - book_form.html
        - book_list.html

- View
    - books_cbv/views.py, code:
    - books_fbv/views.py, code:
    - books_fbv_user/views.py, code:
    - theme/view.py, code:

        
- Routing url

- crudApp/core/urls.py, code:
- crudApp/
    - books_cbv/urls.py, code:
    - books_fbv/urls.py, code:
    - books_fbv_user/urls.py, code:

- Menampilkan semua field di admin panel
    - books_cbv/admin.py, code:
    - books_fbv/admin.py, code:
    - books_fbv_user/admin.py, code:
- 