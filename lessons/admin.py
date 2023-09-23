from django.contrib import admin

from lessons.models import Lesson, LessonView

admin.site.register(Lesson, admin.ModelAdmin)
admin.site.register(LessonView, admin.ModelAdmin)
