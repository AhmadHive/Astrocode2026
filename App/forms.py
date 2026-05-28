from django import forms
from .models import Team, Submission

class TeamSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-style'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-style'}))

    class Meta:
        model = Team
        fields = ['team_name', 'university', 'leader_name', 'member2_name', 
                  'member3_name', 'member4_name', 'email_1', 'email_2', 'phone_1', 'phone_2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['description', 'drive_link','challenge']