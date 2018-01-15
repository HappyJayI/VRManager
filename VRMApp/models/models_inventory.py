from django.db import models
from django.utils import timezone
from django.db import connection
from .models import *

def getPInvNo(self):
    strInOutDate = str(self.PInvDate).replace("-","")

    if self.PInvSeq == None:
        if self.PInvNo == "" :
            with connection.cursor() as cursor:
                cursor.execute( "SELECT max(PInvNo) as PInvNo FROM VRMApp_PhysicalInvM where PInvDate='%s'"%(str(self.PInvDate)))
                NewNo = cursor.fetchone()    

                if NewNo[0] != None:
                        self.PInvNo = strInOutDate + str(int(NewNo[0][-3:]) + 1).rjust(3,'0')
                else:
                    self.PInvNo = strInOutDate + '001'  


class PhysicalInvM(models.Model):    
    PInvSeq = models.AutoField(primary_key=True,verbose_name="재고실사내부번호")
    PInvNo = models.CharField(blank=True,null=True,max_length=20,verbose_name="재고실사번호")
    PInvDate = models.CharField(blank=True,null=True,max_length=20,verbose_name="재고실사일")
    PInvType = models.ForeignKey(DCode,null=True,on_delete=models.SET_NULL,related_name='+',editable=False,db_column="PInvType",verbose_name="재고실사종류")
    WHSeq = models.ForeignKey(WH,null=True,on_delete=models.SET_NULL,related_name='+',editable=False,db_column="WHSeq",verbose_name="창고")
    SrtTime = models.TimeField(blank=True,null=True,verbose_name="시작시간")
    EndTim = models.TimeField(blank=True,null=True,verbose_name="종료시간")
    WorkEmpSeq = models.ForeignKey(Emp,null=True,on_delete=models.SET_NULL,related_name='+',db_column="WorkEmpSeq",verbose_name="작업자")
    Remark = models.CharField(blank=True,null=True,max_length=20,verbose_name="비고")
    RegDT = models.DateTimeField(default=timezone.now,editable=False,verbose_name="등록일시")
    RegUserSeq = models.ForeignKey('auth.User',null=True,on_delete=models.SET_NULL,related_name='+',editable=False,db_column="RegUserSeq",verbose_name="등록자")
    UptDT = models.DateTimeField(blank=True,null=True,editable=False,verbose_name="수정일시")
    UptUserSeq = models.ForeignKey('auth.User',null=True,on_delete=models.SET_NULL,related_name='+',editable=False,db_column="UptUserSeq",verbose_name="수정자")

    def __str__(self):
        return "%s %s" %(self.PInvNo,self.PInvDate)

    def save(self, *args, **kwargs):
        self.RegDT = self.RegDT
        self.UptDT = timezone.now()
        #getPInvNo(self)
        super(PhysicalInvM, self).save(*args, **kwargs)

    class Meta:
        verbose_name="재고실사"
        verbose_name_plural = "재고실사"  

class PhysicalInvD(models.Model):    
    PInvSeq = models.ForeignKey(PhysicalInvM,null=True,on_delete=models.CASCADE,related_name='+',editable=False,db_column="PInvSeq",verbose_name="재고실사내부번호")
    PInvSerl = models.IntegerField(null=False,verbose_name="재고실사순번")
    ItemSeq = models.ForeignKey(Item,null=True,on_delete=models.SET_NULL,related_name='+',editable=False,db_column="ItemSeq",verbose_name="품목코드")
    SerialNo = models.ForeignKey(Item,to_field="SerialNo",null=True,on_delete=models.SET_NULL,related_name='+',editable=False,db_column="SerialNo",verbose_name="SerialNo")
    Qty = models.IntegerField(null=False,verbose_name="수량")
    Remark = models.CharField(blank=True,null=True,max_length=20,verbose_name="비고")
    RegDT = models.DateTimeField(default=timezone.now,editable=False,verbose_name="등록일시")
    RegUserSeq = models.ForeignKey('auth.User',null=True,on_delete=models.SET_NULL,related_name='+',editable=False,db_column="RegUserSeq",verbose_name="등록자")
    UptDT = models.DateTimeField(blank=True,null=True,editable=False,verbose_name="수정일시")
    UptUserSeq = models.ForeignKey('auth.User',null=True,on_delete=models.SET_NULL,related_name='+',editable=False,db_column="UptUserSeq",verbose_name="수정자")

    def __str__(self):
        return "%s %s" %(self.PInvSeq,self.PInvSerl)

    def save(self, *args, **kwargs):
        self.RegDT = self.RegDT
        self.UptDT = timezone.now()
        super(PhysicalInvD, self).save(*args, **kwargs)

    class Meta:
        verbose_name="재고실사D"
        verbose_name_plural = "재고실사D"  


