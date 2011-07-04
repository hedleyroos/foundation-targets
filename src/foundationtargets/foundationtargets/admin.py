from django.contrib import admin

from foundationtargets import models

class GeckoWidgetAdmin(admin.ModelAdmin):
    list_display = ('title',)

class DataPointInline(admin.TabularInline):
    model = models.DataPoint
    extra = 6

class DeterminantAdmin(admin.ModelAdmin):
    list_display = ('title', 'gecko_widget', '_actions')
    inlines = (DataPointInline,)

    def _actions(self, obj):
        return '<a href="/gecko-xml/%s">View Gecko XML</a>' % obj.slug
    _actions.short_description = 'Actions'
    _actions.allow_tags = True

class DataPointAdmin(admin.ModelAdmin):
    list_display = ('determinant', 'month', 'target', 'actual')

admin.site.register(models.GeckoWidget, GeckoWidgetAdmin)
admin.site.register(models.Determinant, DeterminantAdmin)
admin.site.register(models.DataPoint, DataPointAdmin)
