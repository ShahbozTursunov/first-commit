from django import forms
from .models import *

class RegFrom(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'
        
class OrderFrom(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        
class UpdateFrom(forms.ModelForm):
    class Meta:
        model = Register
        fields = ('ism', 'familiya', 'nick', 'card')
        

        
class User_listFrom(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'
        
class UserDeleterom(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'
        
class LogFrom(forms.ModelForm):
    class Meta:
        model = Register
        fields = ('ism', 'password')