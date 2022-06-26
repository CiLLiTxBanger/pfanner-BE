# start prod server
nginx starten
- `systemctl start/restart/status nginx.service`<br>
- `/etc/init.d/nginx start` <br>

wsgi starten
- `sudo uwsgi --emperor /etc/uwsgi/vassals --uid www-data --gid www-data`

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

### To start the server
```
.\env\Scripts\activate
py manage.py runserver
```
### To create migrations
```
python manage.py makemigrations
python manage.py migrate
```
###To load Fixtures - new
```
py manage.py loaddata Disease.json Location.json Variety.json Tree.json OrchardMeasurement.json DiseaseMeasurement.json LabMeasurement.json
```
db: pfannerobstgartendb
user: pfanner
pw: pfannerAdmin2022


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


Als File Sharing vom Cloud Server kann evtl auch: [Transfer.sh](https://github.com/dutchcoders/transfer.sh/) verwendet werden.