from django.db import models

class TestSchedule(models.Model):
    s_no = models.IntegerField()
    batch_name = models.CharField(max_length=100)
    date = models.DateField()
    test_name = models.CharField(max_length=100)
    test_type = models.CharField(max_length=50)
    test_pattern = models.CharField(max_length=50)
    physics = models.TextField()
    chemistry = models.TextField()
    maths = models.TextField()