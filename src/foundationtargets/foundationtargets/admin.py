from django.contrib import admin

from foundationtargets import models

class GeckoWidgetAdmin(admin.ModelAdmin):
    list_display = ('title',)

class DataPointInline(admin.TabularInline):
    model = models.DataPoint
    extra = 6

class DeterminantAdmin(admin.ModelAdmin):
    list_display = ('title', 'gecko_widget')
    inlines = (DataPointInline,)

class DataPointAdmin(admin.ModelAdmin):
    list_display = ('determinant', 'month', 'target', 'actual')

admin.site.register(models.GeckoWidget, GeckoWidgetAdmin)
admin.site.register(models.Determinant, DeterminantAdmin)
admin.site.register(models.DataPoint, DataPointAdmin)
