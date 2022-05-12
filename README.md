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





Setup auf Server:
1: Python3.8.10 installieren
2. sudo apt-get install -y python3-pip
3. sudo apt-get install -y python3-venv
4. wget https://github.com/CiLLiTxBanger/pfanner-BE/archive/main.tar.gz    anschließend entpacken
5. python3 -m venv env
6. . env/bin/activate
7. pip install -r requiremeents.txt

ZUM INSTALLIEREN VON MYSQLCLIENT
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential