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
###To load Fixtures
```
py manage.py loaddata AcidMeasurement.json Disease.json FlavorMeasurement.json FrostSensitivity.json GrowthHabit.json Location.json Precipitation.json Season.json StrengthMeasurement.json SugarMeasurement.json Temperature.json Variety.json YieldHabit.json Tree.json OrchardMeasurement.json DiseaseMeasurement.json LabMeasurement.json Image.json
```