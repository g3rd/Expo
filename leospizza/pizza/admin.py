from django.contrib import admin
from pizza.models import Pizza


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):

    def get_changeform_initial_data(self, request):
        return {'name': 'custom_initial_value'}


admin.site.site_header = "Leo's Pizza"
admin.site.site_title = "Leo's Pizza Administration"
admin.site.index_title = "Administer Leo's Pizza"
