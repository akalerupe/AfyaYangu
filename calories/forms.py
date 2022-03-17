from django.forms import ModelForm
from django import forms
from .models import FoodItems,Profile
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 

class CreateUserForm(UserCreationForm):
    """Registering user form"""
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class SelectFoodItemForm(forms. ModelForm):
    """Selecting food consumed by the user form"""
    class Meta:
        model=Profile
        fields=('food_selected','quantity')

    def __init__(self,user,*args,**kwargs) -> None:
        super(SelectFoodItemForm, self).__init__(*args, **kwargs)
        self.fields['food_selected'].queryset = FoodItems.objects.filter(person_of=user)

class AddFoodForm(forms.ModelForm):
    """Adding food items  """
    class Meta:
        model = FoodItems
        fields = ('food_item','food_quantity','calories') 

class ProfileForm(forms.ModelForm):
    """Recording daily career goals """
    class Meta:
        model = Profile
        fields = ('calorie_goal',)