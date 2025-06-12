git clone https://github.com/alizayadahmadriyaz/StreamTube.git

Create virtual environment
source env/bin/activate 

Install dependencies
pip install -r requirements.txt

Database setup

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

Frontend Setup

cd final_frontend

Install dependencies

npm install


Start Backend Server
python manage.py runserver
Backend will be available at: http://localhost:8000

cd final_frontend
npm start
Frontend will be available at: http://localhost:3000


