from django.contrib import admin


from .models import Category, Client, Language, Project, Type, Project_Feature
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class Project_Feature(admin.StackedInline):
    model = Project_Feature


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    inlines = [Project_Feature]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Client)
admin.site.register(Type)
admin.site.register(Language)
admin.site.register(Project, ProjectAdmin)