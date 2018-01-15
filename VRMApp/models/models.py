from django.db import models
from django.utils import timezone
from django.db import connection


class MCode(models.Model):    
    MCodeSeq = models.AutoField(primary_key=True,verbose_name="M코드내부코드")
    MCodeNo = models.CharField(blank=True,null=True,max_length=20,verbose_name="M코드번호")
    MCodeName = models.CharField(blank=True,null=True,max_length=20,verbose_name="M코드명")
    Remark = models.CharField(blank=True,null=True,max_length=20,verbose_name="비고")
    RegDT = models.DateTimeField(default=timezone.now,editable=False,verbose_name="등록일시")
    RegUserSeq = models.ForeignKey('auth.User',null=True,on_delete=models.SET_NULL,related_name='+',editable=False,db_column="RegUserSeq",verbose_name="등록자")
    UptDT = models.DateTimeField(blank=True,null=True,editable=False,verbose_name="수정일시")
    UptUserSeq = models.ForeignKey('auth.User',null=True,on_delete=models.SET_NULL,related_name='+',editable=False,db_column="UptUserSeq",verbose_name="수정자")

    def __str__(self):
        return "%s" %(self.MCodeName)
                            #timezone.localtime(self.RegDT).strftime('%m/%d %H:%M'),
                            #timezone.localtime(self.UptDT).strftime('%m/%d %H:%M'))

    def save(self, *args, **kwargs):
        self.RegDT = self.RegDT
        self.UptDT = timezone.now()
        super(MCode, self).save(*args, **kwargs)

    class Meta:
        verbose_name="공통코드M"
        verbose_name_plural = "공통코드M"  

class DCode(models.Model):    
    DCodeSeq = models.AutoField(primary_key=True,verbose_name="D코드내부코드")
    DCodeName = models.CharField(blank=True,null=True,max_length=20,verbose_name="D코드명")
    MCodeSeq = models.ForeignKey(MCode,null=True,on_delete=models.SET_NULL,related_name='+',editable=False,db_column="MCodeSeq",verbose_name="M코드")
    Remark = models.CharField(blank=True,null=True,max_length=20,verbose_name="비고")
    RegDT = models.DateTimeField(default=timezone.now,editable=False,verbose_name="등록일시")
    RegUserSeq = models.ForeignKey('auth.User',null=True,on_delete=models.SET_NULL,related_name='+',editable=False,db_column="RegUserSeq",verbose_name="등록자")
    UptDT = models.DateTimeField(blank=True,null=True,editable=False,verbose_name="수정일시")
    UptUserSeq = models.ForeignKey('auth.User',null=True,on_delete=models.SET_NULL,related_name='+',editable=False,db_column="UptUserSeq",verbose_name="수정자")

    def __str__(self):
        return "%s %s" %(self.MCodeSeq,self.DCodeName)

    def save(self, *args, **kwargs):
        self.RegDT = self.RegDT
        self.UptDT = timezone.now()
        super(DCode, self).save(*args, **kwargs)

    class Meta:
        verbose_name="공통코드D"
        verbose_name_plural = "공통코드D"  

class Cust(models.Model):    
    CustSeq = models.AutoField(primary_key=True,verbose_name="거래처내부코드")
    CustNo = models.CharField(blank=True,null=True,max_length=20,verbose_name="거래처번호")
    CustName = models.CharField(blank=True,null=True,max_length=20,verbose_name="거래처명")
    CutFullName = models.CharField(blank=True,null=True,max_length=20,verbose_name="사업자거래처명")
    OwnerName = models.CharField(blank=True,null=True,max_length=20,verbose_name="대표자명")
    Remark = models.CharField(blank=True,null=True,max_length=20,verbose_name="비고")
    RegDT = models.DateTimeField(default=timezone.now,editable=False,verbose_name="등록일시")
    RegUserSeq = models.ForeignKey('auth.User',null=True,on_delete=models.SET_NULL,related_name='+',editable=False,db_column="RegUserSeq",verbose_name="등록자")
    UptDT = models.DateTimeField(blank=True,null=True,editable=False,verbose_name="수정일시")
    UptUserSeq = models.ForeignKey('auth.User',null=True,on_delete=models.SET_NULL,related_name='+',editable=False,db_column="UptUserSeq",verbose_name="수정자")

    def __str__(self):
        return "%s %s" %(self.CustNo,self.CustName)

    def save(self, *args, **kwargs):
        self.RegDT = self.RegDT
        self.UptDT = timezone.now()
        super(Cust, self).save(*args, **kwargs)

    class Meta:
        verbose_name="거래처"
        verbose_name_plural = "거래처"  

