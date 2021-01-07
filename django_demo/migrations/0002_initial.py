from django.db import migrations, models
from django.contrib.auth.models import User


def create_users(apps, schema_editor):
    user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword', is_staff=True)
    user.save()
    user = User.objects.create_user('pienta', 'pienta@pienta.com', 'pientapassword', is_staff=True, is_superuser=True)
    user.save()


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('django_demo', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_users)
    ]
