# Generated by Django 2.0.6 on 2018-09-19 20:47

import codenerix.fields
import codenerix.lib.helpers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codenerix_products', '0044_family_url_external'),
    ]

    operations = [
        migrations.AddField(
            model_name='family',
            name='image_extra',
            field=codenerix.fields.ImageAngularField(blank=True, help_text='Se aconseja que sea una imagen superior a 200px transparente y en formato png o svg', max_length=200, null=True, upload_to=codenerix.lib.helpers.upload_path, verbose_name='Extra image'),
        ),
    ]
