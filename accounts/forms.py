#コード追加（5-6（P.205））
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm) :
  class Meta :
    model = User
    fields = ('username',)
