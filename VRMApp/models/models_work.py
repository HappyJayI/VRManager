from django.db import models
from django.utils import timezone
from django.db import connection
from .models import *

class EmpWorkPlan(models.Model):    
    WorkDate = models.DateField(null=False,verbose_name="근무일")
    EmpSeq = models.ForeignKey(Emp,null=True,on_delete=models.SET_NULL,related_name='+',db_column="EmpSeq",verbose_name="사원")
    StrDate = models.DateField(null=False,verbose_name="시작일")
    StrTime = models.TimeField(blank=True,null=True,verbose_name="시작시간")
    EndDate = models.DateField(null=False,verbose_name="종료일")
    EndTime = models.TimeField(blank=True,null=True,verbose_name="종료시간")
    WorkTime = models.FloatField(blank=True,null=True,verbose_name="계산근무시간")
    AppWorkTime = models.FloatField(blank=True,null=True,verbose_name="확정근무시간")
    Activity = models.CharField(blank=True,null=True,max_length=20,verbose_name="활동내역")
    Remark = models.CharField(blank=True,null=True,max_length=20,verbose_name="비고")
    RegDT = models.DateTimeField(default=timezone.now,editable=False,verbose_name="등록일시")
    RegUserSeq = models.ForeignKey('auth.User',null=True,on_delete=models.SET_NULL,related_name='+',editable=False,db_column="RegUserSeq",verbose_name="등록자")
    UptDT = models.DateTimeField(blank=True,null=True,editable=False,verbose_name="수정일시")
    UptUserSeq = models.ForeignKey('auth.User',null=True,on_delete=models.SET_NULL,related_name='+',editable=False,db_column="UptUserSeq",verbose_name="수정자")

    def __str__(self):
        return "%s %s" %(self.InOutNo,self.InOutDate)

    def save(self, *args, **kwargs):
        self.RegDT = self.RegDT
        self.UptDT = timezone.now()
        super(EmpWorkPlan, self).save(*args, **kwargs)

    class Meta:
        verbose_name="근무계획"
        verbose_name_plural = "근무계획"  
        unique_together = (('WorkDate','EmpSeq'),)

class EmpWorkRpt(models.Model):    
    WorkDate = models.DateField(null=False,verbose_name="근무일")
    EmpSeq = models.ForeignKey(Emp,null=True,on_delete=models.SET_NULL,related_name='+',db_column="EmpSeq",verbose_name="사원")
    StrDate = models.DateField(null=False,verbose_name="시작일")
    StrTime = models.TimeField(blank=True,null=True,verbose_name="시작시간")
    EndDate = models.DateField(null=False,verbose_name="종료일")
    EndTime = models.TimeField(blank=True,null=True,verbose_name="종료시간")
    WorkTime = models.FloatField(blank=True,null=True,verbose_name="계산근무시간")
    AppWorkTime = models.FloatField(blank=True,null=True,verbose_name="확정근무시간")
    Activity = models.CharField(blank=True,null=True,max_length=20,verbose_name="활동내역")
    Remark = models.CharField(blank=True,null=True,max_length=20,verbose_name="비고")
    RegDT = models.DateTimeField(default=timezone.now,editable=False,verbose_name="등록일시")
    RegUserSeq = models.ForeignKey('auth.User',null=True,on_delete=models.SET_NULL,related_name='+',editable=False,db_column="RegUserSeq",verbose_name="등록자")
    UptDT = models.DateTimeField(blank=True,null=True,editable=False,verbose_name="수정일시")
    UptUserSeq = models.ForeignKey('auth.User',null=True,on_delete=models.SET_NULL,related_name='+',editable=False,db_column="UptUserSeq",verbose_name="수정자")

    def __str__(self):
        return "%s %s" %(self.InOutNo,self.InOutDate)

    def save(self, *args, **kwargs):
        self.RegDT = self.RegDT
        self.UptDT = timezone.now()
        super(EmpWorkRpt, self).save(*args, **kwargs)

    class Meta:
        verbose_name="근무일지"
        verbose_name_plural = "근무일지"  
        unique_together = (('WorkDate','EmpSeq'),)


class PlayPlan(models.Model):    
    PlayDate = models.DateField(null=False,verbose_name="상영일")
    PlayOrder = models.IntegerField(null=False,verbose_name="회차")
    PlaySerl = models.IntegerField(null=False,verbose_name="영화")
    ContentsSeq = models.ForeignKey(Contents,null=True,on_delete=models.SET_NULL,related_name='+',db_column="ContentsSeq",verbose_name="영화")
    StrTime = models.TimeField(blank=True,null=True,verbose_name="시작시간")
    EndTime = models.TimeField(blank=True,null=True,verbose_name="종료일")
    Remark = models.CharField(blank=True,null=True,max_length=20,verbose_name="비고")
    RegDT = models.DateTimeField(default=timezone.now,editable=False,verbose_name="등록일시")
    RegUserSeq = models.ForeignKey('auth.User',null=True,on_delete=models.SET_NULL,related_name='+',editable=False,db_column="RegUserSeq",verbose_name="등록자")
    UptDT = models.DateTimeField(blank=True,null=True,editable=False,verbose_name="수정일시")
    UptUserSeq = models.ForeignKey('auth.User',null=True,on_delete=models.SET_NULL,related_name='+',editable=False,db_column="UptUserSeq",verbose_name="수정자")

    def __str__(self):
        return "%s %s" %(self.PlayDate,self.ContentsSeq)

    def save(self, *args, **kwargs):
        self.RegDT = self.RegDT
        self.UptDT = timezone.now()
        super(PlayPlan, self).save(*args, **kwargs)

    class Meta:
        verbose_name="상영계획"
        verbose_name_plural = "상영계획"  
        unique_together = (('PlayDate','PlayOrder','PlaySerl'),)


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="게시판"
        verbose_name_plural = "게시판"  