from django.db import models

# Create your models here.

# 兼容python2.x
@python_2_unicode_compatible
class Article(models.Model):
	title = models.CharField(u'标题', max_length=256)
	content = models.TextField(u'内容')

	pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
	update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)
	
	def __str__(self):
		# 显示每个文章的文章标题
		return self.title
