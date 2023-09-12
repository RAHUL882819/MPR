from django import forms

class logininfo(forms.Form):
    username=forms.CharField(max_length=20)
    mail=forms.CharField(max_length=50,label="REGISTER YOUR EMAIL ID")
    password=forms.CharField(max_length=20)
    number=forms.CharField(max_length=10,label="ENTER PHONE NUMBER")
