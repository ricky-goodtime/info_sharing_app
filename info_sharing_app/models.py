from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Info(models.Model):
    # 情報共有の主題
    info_about_list = (
        (1, '業務連絡'),
        (2, '日程調整'),
        (3, '人事異動'),
        (4, 'その他'),
    )
    person = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    info_about = models.IntegerField(choices=info_about_list)
    text = models.TextField()
    shared_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    # コメントの目的
    comment_about_list = (
        (1, '補足'),
        (2, '意見'),
        (3, 'その他'),
    )
    info = models.ForeignKey(Info, on_delete=models.CASCADE, related_name='comments')
    person = models.CharField(max_length=20)
    comment_about = models.IntegerField(choices=comment_about_list)
    text = models.TextField()

    def __str__(self):
        return self.text
