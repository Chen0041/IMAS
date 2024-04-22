# Generated by Django 5.0.3 on 2024-03-31 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AutoAnswerTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('train_model_id', models.IntegerField()),
                ('status', models.CharField(max_length=1)),
                ('question', models.CharField(max_length=1024)),
                ('picture_path', models.CharField(blank=True, max_length=128, null=True)),
                ('answer', models.CharField(blank=True, max_length=1024, null=True)),
            ],
            options={
                'db_table': 'auto_answer_task',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=512)),
                ('data_format', models.CharField(max_length=20)),
                ('is_labeled', models.CharField(max_length=1)),
                ('is_single_case', models.CharField(max_length=1)),
                ('with_picture', models.CharField(max_length=1)),
                ('status', models.CharField(max_length=1)),
                ('dataset_path', models.CharField(blank=True, max_length=128, null=True)),
                ('after_train_dataset_path', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'db_table': 'dataset',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DeepLearningModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('category_id', models.IntegerField()),
                ('introduction', models.CharField(blank=True, max_length=1024, null=True)),
                ('article_title', models.CharField(blank=True, max_length=50, null=True)),
                ('article_url', models.CharField(blank=True, max_length=128, null=True)),
                ('code_url', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'db_table': 'deep_learning_model',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'department',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='KnowledgeGraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('disease_case_id', models.IntegerField()),
            ],
            options={
                'db_table': 'knowledge_graph',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ModelCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'model_category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('department_id', models.IntegerField()),
                ('content', models.CharField(max_length=1024)),
                ('picture_path', models.CharField(blank=True, max_length=128, null=True)),
                ('answer', models.CharField(blank=True, max_length=1024, null=True)),
                ('status', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'question',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SimilarCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('knowledge_graph_id', models.IntegerField()),
                ('similar_graph_id', models.IntegerField()),
            ],
            options={
                'db_table': 'similar_case',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SingleDiseaseCaseInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('dataset_id', models.IntegerField()),
                ('picture_path', models.CharField(blank=True, max_length=128, null=True)),
                ('disease', models.CharField(blank=True, max_length=128, null=True)),
                ('medicine', models.CharField(blank=True, max_length=128, null=True)),
                ('diagnosis', models.CharField(blank=True, max_length=128, null=True)),
                ('symptom', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'db_table': 'single_disease_case_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TrainModelTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('task_name', models.CharField(max_length=50)),
                ('dataset_id', models.IntegerField()),
                ('model_id', models.IntegerField()),
                ('epoch', models.IntegerField(blank=True, null=True)),
                ('batch_size', models.IntegerField(blank=True, null=True)),
                ('rnn_cell', models.CharField(blank=True, max_length=20, null=True)),
                ('embedding', models.CharField(blank=True, max_length=20, null=True)),
                ('constructor', models.CharField(blank=True, max_length=20, null=True)),
                ('train_set_proportion', models.IntegerField()),
                ('test_set_proportion', models.IntegerField()),
                ('valid_set_proportion', models.IntegerField()),
                ('status', models.CharField(max_length=1)),
                ('after_train_model_path', models.CharField(blank=True, max_length=128, null=True)),
                ('f1', models.IntegerField(blank=True, null=True)),
                ('accuracy', models.IntegerField(blank=True, null=True)),
                ('recall', models.IntegerField(blank=True, null=True)),
                ('precision', models.IntegerField(blank=True, null=True)),
                ('bleu', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'train_model_task',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('role', models.CharField(blank=True, max_length=1, null=True)),
                ('age', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('gender', models.CharField(blank=True, max_length=1, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'user_info',
                'managed': False,
            },
        ),
    ]