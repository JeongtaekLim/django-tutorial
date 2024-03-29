from django import forms

from polls.models import SignupAnswerer


class SignUpQuestionerForm(forms.Form):
    """
    Description:
     나이 ,성별, 이메일, 다니는 회사, 비밀번호 등을 기재
    """

    CHOICES = [('남', '남'), ('여', '여')]
    name = forms.CharField()
    sex = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    email = forms.EmailField()
    company = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class SignUpAnswererForm(forms.ModelForm):
    """
    Description:
     나이 ,성별, 이메일, 다니는 회사, 비밀번호 등을 기재
    """

    class Meta:
        model = SignupAnswerer
        fields = ["name", "sex", "company", "email", "password"]
