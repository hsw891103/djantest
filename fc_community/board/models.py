from turtle import title
from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=128, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    writer = models.ForeignKey('fcuser.Fcuser', on_delete=models.CASCADE, verbose_name='작성자')
    reg_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')
    

    class Meta:
        db_table = 'fastcampus_board'
        verbose_name = '게시판'
        verbose_name_plural = '게시판'

    def __str__(self):
        return self.title # Fcuer 오브젝트 네임으로 반환되는걸 유저 네임으로 반환시킴