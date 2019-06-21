from django.db import models


# Create your models here.


# add this
class Backend(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title
