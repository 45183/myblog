from django.contrib import admin

from blog.models import Post, Category

admin.site.register(Post)


# 카테고리 관리 클래스
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Category, CategoryAdmin)