from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.
class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    state = models.BooleanField("State", default=True)
    create_date = models.DateField("Ceration_date",auto_now_add=True)
    modify_date = models.DateField("Modify date",auto_now=True)
    delete_date = models.DateField("Delete date",auto_now=True)
    history = HistoricalRecords(user_model="user.User")

    class Meta:
        abstract = True
        verbose_name ='DB Model base'
        verbose_name_plural = "DB Models base"

