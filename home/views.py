from django.shortcuts import render
from django.views.generic import TemplateView
from home.models import SocialMedia, OfficeTimeLocation, Banner, Feature, FeatureItem

# Create your views here.


class Home(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['socialmedia'] = SocialMedia.objects.first()
        context['office'] = OfficeTimeLocation.objects.first()
        context['banner'] = Banner.objects.first()
        context['feature'] = Feature.objects.first()
        context['feature_items'] = FeatureItem.objects.all()
        return context
