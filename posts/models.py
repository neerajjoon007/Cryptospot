from django.db import models
from datetime import datetime
from django.core.validators import URLValidator
from slugify import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from dashboard.models import Exchange
# Create your models here.

class Post(models.Model):
#    category = models.ForeignKey(Category)
    created_at = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length = 100)
    content = models.TextField()
    url = models.URLField(max_length=250, blank=True)
    ups = models.IntegerField(default=0)
    down = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to="images",blank=True, null=True)
    slug = models.CharField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.title, instance=self, max_length=100)
        super(Post, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.title

class Signels(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE ,null=True)
    coin_name = models.CharField(max_length=300 , null=True, blank=True)
    symbol = models.CharField(max_length=10 , null=True, blank=True)
    title = models.CharField(max_length = 100, null=True, blank=True)
    signal_id = models.IntegerField(default=0, null=True, blank=True)
    buy =  models.CharField(max_length=200 , null=True, blank=True)
    sell =  models.CharField(max_length=200 , null=True, blank=True)
    stop_loss = models.CharField(max_length=200 , null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now,blank=True,null=True, editable=False)
    trade_time = models.CharField(max_length=100, null=True, blank=True)
    Exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE, null=True)
    values_in = models.CharField(max_length=50 ,  null=True, choices=[('BTC', 'BTC'), ('USD', 'USD')])
    like = models.ManyToManyField(User, blank=True, related_name='user_liked')
    dislike = models.ManyToManyField(User, blank=True, related_name='user_disliked')


    def __str__(self):
        return str(self.coin_name)

    @property
    def Total(self):
        ups = self.like.count()
        down = self.dislike.count()
        return ups - down




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    Propic = models.ImageField(upload_to="Banners/propics/", default="propics/default.png")
    telegram = models.CharField(max_length=50 , null=True, blank=True)
    twitter = models.CharField(max_length=50 , null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    
    # other fields...
    def __str__(self):
        return str(self.user)

    def get_following(self, current_user):
        followess = Follow.objects.filter(from_user__username=current_user)    
        following = []
        for i in followess:
            following.append(i.to_user)
        return following

    def get_followers_count(self ,current_user):
        followers_count = Follow.objects.filter(to_user__username=current_user).count()
        return followers_count


class Follow(models.Model):
    from_user = models.ForeignKey(User,
        on_delete=models.CASCADE,
        related_name='from_user',
        null=True
    )
    to_user = models.ForeignKey(User,
        on_delete=models.CASCADE,
        related_name='to_user',
         null=True
    )

    class Meta:
        unique_together=('from_user', 'to_user')

    def __str__(self):
        return '{} follows {}'.format(self.from_user, self.to_user)

    




@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()
