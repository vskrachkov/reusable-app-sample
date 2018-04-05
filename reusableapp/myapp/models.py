from django.conf import settings
from django.db import models
from django.apps import apps
from django.utils.translation import ugettext_lazy as _


_app_label = settings.MYAPP_COMMON_MODELS_APP_LABEL


def get_model_string(model_name):
    return '{}.{}'.format(_app_label, model_name)


def get_model(model_name):
    try:
        app_label = _app_label
        return apps.get_model(app_label, model_name)
    except Exception as err:
        raise err


class AbstractAuthor(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True


class AbstractArticle(models.Model):
    article_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(
        to=get_model_string('Author'), on_delete=models.CASCADE
    )
    category = models.CharField(
        max_length=20, choices=((_('News'), _('News')),
                               (_('Science'), _('Science')))
    )

    class Meta:
        abstract = True


class RootModel(models.Model):
    some_text = models.TextField()

    objects = models.Manager()
