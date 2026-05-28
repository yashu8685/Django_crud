from django.db import models

# Create your models here.

class Emp(models.Model):
        eid=models.IntegerField(unique=True)
        ename=models.CharField(max_length=20)
        esal=models.FloatField()
        eemail=models.EmailField()




# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/yashu8685/Django_crud.git
# git push -u origin main