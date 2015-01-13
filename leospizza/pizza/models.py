from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.html import format_html

class Pizza(models.Model):
    name = models.CharField(_('name'), max_length=12)
    price = models.DecimalField(_('price'), max_digits=5, decimal_places=2)

    def stylized_name(self):
        if self.price > 20:
            color = 'red'
        else:
            color = 'inherit'

        return format_html('<span style="color: {0};>{1}</span>', color, self.name)
    stylized_name.allow_tags = True
    stylized_name.admin_order_field = '-name'

    class Meta:
        verbose_name = _('pizza')
        verbose_name_plural = _('pizzas')
