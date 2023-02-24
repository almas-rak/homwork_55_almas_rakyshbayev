from django.contrib import admin

from TODO_app.models import TODO


# Register your models here.


class TODOAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'date_of_completion', 'is_deleted', 'at_deleted')
    list_editable = ('title', 'status', 'date_of_completion', 'is_deleted')


admin.site.register(TODO, TODOAdmin)
