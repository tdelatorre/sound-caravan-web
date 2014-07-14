from django.db import models
from django.utils.translation import ugettext_lazy as _


class Home(models.Model):
    main_video = models.ForeignKey('Video',
        blank=False, null=False,
        verbose_name=_(u'Main video')
    )

    class Meta:
        verbose_name = _(u'Home')
        verbose_name_plural = _(u'Homes')


class AboutUs(models.Model):
    title = models.CharField(
        max_length=50, blank=False, null=False,
        verbose_name=_(u'Title')
    )
    description = models.TextField(
        blank=False, null=False,
        verbose_name=_(u'Description')
    )
    image = models.ForeignKey('Image',
        blank=False, null=False,
        verbose_name=_(u'Image')
    )

    class Meta:
        verbose_name = _(u'About us')
        verbose_name_plural = _(u'About us')

    def __unicode__(self):
        return u'{}'.format(self.title)


class Member(models.Model):
    name = models.CharField(
        max_length=100, blank=False, null=False,
        verbose_name=_(u'Name')
    )
    description = models.TextField(
        blank=False, null=False,
        verbose_name=_(u'Description')
    )
    image = models.ForeignKey('Image',
        blank=False, null=False,
        verbose_name=_(u'Image')
    )

    class Meta:
        verbose_name = _(u'Member')
        verbose_name_plural = _(u'Members')

    def __unicode__(self):
        return u'{}'.format(self.name)


class Event(models.Model):
    title = models.CharField(
        max_length=50, blank=False, null=False,
        verbose_name=_(u'Title')
    )
    description = models.TextField(
        blank=False, null=False,
        verbose_name=_(u'Description')
    )
    location = models.TextField(
        blank=False, null=False,
        verbose_name=_(u'Location')
    )
    event_date = models.DateField(
        blank=False, null=False,
        verbose_name=_(u'Event Date')
    )
    event_hour = models.TimeField(
        blank=False, null=False,
        verbose_name=_(u'Event Hour')
    )
    price = models.CharField(
        max_length=50, blank=False, null=False,
        verbose_name=_(u'Price')
    )

    class Meta:
        verbose_name = _(u'Event')
        verbose_name_plural = _(u'Events')

    def __unicode__(self):
        return u'{}'.format(self.title)


class Contact(models.Model):
    address = models.TextField(
        blank=True, null=False,
        verbose_name=_(u'Address')
    )
    email1 = models.CharField(
        max_length=50, blank=False, null=False,
        verbose_name=_(u'Email1')
    )
    email2 = models.CharField(
        max_length=50, blank=True, null=False,
        verbose_name=_(u'Email2')
    )
    phone1 = models.CharField(
        max_length=25, blank=False, null=False,
        verbose_name=_(u'Phone1')
    )
    phone2 = models.CharField(
        max_length=25, blank=True, null=False,
        verbose_name=_(u'Phone2')
    )
    facebook = models.CharField(
        max_length=255, blank=False, null=False,
        verbose_name=_(u'Facebook')
    )
    twitter = models.CharField(
        max_length=255, blank=False, null=False,
        verbose_name=_(u'Twitter')
    )
    myspace = models.CharField(
        max_length=255, blank=False, null=False,
        verbose_name=_(u'MySpace')
    )

    class Meta:
        verbose_name = _(u'Contact')
        verbose_name_plural = _(u'Contacts')


class Image(models.Model):
    image = models.ImageField(
        null=False, blank=False,
        default=None, upload_to=None
    )

    class Meta:
        verbose_name = _(u'Image')
        verbose_name_plural = _(u'Images')

    def __unicode__(self):
        return _(u'image {}').format(self.image)


class Video(models.Model):
    video_script = models.TextField(
        blank=False, null=False,
        verbose_name=_(u'Video Script')
    )

    class Meta:
        verbose_name = _(u'Video')
        verbose_name_plural = _(u'Videos')