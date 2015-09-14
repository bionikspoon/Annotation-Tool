# Django Packages
from django.conf import settings

google_id = 'google51945c962ca81cb4.html'


def add_page(apps, _):
    """Set site domain and name."""
    FlatPage = apps.get_model("flatpages", "FlatPage")
    page, _ = FlatPage.objects.update_or_create(url='/%s/' % google_id, defaults={
        'title': google_id,
        'content': 'google-site-verification: %s' % google_id,
        'template_name': 'flatpages/empty.html'
    })
    page.sites.add(settings.SITE_ID)
    page.save()


def remove_page(apps, _):
    """Revert site domain and name to default."""
    FlatPage = apps.get_model("flatpages", "FlatPage")
    FlatPage.objects.get(url='/%s/' % google_id).delete()
