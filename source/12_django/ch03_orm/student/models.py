from django.db import models

# Create your models here.

class Student(models.Model):  # 아무 설정하지 않으면 테이블이름은 '앱명_클래스명' - ex : student_student
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    major = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(default=0)
    grade = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.id} : {self.name} ({self.major}, {self.age}세, {self.grade}학년)"