class Emp(models.Model):    
    EmpSeq = models.AutoField(primary_key=True,verbose_name="담당자내부코드")
    EmpNo = models.CharField(blank=True,null=True,max_length=20,verbose_name="담당자번호")
    EmpName = models.CharField(blank=True,null=True,max_length=20,verbose_name="담당자명")
    WorkDept = models.CharField(blank=True,null=True,max_length=20,verbose_name="근무부서")
    WorkCompany = models.ForeignKey(Cust,null=True,on_delete=models.SET_NULL,related_name='+',editable=False,db_column="WorkCompany",verbose_name="소속")
    Remark = models.CharField(blank=True,null=True,max_length=20,verbose_name="비고")
    RegDT = models.DateTimeField(default=timezone.now,editable=False,verbose_name="등록일시")
    RegUserSeq = models.ForeignKey('auth.User',null=True,on_delete=models.SET_NULL,related_name='+',editable=False,db_column="RegUserSeq",verbose_name="등록자")
    UptDT = models.DateTimeField(blank=True,null=True,editable=False,verbose_name="수정일시")
    UptUserSeq = models.ForeignKey('auth.User',null=True,on_delete=models.SET_NULL,related_name='+',editable=False,db_column="UptUserSeq",verbose_name="수정자")

    def __str__(self):
        return "%s %s" %(self.EmpNo,self.EmpName)

    def save(self, *args, **kwargs):
        self.RegDT = self.RegDT
        self.UptDT = timezone.now()
        super(Emp, self).save(*args, **kwargs)

    class Meta:
        verbose_name="사원"
        verbose_name_plural = "사원"  

class Item(models.Model):    
    ItemSeq = models.AutoField(primary_key=True,verbose_name="품목내부코드")
    SerialNo = models.CharField(unique=True,max_length=20,verbose_name="SerialNo")
    HWSerialNo = models.CharField(blank=True,null=True,max_length=20,verbose_name="HWSerialNo")
    ItemTypeSeq = models.ForeignKey(DCode,null=True,on_delete=models.SET_NULL,related_name='+',db_column="ItemTypeSeq",verbose_name="장비종류")
    ModelSeq = models.ForeignKey(DCode,null=True,on_delete=models.SET_NULL,related_name='+',db_column="ModelSeq",verbose_name="모델")
    MacAddr = models.CharField(blank=True,null=True,max_length=20,verbose_name="MAC")
    Remark = models.CharField(blank=True,null=True,max_length=20,verbose_name="비고")
    RcvDate = models.DateTimeField(blank=True,null=True,verbose_name="수령일시")
    RcvEmpSeq = models.ForeignKey(Emp,null=True,on_delete=models.SET_NULL,related_name='+',db_column="RcvEmpSeq",verbose_name="수령자")
    RegDT = models.DateTimeField(default=timezone.now,editable=False,verbose_name="등록일시")
    RegUserSeq = models.ForeignKey('auth.User',null=True,on_delete=models.SET_NULL,related_name='+',editable=False,db_column="RegUserSeq",verbose_name="등록자")
    UptDT = models.DateTimeField(blank=True,null=True,editable=False,verbose_name="수정일시")
    UptUserSeq = models.ForeignKey('auth.User',null=True,on_delete=models.SET_NULL,related_name='+',editable=False,db_column="UptUserSeq",verbose_name="수정자")

    def __str__(self):
        return "%s %s" %(self.SerialNo,self.ModelSeq)

    def save(self, *args, **kwargs):
        self.RegDT = self.RegDT
        self.UptDT = timezone.now()
        super(Item, self).save(*args, **kwargs)

    class Meta:
        verbose_name="품목"
        verbose_name_plural = "품목"  

