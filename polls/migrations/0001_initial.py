# Generated by Django 4.0.1 on 2022-01-14 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
                ('description', models.TextField()),
                ('date_start', models.DateField(auto_now_add=True)),
                ('date_finish', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(null=True)),
                ('answers', models.CharField(max_length=200, null=True)),
                ('poll', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='polls.poll')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('question_type', models.CharField(choices=[('text field', 'Text field'), ('choose one', 'Choose one'), ('choose many', 'Choose many')], default='text field', max_length=20)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='polls.poll')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='polls.question')),
            ],
        ),
    ]