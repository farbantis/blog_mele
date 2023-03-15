from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    changefreq = 'weekly'  # change frequency of your post pages
    priority = 0.9  # their relevance in your website (the maximum value is 1)

    def items(self):  # the QuerySet of objects to include in this sitemap, использует get_absolute_url
        return Post.published.all()

    #  lastmod method receives each object returned by items() and returns the last time the object was modified
    def lastmod(self, obj):
        return obj.updated

