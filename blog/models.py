from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=100)
    pic=models.ImageField(upload_to='postpics',blank=True)
    content=models.TextField()
    date=models.DateTimeField(default=now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    approved=models.BooleanField(default=False)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})


#comments
class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    reply=models.ForeignKey('self',null=True,blank=True ,related_name='replies',on_delete=models.CASCADE)
    content=models.TextField()
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}.{}'.format(self.post.title,self.user.username)