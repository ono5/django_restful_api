from django.db import models


class Hello(models.Model):
    message = models.CharField(max_length=250)

    class Meta:
        app_label = 'grpc_app'