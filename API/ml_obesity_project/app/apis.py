from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponseRedirect,HttpResponse

from datetime import date

from django.views.decorators.csrf import csrf_exempt



from django.shortcuts import render
from django.conf import settings
# Create your views here.
from .models import *

#import projet
import numpy as np
import pandas as pd

from sklearn import svm
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import numpy as np




	

def client_get_result(request,Gender,Age,Height,Weight,family_history_with_overweight,FAVC,FCVC,NCP,CAEC,SMOKE,CH2O,SCC,FAF,TUE,CALC,MTRANS):

	dfObesity = pd.read_csv("C:/Users/Ykhil/Desktop/ml_obesity_project/app/static/app/csv/ObesityDataSet_raw_and_data_sinthetic.csv",sep=",")
	dfObesity["Height"]*=100
	title_cat = ["Gender", "family_history_with_overweight", "FAVC", "CAEC", "SMOKE","SCC","CALC","MTRANS","NObeyesdad"]
	title_cat2 = title_cat[:-1]
	df = dfObesity
	for i in title_cat2:
	  df[i]=df[i].astype("category").cat.codes
	"""df["NObeyesdad"]=df["NObeyesdad"].astype("category").cat.codes"""

	y=df["NObeyesdad"]
	X=df.drop("NObeyesdad",axis=1)
	X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.33)


	rfc = RandomForestClassifier(n_estimators=50, random_state=0)
	rfc.fit(X_train, y_train)
	y_pred = rfc.predict(X_test)


	predict = "Aucune prediction"

	int_features = [int(Gender),int(Age),int(Height),int(Weight),int(family_history_with_overweight),int(FAVC),int(FCVC),int(NCP),int(CAEC),int(SMOKE),int(CH2O),int(SCC),int(FAF),int(TUE),int(CALC),int(MTRANS)]

	final_features = [np.array(int_features)]
	prediction = rfc.predict(final_features)
	print(prediction)
	predict = prediction[0]
	

	return JsonResponse({"predict":predict})