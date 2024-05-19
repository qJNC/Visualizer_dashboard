from django.contrib import admin
from dashboard.models import visualize
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class VisualizerResource(resources.ModelResource):
    class Meta:
        model=visualize

class visualizerAdmin(ImportExportModelAdmin):
    resource_class = VisualizerResource

admin.site.register(visualize, visualizerAdmin)