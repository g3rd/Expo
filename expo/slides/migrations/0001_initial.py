# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('status', model_utils.fields.StatusField(default='draft', max_length=100, verbose_name='status', no_check_for_status=True, choices=[('draft', 'draft'), ('published', 'published'), ('archived', 'archived')])),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, verbose_name='status changed', monitor='status')),
                ('title', models.CharField(max_length=140, verbose_name='title')),
                ('slug', models.SlugField(unique=True, max_length=140, verbose_name='slug')),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('template_path', models.CharField(default='slides/reveal.html', max_length=1024, verbose_name='template')),
            ],
            options={
                'verbose_name': 'presentation',
                'verbose_name_plural': 'presentations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('path', models.CharField(unique=True, max_length=255)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('title', models.CharField(max_length=140, verbose_name='title')),
                ('slug', models.SlugField(verbose_name='slug', max_length=140, editable=False)),
                ('votable', models.BooleanField(default=True, verbose_name='is votable')),
                ('sms_value', models.CharField(max_length=12, null=True, verbose_name='sms value', blank=True)),
                ('votes', models.IntegerField(default=1, verbose_name='votes', validators=[django.core.validators.MinValueValidator(1)])),
                ('color', models.CharField(help_text='hex value', max_length=6, null=True, verbose_name='color', blank=True)),
                ('slide_path', models.CharField(blank=True, max_length=1024, null=True, verbose_name='template', choices=[(b'slides/content/webchad.html', 'webchad.html')])),
                ('presentation', models.ForeignKey(to='slides.Presentation')),
            ],
            options={
                'verbose_name': 'slide',
                'verbose_name_plural': 'slides',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.CharField(unique=True, max_length=255)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(max_length=140, verbose_name='title')),
                ('order', models.IntegerField(default=0, verbose_name='order')),
                ('is_default_state', models.BooleanField(default=False, verbose_name='is default state')),
            ],
            options={
                'verbose_name': 'state',
                'verbose_name_plural': 'states',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='slide',
            name='visible_states',
            field=models.ManyToManyField(to='slides.State', null=True, verbose_name='visible states', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='presentation',
            name='state',
            field=models.ForeignKey(to='slides.State'),
            preserve_default=True,
        ),
    ]