class WH(models.Model):    
    WHSeq = models.AutoField(primary_key=True,verbose_name="창고내부코드")
    WHNo = models.CharField(blank=True,null=True,max_length=20,verbose_name="창고번호")
    WHName = models.CharField(blank=True,null=True,max_length=20,verbose_name="창고명")
    Remark = models.CharField(blank=True,null=True,max_length=20,verbose_name="비고")
    RegDT = models.DateTimeField(default=timezone.now,editable=False,verbose_name="등록일시")
    RegUserSeq = models.ForeignKey('auth.User',null=True,on_delete=models.SET_NULL,related_name='+',editable=False,db_column="RegUserSeq",verbose_name="등록자")
    UptDT = models.DateTimeField(blank=True,null=True,editable=False,verbose_name="수정일시")
    UptUserSeq = models.ForeignKey('auth.User',null=True,on_delete=models.SET_NULL,related_name='+',editable=False,db_column="UptUserSeq",verbose_name="수정자")

    def __str__(self):
        return "%s %s" %(self.WHNo,self.WHName)

    def save(self, *args, **kwargs):
        self.RegDT = self.RegDT
        self.UptDT = timezone.now()
        super(WH, self).save(*args, **kwargs)

    class Meta:
        verbose_name="창고"
        verbose_name_plural = "창고"  


class Contents(models.Model):    
    ContentsSeq = models.AutoField(primary_key=True,verbose_name="영화내부코드")
    ContentsNo = models.CharField(blank=True,null=True,max_length=20,verbose_name="영화번호")
    ContentsName = models.CharField(unique=True,max_length=50,verbose_name="제목")
    ContentsEngName = models.CharField(blank=True,null=True,max_length=50,verbose_name="영문제목")
    RegNo = models.CharField(blank=True,null=True,max_length=20,verbose_name="영등위등록번호")
    PlayRate = models.CharField(blank=True,null=True,max_length=20,verbose_name="상영등급")
    MakerSeq = models.ForeignKey(Cust,blank=True,null=True,on_delete=models.SET_NULL,related_name='+',db_column="MakerSeq",verbose_name="제작사")
    Director = models.CharField(blank=True,null=True,max_length=20,verbose_name="감독")
    MainActors = models.CharField(blank=True,null=True,max_length=20,verbose_name="주연배우")
    FileName = models.CharField(blank=True,null=True,max_length=20,verbose_name="파일명")
    Remark = models.CharField(blank=True,null=True,max_length=20,verbose_name="비고")
    RegDT = models.DateTimeField(default=timezone.now,editable=False,verbose_name="등록일시")
    RegUserSeq = models.ForeignKey('auth.User',null=True,on_delete=models.SET_NULL,related_name='+',editable=False,db_column="RegUserSeq",verbose_name="등록자")
    UptDT = models.DateTimeField(blank=True,null=True,editable=False,verbose_name="수정일시")
    UptUserSeq = models.ForeignKey('auth.User',null=True,on_delete=models.SET_NULL,related_name='+',editable=False,db_column="UptUserSeq",verbose_name="수정자")



    def __str__(self):
        return "%s %s" %(self.ContentsNo,self.ContentsName)

    def save(self, *args, **kwargs):
        self.RegDT = self.RegDT
        self.UptDT = timezone.now()
        super(Contents, self).save(*args, **kwargs)

    class Meta:
        verbose_name="영화"
        verbose_name_plural = "영화"  


