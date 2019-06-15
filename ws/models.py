from django.db import models
from django.utils.translation import ugettext as _
from rest_framework.reverse import reverse
# Create your models here.
class Profile(models.Model):
	file_name = models.CharField(max_length=100, blank=True)
	attach_file = models.FileField(
		upload_to='documents/%Y/%m/%d',
		verbose_name=u'PDF File',
		blank = True,
		null = True
	)
	attach_file_src = ''

	def __unicode__(self):
		return self.file_name

	def attach_file_src(self):
		if self.attach_file_src:
			return reverse('profile-preview', kwargs={'id': self.id})
		else:
			return ""