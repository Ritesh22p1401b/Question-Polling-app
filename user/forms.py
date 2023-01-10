from django import forms
from .models import User
from django.core.exceptions import ValidationError  
from phonenumber_field.formfields import PhoneNumberField  



class CustomUserForm(forms.Form):
    username = forms.CharField(label='username', min_length=5, max_length=150)
    first_name = forms.CharField(label='First Name',max_length=150)  
    last_name = forms.CharField(label='Last Name',max_length=150)  
    email = forms.EmailField(label='email')
    phone_number=PhoneNumberField(region="IN")
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'phone_number','password1','password2')


    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return username  
  

    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError(" Email Already Exist")  
        return email  
  

    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Password don't match")  
        return password1  


    def save(self,**data):  
        user = User.objects.create(  
            username=self.data['username'],  
            email=self.data['email'],
            first_name=self.data['first_name'],  
            last_name=self.data['last_name'],  
            phone_number=self.data['phone_number']
        )
        user.set_password(self.data["password1"])
        user.save()
        return user
