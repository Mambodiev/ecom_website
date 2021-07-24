from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class About(models.Model):
    name = models.CharField(max_length=50)
    about_text = RichTextUploadingField()
    
    def __str__(self):
        return self.about_text


class Faq(models.Model):
    name = models.CharField(max_length=50)
    faq_text = RichTextUploadingField(blank=True, null=True,)
    
    def __str__(self):
        return self.faq_text
        

class Privacy_policy(models.Model):
    name = models.CharField(max_length=50)
    privacy_policy_text = RichTextUploadingField(blank=True, null=True,)
    
    def __str__(self):
        return self.privacy_policy_text



class Shipping_returns(models.Model):
    name = models.CharField(max_length=50)
    shipping_returns_text = RichTextUploadingField(blank=True, null=True,)
    
    def __str__(self):
        return self.shipping_returns_text
    


class Terms_of_use(models.Model):
    name = models.CharField(max_length=50)
    terms_of_use_text = RichTextUploadingField(blank=True, null=True,)
    
    def __str__(self):
        return self.terms_of_use_text

class Carousel(models.Model):
    carousel_image = models.ImageField()
    carousel_logo_slider = models.ImageField()
    carousel_title = models.CharField(max_length=100, blank=True)
    carousel_sub_title = models.CharField(max_length=100)
    carousel_action = models.CharField(max_length=100) or models
    
    def __str__(self):
        return self.carousel_title
