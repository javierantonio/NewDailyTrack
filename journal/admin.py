from django.contrib import admin

from journal.models import Journal


# Register your models here.

class JournalAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'content', 'isStarred', 'created_at', 'updated_at')
    list_display_links = ('id', 'title')


admin.site.register(Journal)
