from django.contrib import admin

from members.models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_joined', 'lifetime', 'honorary', 'seller')
    search_fields = ['name']
    list_filter = ('lifetime', 'honorary', 'seller')


# Register your models here.
admin.site.register(Member, MemberAdmin)
