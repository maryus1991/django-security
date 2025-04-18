from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3


# User creation form
User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    captcha = ReCaptchaField(widget=ReCaptchaV3,
        public_key='6Le-cBgrAAAAAMtouFjnBb5VDM7wwWpyhBw9Rs18',
        private_key='6Le-cBgrAAAAAHYlSktNAuSUYmOKDuvRpAFN1-5-'
    )