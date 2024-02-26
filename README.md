# product-review

## Installation

1. **First clone the repository in your system.**

   `https://github.com/swalih2233/product-review.git`

2. **Then start Virtual Environment within current Directory.**

   `python -m venv venv`

   `venv\Scripts\activate`

3. **Then install the dependencies from requirements.txt.**

   `pip install -r requirements.txt`


4. **Then change the PostgreSQL DB Details in settings.py**
   **If your dont have postgres you can use Sqlite3**


   **For sqlite3 Update DB Details in settings.py**

   DATABASES = { \
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
   } 

   **For PostgreSQL Update DB Details in settings.py**

   DATABASES = { \
      'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2', \
         'NAME': 'DB_NAME', \
         'USER':'DB_USER', \
         'PASSWORD':'DB_USER_PASSWORD', \
         'HOST':'localhost', \
         'PORT':'5432' \
      } \
   } 

5. **Then Apply Migrations.**

   `python manage.py makemigrations`

   `python manage.py migrate`

6. **Execute the manage.py file to runserver.**

   `python manage.py runserver`

7. **Use Postman to check api endpoints**

   `BASE_URL = http://127.0.0.1:8000/api/`

   `1. GET BASE_URL + product_details/`

      `SAMPLE RESPONSE`

      { \
         "status_code": 6000, \
        "data" : [product details]
        \
      } 

    
    `2. GET BASE_URL + list_products/`

      `SAMPLE RESPONSE`

      { \
         "status_code": 6000, \
          "data" : [list_products]
        \
      } 

    `3. GET BASE_URL + discount_category/`

      `SAMPLE RESPONSE`

      { \
         "status_code": 6000, \
          "data" : [discount_category]
        \
      } 

    `4. GET BASE_URL + search_product/`

      `SAMPLE RESPONSE`

      { \
         "status_code": 6000, \
          "data" : [search_product]
        \
      } 