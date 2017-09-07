import datetime

from django.conf import settings
from django.db import models
from django.utils import timezone
#from django.forms import ModelForm

from django.contrib.auth.models import User

from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Question(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

@python_2_unicode_compatible
class Answers(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_label = models.CharField(max_length=200)
    answer_text = models.TextField()
    comment = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.answer_label
    #votes = models.IntegerField(default=0)

@python_2_unicode_compatible
class Upload(models.Model):
    pic = models.ImageField("Image", upload_to="images/")
    ### here is /dir/path/image/
    name_pic = models.CharField(max_length=200)
    upload_date=models.DateTimeField(auto_now_add =True)

    # title = models.CharField(max_length=255, blank=True)
    # file = models.FileField(upload_to='photos/')
    # uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_pic

#class UploadForm(ModelForm):
#    class Meta:
#        model = Upload
