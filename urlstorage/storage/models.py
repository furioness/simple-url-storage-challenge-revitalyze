from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()

class URL(models.Model):
    user = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, related_name="urls"
    )
    url = models.URLField()

    class Meta:
        unique_together = ('user', 'url',)
