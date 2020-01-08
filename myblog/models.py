from django.db import models
#from django.contrib.auth.models import User


# Create your models here.
#class UserProfile(models.Model):
#    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
#    description = models.CharField(max_length=100, default='')
#    city = models.CharField(max_length=100, default='')
#    website = models.URLField(default='')
#    phone = models.IntegerField(default=0)


#class Home(models.Model):
#    title = models.TextField(max_length=50, default='')
#    cover = models.ImageField(upload_to='images/home/')

#    def __str__(self):
#        return self.title

class Men(models.Model):
    title = models.TextField(max_length=50, default='')
    cover = models.ImageField(upload_to='images/mens/')

    def __str__(self):
        return self.title

class Women(models.Model):
    title = models.TextField(max_length=50, default='')
    cover = models.ImageField(upload_to='images/womens/')

    def __str__(self):
        return self.title

class Kid(models.Model):
    title = models.TextField(max_length=50, default='')
    cover = models.ImageField(upload_to='images/kids/')

    def __str__(self):
        return self.title

class Home_1(models.Model):
	title = models.TextField(max_length=50, default='upload 2000x800 size')
	cover = models.ImageField(upload_to='images/post/')

	def __str__(self):
		return self.title

class Home_2(models.Model):
        title = models.TextField(max_length=50, default='gender')
        cover = models.ImageField(upload_to='images/post/')

        def __str__(self):
                return self.title

