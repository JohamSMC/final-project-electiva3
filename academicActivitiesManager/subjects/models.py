from django.db import models


class TypeActivity(models.Model):
    id_activity = models.AutoField(primary_key=True)

    LOAN_TYPE_ACTIVITIES = (
        ("Pa", "Parcial"),
        ("Q", "Quicez"),
        ("T", "Taller"),
        ("E", "Expocision"),
        ("Pr", "Proyecto")
    )
    type_activity = models.CharField(
        max_length=2, choices=LOAN_TYPE_ACTIVITIES, blank=False, default="T",
        help_text="Tipo de actividad")


class Subject(models.Model):
    id_subject = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    teacher = models.CharField(max_length=50)
    grade = models.FloatField(default=0)
    date_created = models.DateTimeField()


class Activity(models.Model):
    id_activity = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    type_activity = models.ForeignKey(TypeActivity, on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,)
    state = models.BooleanField(default=False)
    grade = models.FloatField(default=0)
    date_created = models.DateTimeField()
    date_finished = models.DateTimeField()
