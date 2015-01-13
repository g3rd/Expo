from django.contrib import admin
from slides.models import State, Presentation, Slide
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory


@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
    list_display = ('title', 'state', 'status', )
    list_display_links = ('title', )
    list_editable = ('state', 'status', )


@admin.register(State)
class StateAdmin(TreeAdmin):
    form = movenodeform_factory(State)


@admin.register(Slide)
class SlideAdmin(TreeAdmin):
    form = movenodeform_factory(Slide)
