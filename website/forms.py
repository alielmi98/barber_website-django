from django import forms
from captcha.fields import CaptchaField
from website.models import Contact,NewsLetter,Appointment



class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model=Contact
        fields='__all__'


class NewsLetterForm(forms.ModelForm):
    class Meta:
        model=NewsLetter
        fields='__all__'


class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields='__all__'