class InOutM(models.Model):    
    InOutSeq = models.AutoField(primary_key=True,verbose_name="입출고내부코드")
    InOutNo = models.CharField(blank=True,null=True,max_length=20,verbose_name="입출고번호")
    InOutDiv = models.IntegerField(null=False,verbose_name="입출고구분")
    InOutDate = models.DateField(null=False,verbose_name="입출고일")
    InWHSeq = models.ForeignKey(WH,null=True,on_delete=models.SET_NULL,related_name='+',editable=False,db_column="InWHSeq",verbose_name="입고창고")
    OutWHSeq = models.ForeignKey(WH,null=True,on_delete=models.SET_NULL,related_name='+',editable=False,db_column="OutWHSeq",verbose_name="출고창고")
    RegDT = models.DateTimeField(default=timezone.now,editable=False,verbose_name="등록일시")
    RegUserSeq = models.ForeignKey('auth.User',null=True,on_delete=models.SET_NULL,related_name='+',editable=False,db_column="RegUserSeq",verbose_name="등록자")
    UptDT = models.DateTimeField(blank=True,null=True,editable=False,verbose_name="수정일시")
    UptUserSeq = models.ForeignKey('auth.User',null=True,on_delete=models.SET_NULL,related_name='+',editable=False,db_column="UptUserSeq",verbose_name="수정자")

    def __str__(self):
        return "%s %s" %(self.InOutNo,self.InOutDate)

    def save(self, *args, **kwargs):
        self.RegDT = self.RegDT
        self.UptDT = timezone.now()
        #getInOutNo(self)
        super(InOutM, self).save(*args, **kwargs)

    class Meta:
        verbose_name="입출고"
        verbose_name_plural = "입출고"  


class InOutD(models.Model):    
    InOutSeq = models.ForeignKey(InOutM,null=True,on_delete=models.CASCADE,related_name='+',editable=False,db_column="InOutSeq",verbose_name="입출고Seq")
    InOutSerl = models.IntegerField(null=False,verbose_name="입출고순번")
    ItemSeq = models.ForeignKey(Item,null=True,on_delete=models.SET_NULL,related_name='+',editable=False,db_column="ItemSeq",verbose_name="품목코드")
    SerialNo = models.ForeignKey(Item,to_field="SerialNo",null=True,on_delete=models.SET_NULL,related_name='+',editable=False,db_column="SerialNo",verbose_name="SerialNo")
    Qty = models.IntegerField(null=False,verbose_name="수량")
    Remark = models.CharField(blank=True,null=True,max_length=20,verbose_name="비고")
    RegDT = models.DateTimeField(default=timezone.now,editable=False,verbose_name="등록일시")
    RegUserSeq = models.ForeignKey('auth.User',null=True,on_delete=models.SET_NULL,related_name='+',editable=False,db_column="RegUserSeq",verbose_name="등록자")
    UptDT = models.DateTimeField(blank=True,null=True,editable=False,verbose_name="수정일시")
    UptUserSeq = models.ForeignKey('auth.User',null=True,on_delete=models.SET_NULL,related_name='+',editable=False,db_column="UptUserSeq",verbose_name="수정자")

    def __str__(self):
        return "%s %s" %(self.InOutSeq,self.InOutSerl)

    def save(self, *args, **kwargs):
        self.RegDT = self.RegDT
        self.UptDT = timezone.now()
        super(InOutD, self).save(*args, **kwargs)

    class Meta:
        verbose_name="입출고D"
        verbose_name_plural = "입출고D"  
        unique_together = (('InOutSeq', 'InOutSerl'),)
