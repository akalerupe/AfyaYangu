from tkinter import N
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class FoodItems(models.Model):
    """Model definition for storing food items a user wants in their profile"""
    food_item=models.CharField(max_length=50,null=False)
    food_quantity=models.PositiveSmallIntegerField(null=False,default=0)
    calories=models.FloatField(null=False)
    person_of=models.ForeignKey(User,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.food_item


class Profile(models.Model):
    """user data for tracking calories"""
    person_of=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    food_selected=models.ForeignKey(FoodItems,null=False,on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)
    total_calories = models.FloatField(default=0,null=True)
    date = models.DateField(auto_now_add = True)
    calorie_goal = models.PositiveIntegerField(default=0)
    all_food_selected_today = models.ManyToManyField(FoodItems,through='PostFood',related_name='inventory')

    def __str__(self):
        return str(self.person_of.username)


    def save(self,*args,**kwargs):
        if self.food_selected!=None:
            self.amount=(self.food_selected.calories/self.food_selected.quantity)
            self.calorie_count=self.amount*self.quantity
            self.total_calories=self.calorie_count +self.total_calories
            calories=Profile.objects.filter(person_of=self.person_of).last()
            PostFood.objects.create(profile=calories,food=self.food_selected,calorie_amount=self.calorie_count,amount=self.quantity)
            self.food_selected = None
            super(Profile, self).save(*args,**kwargs)

        else:
            super(Profile,self).save(*args,**kwargs)


class PostFood(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    food = models.ForeignKey(FoodItems,on_delete=models.CASCADE)
    calorie_amount = models.FloatField(default=0,null=True,blank=True)
    amount = models.FloatField(default=0)










