from django.db import models

#class Post(models.Model):
    #title = models.CharField(max_length=100)
    #content = models.TextField()
    #pub_date = models.DateTimeField(auto_now_add=True)

    #def __str__(self):
      #  return self.title


# Create your models here.

# class Social(models.Model):
#     website_url = models.CharField(max_length=255, null=True, blank=True)
#     facebook_url = models.CharField(max_length=255, null=True, blank=True)
#     instagram_url = models.CharField(max_length=255, null=True, blank=True)
#     twitter_url = models.CharField(max_length=255, null=True, blank=True)
#     github_url = models.CharField(max_length=255, null=True, blank=True)
#     linkedin_url = models.CharField(max_length=255, null=True, blank=True)
#
#     def __str__(self):
#         return self.website_url
    
    # Create your models here.

# class Social(models.Model):
#     website_url = models.CharField(max_length=255, null=True, blank=True)
#     facebook_url = models.CharField(max_length=255, null=True, blank=True)
#     instagram_url = models.CharField(max_length=255, null=True, blank=True)
#     twitter_url = models.CharField(max_length=255, null=True, blank=True)
#     github_url = models.CharField(max_length=255, null=True, blank=True)
#     linkedin_url = models.CharField(max_length=255, null=True, blank=True)
#
#     def __str__(self):
#         return self.website_url


from django.db import models

class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')




