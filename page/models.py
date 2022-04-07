from django.utils.translation import gettext as _
from django.db import models


class Contact(models.Model):
    email = models.EmailField(_('E-Mail'), max_length=255, default='')
    message = models.CharField(_('Wiadomość'), default='', max_length=2000)
    created_at = models.DateTimeField(_('Data'), auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return '%s - %s' %(self.email, self.created_at)
