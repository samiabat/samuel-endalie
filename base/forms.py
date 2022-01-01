from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Employer, User, Message, Freelancer, Job, Project, Level


class FreelancerForm(ModelForm):
    class Meta:
        model = Freelancer
        fields = '__all__'


class EmployerForm(ModelForm):
   class Meta:
        model = Freelancer
        fields = '__all__'
class LevelForm(ModelForm):
    class Meta:
        model = Level
        fields = '__all__'

        


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

class LoginForm(UserCreationForm):
    class  Meta:
        model = User
        fields = ['email' , 'password', 'password']
class LoginAsFreelancerForm(ModelForm):
    class Meta:
        model = Freelancer
        fields = ['email', 'password']
class JobForm(ModelForm): 
    class Meta:
        model = Job
        fields = '__all__'
class ProposalForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'