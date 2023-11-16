from django.db import models

# Create your models here.

class Contact(models.Model):
	name=models.CharField(max_length=50)
	email=models.CharField(max_length=15)
	phone=models.CharField(max_length=10)
	subject=models.CharField(max_length=100)
		

class Course(models.Model):
	name=models.CharField(max_length=50)
	email=models.CharField(max_length=15)
	phone=models.CharField(max_length=10)
	coursename=models.CharField(max_length=10)

IMAGES_CATEGORY = (
	("memory", "memory"),
	("portrait", "portrait"),
	("wedding", "wedding"),
	("fashion", "fashion"),
	("travel", "travel"),
)

class Image(models.Model):
	image_category = models.CharField(max_length=10, choices=IMAGES_CATEGORY, null=True, blank=True)
	image = models.ImageField(upload_to='images/')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


class UpperSlider(models.Model):
	image_category = models.CharField(max_length=10, choices=IMAGES_CATEGORY, null=True, blank=True)
	image = models.ImageField(upload_to='images/')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


class MiddleSlider(models.Model):
	image_category = models.CharField(max_length=10, choices=IMAGES_CATEGORY, null=True, blank=True)
	image = models.ImageField(upload_to='images/')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

 
