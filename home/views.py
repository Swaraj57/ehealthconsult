from django.shortcuts import render, HttpResponse
from .forms import heartform,diabetesform
import joblib
# Create your views here.

def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

def main(request):
    return render (request, 'main.html')

def covid(request):
    return render (request, 'covidchecker.html')

def hospital(request):
    return render (request, 'hospital-locator.html')

def pharmacy(request):
    return render (request, 'pharmacy-locator.html')

def medstore(request):
    return render (request, 'medstore.html')

def checkout(request):
    return render (request, 'checkout.html')

def confirmation(request):
    return render (request, 'confirmation-page.html')

def forgot(request):
    return render (request, 'forgot-pass.html')

def mobile(request):
    return render (request, 'mobile-app.html')

def faq(request):
    return render (request, 'faq.html')

def diabetes(request):
	result= None
	if request.method == 'POST':
		form=diabetesform(request.POST)
		if form.is_valid():
			a1= form.cleaned_data['Pregnancies']
			a2= form.cleaned_data['Glucose']
			a3= form.cleaned_data['Blood_Pressure']
			a4= form.cleaned_data['Skin_Thickness']
			a5= form.cleaned_data['Insulin']
			a6= form.cleaned_data['BMI']
			a7= form.cleaned_data['Diabetes_Pedigree_Function']
			a8= form.cleaned_data['Age']
			model=joblib.load('home/final_model_diabetes.joblib')
			try:
				result=model.predict([[a1,a2,a3,a4,a5,a6,a7,a8]])[0]
			except:
				result=5
	else:
		form = diabetesform()
	return render(request,'diabetes.html',{'form':form,'result':result})


def heart(request):
	result= None
	if request.method == 'POST':
		form=heartform(request.POST)
		if form.is_valid():
			a1= form.cleaned_data['age']
			a2= form.cleaned_data['Sex']
			a3= form.cleaned_data['Chest_Pain_Level']
			a4= form.cleaned_data['Blood_Pressure']
			a5= form.cleaned_data['Cholestoral']
			a6= form.cleaned_data['Blood_Sugar']
			a7= form.cleaned_data['ECG_Result']
			a8= form.cleaned_data['Maximum_Heart_Beat']
			a9= form.cleaned_data['Exercise_induced_Angina']
			a10= form.cleaned_data['Depression_level']
			a11= form.cleaned_data['Condition_During_Peak_Exercise']
			a12= form.cleaned_data['Result_of_Fluoroscopy']
			a13= form.cleaned_data['Thallium_Test']
			model=joblib.load('home/final_model_heart.joblib')
			try:
				result=model.predict([[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13]])[0]
			except:
				result=5

	else:
		form = heartform()
	return render(request,'heart.html',{'form':form,'result':result})
