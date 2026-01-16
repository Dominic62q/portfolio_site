from django.contrib import admin
from .models import Home, About, ContactMessage, Project, ProjectImage
# Register your models here.


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 3  # Number of empty image fields to show
    fields = ['image', 'caption']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'github_link', 'live_link']
    list_filter = ['created_at']
    search_fields = ['title', 'description']
    inlines = [ProjectImageInline]


admin.site.register(Home)
admin.site.register(About)
admin.site.register(ContactMessage)
admin.site.register(Project, ProjectAdmin)