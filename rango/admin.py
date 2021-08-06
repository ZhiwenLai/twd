from rango.models import *
from django.contrib import admin
from rango.models import UserProfile

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# Administrator interface customization of dogs information
class DogAdmin(admin.ModelAdmin):
    list_display = ('id','breedname','image','description','salesinfo','status')
    list_filter = (['breedname'])
    search_fields = (['breedname'])

    list_editable = ('description','image')

# Administrator interface customization of dogs sales information
class salesinfoAdmin(admin.ModelAdmin):
    list_display = ('id','image','breedname','description','color','gender','price','contactnumber')
    list_filter = (['breedname'])
    search_fields = (['breedname'])

    list_editable = ('image',)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'content', 'date')

class UserprifileAdmin(admin.ModelAdmin):
    list_display = ('user','website','picture')
admin.site.register(UserProfile)
admin.site.register(Dog,DogAdmin)
admin.site.register(salesinfo,salesinfoAdmin)
admin.site.register(comment,CommentAdmin)

# admin.site.register