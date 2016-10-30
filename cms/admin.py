from django.contrib import admin

from .models import Answer


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent_id', 'text', 'keyword', )

    def parent_id(self):
        return unicode(self.parent.id) + self.text[:10]

admin.site.register(Answer, AnswerAdmin)