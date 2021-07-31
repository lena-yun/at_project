from django.shortcuts import render
from django.views.generic import TemplateView


class IndexViews(TemplateView):
    template_name = "at_project/gy/index.html"


class AboutViews(TemplateView):
    template_name = "at_project/gy/about.html"


class BlogViews(TemplateView):
    template_name = "at_project/gy/blog.html"


class BlogDetailViews(TemplateView):
    template_name = "at_project/gy/blog-details.html"


class CheckoutViews(TemplateView):
    template_name = "at_project/gy/checkout.html"


class ClassViews(TemplateView):
    template_name = "at_project/gy/class.html"


class ContactViews(TemplateView):
    template_name = "at_project/gy/contact.html"


class ShopViews(TemplateView):
    template_name = "at_project/gy/shop.html"


class ShopDetailViews(TemplateView):
    template_name = "at_project/gy/shop-details.html"


class ShopingCartViews(TemplateView):
    template_name = "at_project/gy/shoping-cart.html"


class WissListViews(TemplateView):
    template_name = "at_project/gy/wisslist.html"
