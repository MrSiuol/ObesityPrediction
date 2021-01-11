REQUIEREMENTS
Python 3.6
Django 1.11.4
djangorestframework==3.4.3
pandas==0.18.1
scikit-learn==0.17.1
sklearn==0.0

IMPORTANT
-Si windows, les python et Django doivent etre dans les PATH afin de lancer les commande depuis le CMD.
-La commande "python manage.py runserver" permet de lancer le projet, il faut lancer la commande depuis le CMD.
-ll faut changer l'endroit ou se trouve le csv, dans views.py et apis.py changer : 
dfObesity = pd.read_csv("C:/Users/99loi/Desktop/ml_obesity/ml_obesity_project/app/static/app/csv/ObesityDataSet_raw_and_data_sinthetic.csv",sep=",") 
avec le bon path .

UTILISATION
Comment utiliser notre app web.
python manage.py runserver
puis aller localhost:8000/predict

Comment utiliser notre api "hors ligne".
python manage.py runserver
selectioner l'url + les variables.
http://localhost:8000/api/client/get/result/1/21/178/76/0/2/2/0/2/3/0/4/2/0/2/4/   ----> api que l'on a crée et qui renvois le resultat
(Gender,Age,Height,Weight,family_history_with_overweight,FAVC,FCVC,NCP,CAEC,SMOKE,CH2O,SCC,FAF,TUE,CALC,MTRANS)


