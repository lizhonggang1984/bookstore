from django.db import models

class BookInfoManager(models.Manager):
    def all(self):
        books = super().all()
        books = books.filter(isDelete=False)
        return books

    def create_book(self,btitle,bpub_date):
        model_class = self.model
        book = model_class()
        book.btitle = btitle
        book.bpub_date = bpub_date
        book.save()
        return book

# Create your models here.
class BookInfo (models.Model):
    btitle=models.CharField(max_length=50,unique=True)
    bpub_date = models.DateField()
    bread=models.IntegerField(default=0)
    bcomment=models.IntegerField(default=0)
    # bprice=models.DecimalField(max_digits=10,decimal_places=2)
    isDelete = models.BooleanField(default=False)
    # book=models.Manager()
    objects = BookInfoManager()

    # @classmethod
    # def create_book(cls, btitle, bpub_date):
    #     '''添加一本图书'''
    #     # 创建一个cls类的对象
    #     obj = cls()
    #     obj.btitle = btitle
    #     obj.bpub_date = bpub_date
    #     # 添加进数据库
    #     obj.save()
    #     # 返回obj
    #     return obj
    class Meta:
        db_table = 'bookinfo'

class HeroInfo(models.Model):
    hname=models.CharField(max_length=50)
    hgender=models.BooleanField(default=False)
    hcomment=models.CharField(max_length=100,null=True,blank=True)
    # use foreign key to connect hero to one book (many to one)
    hbook=models.ForeignKey('BookInfo',on_delete=models.CASCADE)
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table = 'heroinfo'

class AreaInfo(models.Model):
    atitle=models.CharField(max_length=100)
    aParent=models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE)
