from django.contrib import admin

from blog.models import Post


@admin.register(Post)
class ProductAdmin(admin.ModelAdmin):
    pass
    # list_display = ('id', 'name', 'price', 'category')
    # list_filter = ('category',)
    # search_fields = ('name', 'description')
