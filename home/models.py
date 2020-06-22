from django.db import models


class SocialMedia(models.Model):
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    googleplus = models.URLField(blank=True)


class OfficeTimeLocation(models.Model):
    location = models.CharField(max_length=100, blank=True)
    office_time = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.location


class Banner(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    background_image = models.ImageField(upload_to='banner')
    foreground_image = models.ImageField(upload_to='banner')

    def __str__(self):
        return self.title


class Feature(models.Model):
    feature_title = models.CharField(max_length=100, blank=True)
    feature_description = models.TextField()
    feature_image = models.ImageField(upload_to='feature')

    def __str__(self):
        return self.feature_title


class FeatureItem(models.Model):
    feature_icon_name = models.CharField(max_length=100, blank=True)
    feature_item_title = models.CharField(max_length=100, blank=True)
    feature_item_description = models.TextField()

    def __str__(self):
        return self.feature_item_title
