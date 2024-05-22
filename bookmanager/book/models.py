from django.db import models

# Create your models here.

class BookInfo(models.Model):
    name = models.CharField(max_length=32, unique=True)
    pub_time = models.DateTimeField(auto_now_add=True, null=True)
    readcount = models.IntegerField(verbose_name='阅读量', default=0)
    commentcount = models.IntegerField(verbose_name='评论量', default=0)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'BookInfo'
        verbose_name = '书籍管理'

    def __str__(self):
        return self.name

class PeopleInfo(models.Model):
    GENDER_CHOICE = (
        (0, '男'),
        (1, '女'),
    )
    name = models.CharField(max_length=32, unique=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=1)
    description = models.CharField(max_length=100, null=True)
    is_delete = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'PeopleInfo'
