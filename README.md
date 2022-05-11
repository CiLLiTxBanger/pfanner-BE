# pfanner-BE setup Guide

1. Create a virtual environment 
   "python3 -m venv env"

2. Activate the virtual environment 
   "source env/bin/activate"
   ```
   .\env\Scripts\activate
   ```

4. Install dependencies 
   "pip install -r requirements.txt"

5. Mac Users need to run 
   "brew install mysql" first

### To create migrations
```
python manage.py makemigrations
python manage.py migrate
```