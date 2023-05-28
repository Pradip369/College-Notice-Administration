from django.contrib import admin
from college.models import Notice,Branch,Profile,Question

class NoticeAdmin(admin.ModelAdmin):
    list_display = ["subject", "cr_date","msg"]
    list_filter = ["cr_date"]
    search_fields = ["subject","msg"]
admin.site.register(Notice,NoticeAdmin)

admin.site.register(Branch)

admin.site.register(Profile)


class QuestioneAdmin(admin.ModelAdmin):
    list_display = ["subject", "cr_date"]
    list_filter = ["cr_date"]
    search_fields = ["subject","question"]
admin.site.register(Question,QuestioneAdmin)
