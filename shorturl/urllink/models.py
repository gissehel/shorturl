from django.db import models

# Create your models here.

class Link(models.Model):
    name = models.CharField(max_length=10,unique=True)
    url = models.CharField(max_length=1024)

    def __unicode__(self) :
        return "%s : [%s]" % (self.name, self.url)



