from django.shortcuts import render, redirect
from .models import Food, Consume
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate

def register_user(request):
		if request.method=='POST':
			form=UserCreationForm(request.POST)
			if form.is_valid:
				form.save()
				username=form.cleaned_data.get('username')
				pswd=form.cleaned_data.get('password')
				user=authenticate(username=username,password=pswd)
				login(request,user)
				return redirect('index')
		else:
			form=UserCreationForm()
		return render(request,'register.html',{'form':form})

    	
@login_required
def index(request):
	
    if request.user.is_authenticated:
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user, food_consumed=consume)
        consume.save()
        foods = Food.objects.all()

    else:
        foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)

    return render(request, 'index.html', {'foods': foods, 'consumed_food': consumed_food})


def delete_consume(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('/')
    return render(request, 'delete.html')