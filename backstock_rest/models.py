from django.db import models

class Photo(models.Model):
  tumblr_id = models.IntegerField()
  tumblr_url = models.CharField(max_length=160)
  src = models.CharField(max_length=160)
  tags = models.CharField(max_length=200)

  def __unicode__(self):
    return self.tumblr_url;
