from django.db import models

# Create your models here.
class AccessLog(models.Model):
    class Meta:
        db_table = 'AccessLog'
    
    created_at = models.DateTimeField('접속 시간', auto_now_add=True)
    # updated_at = models.DateTimeField('수정 시간', auto_now=True)
    location = models.CharField('접속 경로', max_length=256)
        
    def __str__(self):
        return f'{self.created_at}  {self.location}'
    