from django.contrib import admin
from booktest.models import HeroInfo,BookInfo,AreaInfo
# Register your models here.

admin.site.register(HeroInfo)
admin.site.register(BookInfo)
admin.site.register(AreaInfo)