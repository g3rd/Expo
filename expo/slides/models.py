from __future__ import unicode_literals
from django.core.validators import MinValueValidator
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from matplotlib.colors import rgb2hex
from model_utils import Choices
from model_utils.models import TimeStampedModel, StatusModel
from seaborn import light_palette
from slides.utils import get_templates
from treebeard.mp_tree import MP_Node


class PublicPresentationManager(models.Manager):
    def get_queryset(self):
        return super(PublicPresentationManager, self).get_queryset().exclude(status=Presentation.STATUS.draft)


class DraftPresentationManager(models.Manager):
    def get_queryset(self):
        return super(PublicPresentationManager, self).get_queryset().filter(status=Presentation.STATUS.draft)


@python_2_unicode_compatible
class State(MP_Node):
    name = models.CharField(_('title'), max_length=140)
    order = models.IntegerField(_('order'), default=0)
    is_default_state = models.BooleanField(_('is default state'), default=False)
    node_order_by = ['order']

    def __str__(self):
        if self.is_default_state:
            return "{}*".format(self.name)
        return self.name

    class Meta:
        verbose_name = _('state')
        verbose_name_plural = _('states')


@python_2_unicode_compatible
class Presentation(TimeStampedModel, StatusModel):

    STATUS = Choices(
        ('draft', _('draft')),
        ('published', _('published')),
        ('archived', _('archived')),
    )

    title = models.CharField(_('title'), max_length=140)
    slug = models.SlugField(_('slug'), max_length=140, unique=True)
    description = models.TextField(_('description'), blank=True, null=True)
    state = models.ForeignKey(State)
    template_path = models.CharField(_('template'), max_length=1024, default="slides/reveal.html")

    objects = models.Manager()
    drafts = DraftPresentationManager()
    published = PublicPresentationManager()

    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        if self.status == Presentation.STATUS.draft:
            return ('draft_presentation', (), {'slug': self.slug, })
        return ('presentation', (), {'slug': self.slug, })

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Presentation, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('presentation')
        verbose_name_plural = _('presentations')


@python_2_unicode_compatible
class Slide(MP_Node, TimeStampedModel):

    TEMPLATE_CHOICES = [(x, _(y)) for x, y in get_templates()]

    presentation = models.ForeignKey(Presentation)

    title = models.CharField(_('title'), max_length=140)
    slug = models.SlugField(_('slug'), max_length=140, editable=False)
    votable = models.BooleanField(_('is votable'), default=True)
    sms_value = models.CharField(_('sms value'), max_length=12, blank=True, null=True)
    votes = models.IntegerField(_('votes'), default=1, validators=[MinValueValidator(1)])
    color = models.CharField(_('color'), max_length=6, help_text=_('hex value'), blank=True, null=True)

    slide_path = models.CharField(_('template'), max_length=1024, choices=TEMPLATE_CHOICES, blank=True, null=True)
    visible_states = models.ManyToManyField(State, verbose_name=_('visible states'), blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Slide, self).save(*args, **kwargs)

    def _get_parent_colorset(self):
        parent = self.get_parent(update=True)
        if parent.color:
            return light_palette('#{}'.format(parent.color), reverse=True)
        if parent.is_root():
            return light_palette('#5d2989', reverse=True)
        return parent._get_parent_colorset()

    def processed_color(self):
        if self.color:
            return "#{}".format(self.color)
        if self.is_root():
            return '#5d2989'
        colorset = self._get_parent_colorset()
        return rgb2hex(colorset[self.depth - 1])

    def to_jsonable_python_object(self):
        json = {}
        json['id'] = self.id
        json['name'] = self.title
        json['votable'] = self.votable
        json['sms_value'] = self.sms_value
        json['size'] = self.votes
        if self.get_children_count() > 0:
            json['children'] = []
            for child in self.get_children().filter(visible_states__in=State.objects.filter(name='voting')):
                json['children'].append(child.to_jsonable_python_object())
        json['color'] = self.processed_color()
        return json

    class Meta:
        verbose_name = _('slide')
        verbose_name_plural = _('slides')
