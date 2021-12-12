# DrawGithubBoard
Allows to draw any image on your Github Board profile


Startup:

Terminal 1 (Django):
cd backend_app
pip install -r requirements.txt
./manage.py migrate
./manage.py runserver

Terminal 2 (Rqworker queue for integration with github and later to draw on board):
cd backend_app
./manage.py rqworker default

Terminal 3 (Flask and ML):
cd ml_app
python main.py


# Django Module:
Handle connection with Github
Saves User Drawings

# Frontend Module:
For now using django templates. TODO

# ML Module:
Implements recognition of letter that is currently drawn on grid.

![image](https://user-images.githubusercontent.com/38433235/145724259-c0024216-3f87-4a1a-bbdf-45f0892d9489.png)
![image](https://user-images.githubusercontent.com/38433235/145724271-6c6f0922-bfbd-4152-a17d-f5ea51b852b3.png)
![image](https://user-images.githubusercontent.com/38433235/145724278-7b9ff7ae-174a-4c6d-81a2-43dc8c819464.png)

# Flask Modeule:
Interface for communication between Django and ML
