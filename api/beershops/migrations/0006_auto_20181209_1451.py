# Generated by Django 2.1.2 on 2018-12-09 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beershops', '0005_beershopreview_score'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='beershopreview',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='beershopreview',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete='CASCADE', to='beershops.BeerShopReview'),
        ),
    ]
