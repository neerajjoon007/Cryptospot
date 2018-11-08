# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from django.core.validators import URLValidator
#from django.contrib.contenttypes.fields import GenericRelation
#from star_ratings.models import Rating

# Create your models here
class Dashconf(models.Model):
	sidebar_image = models.ImageField(upload_to="Banners", null=True, blank=True)
	site_name = models.CharField(max_length=300 , null=True, blank=True)

	market_status = models.CharField(max_length=300 , null=True, blank=True)
	market_image = models.ImageField(upload_to="Banners", null=True, blank=True)


class Signels(models.Model):
	coin_name = models.CharField(max_length=300 , null=True, blank=True)
	symbol = models.CharField(max_length=10 , null=True, blank=True)
	signal_id = models.IntegerField(default=0, null=True, blank=True)
	buy =  models.CharField(max_length=200 , null=True, blank=True)
	sell =  models.CharField(max_length=200 , null=True, blank=True)
	stop_loss = models.CharField(max_length=200 , null=True, blank=True)

	def __str__(self):
		return str(self.coin_name)

class Exchange(models.Model):
	name = models.CharField(max_length=30)
	
	def __str__(self):
       		return self.name
		

class Coin_listings(models.Model):
	coin = models.CharField(max_length=300 , null=True, blank=True)
	cymbol = models.CharField(max_length=10 , null=True, blank=True)
	coin_id = models.IntegerField(default=0, null=True, blank=True)
	exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE, null=True)
	date = models.DateTimeField(default=datetime.now,blank=True,null=True, editable=False)

	def __str__(self):
		return self.coin

class Airdrop(models.Model):
	Coin_name =  models.CharField(max_length=300 , null=True, blank=True)
	logo = models.ImageField(upload_to="Banners", null=True, blank=True)
	value = models.IntegerField(blank=True, null=True)
	ratings = models.IntegerField(blank=True, null=True,) 	
	details = models.TextField(max_length=2000, null=True, blank=True )
	status = models.CharField(max_length=50 ,  null=True, choices=[('Active', 'Active'), ('Expired', 'Expired')])
#	ratings = GenericRelation(Rating, related_query_name='foos')
	
	def __str__(self):
		return self.Coin_name

class Shop(models.Model):
	item_name = models.CharField(max_length=300, null=True, blank=True )
	itempic =  models.ImageField(upload_to="Banners", null=True, blank=True)
	item_price = models.DecimalField(max_digits=10, decimal_places=2)
	item_url =   models.URLField(null=True, blank=True )

	def __str__(self):
		return self.item_name
