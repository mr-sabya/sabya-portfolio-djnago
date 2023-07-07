from django.contrib import admin


from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class Project_Feature(admin.TabularInline):
    model = Project_Feature

class Project_image(admin.TabularInline):
    model = Project_image


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    inlines = (Project_Feature, Project_image)


class BlogCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'created_at']


    def get_ordering(self, request):
        return ['created_at']


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class Comment_reply(admin.StackedInline):
    model = Reply


class CommentAdmin(admin.ModelAdmin):
    inlines = [Comment_reply]
    list_display = ['name', 'get_blog', 'created_at']

    def get_blog(self, obj):
        return obj.blog
    get_blog.short_description = 'Blog'
    get_blog.admin_order_field = 'blog'

    def get_ordering(self, request):
        return ['created_at']
    


class Pricing_Options(admin.StackedInline):
    model = Pricing_Options


class PricingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    inlines = [Pricing_Options]


#user
admin.site.register(UserInfo)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Client)
admin.site.register(Type)
admin.site.register(Language)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Service)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Info)

admin.site.register(Brand)

admin.site.register(Feedback)

#blog
admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)

#pricing
admin.site.register(Pricing, PricingAdmin)