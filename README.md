# Flask-Web-Application
This repository is a full facebook flask application ready to be edited and published


# Tools you will need for this project
 
  1) You need to have python installed
  
      https://www.python.org/downloads/
      Download a version 3.x 
  
  2)  A virtual environment
  
      here is already a virtual environment created (virtual folder), but you can create yours if you want:
      to create your own virtual environment use the command bellow
      > python –m venv "your virtual env folder name"
      
      then activate the virtual environment with the following command:
      > \virtual\Scripts\activate.bat
      
      your terminal will look like :
      (virtual) >
      
   
  3) Flask
    
    you can install flask using pip included in python (>=3.4)
    > pip install flask
    
  4) A database and an ORM
     
     For this project, Sqlite is used but you can use another database, but dont forget to change it in the config.py
     for interpretation of queries, I used Flask_sqlalchemy
     You can download sqlite here ---> https://www.sqlite.org/download.html
     extract it in the same folder with your facebookApp
     flask_sqlalchemy can be installed with pip:
     > pip install flask_sqlalchemy
     
To test if the communication with database is ok type these commands:
      > export FLASK_APP='run.py'
      > flask shell
    on windows:
      > set FLASK_APP=run.py
      > flask shell
      
To run the application 
      > python run.py
      


Any proposition? you can contribute
any question? you can contact me: thierrynjike14@gmail.com
i will try to answer as soon as possible
    
