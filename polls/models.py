from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class Question(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    questions = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    # created_at=models.DateTimeField(auto_now_add=True)
    # updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.questions
