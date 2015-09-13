# Django Packages
from django.core.files.storage import get_storage_class

# Third Party Packages
import storages.backends.s3boto
from whitenoise.django import GzipManifestStaticFilesStorage


class CachedS3BotoStorage(storages.backends.s3boto.S3BotoStorage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.local_storage = get_storage_class('compressor.storage.CompressorFileStorage')()

    def save(self, *args, **kwargs):
        name = super(CachedS3BotoStorage, self).save(*args, **kwargs)
        self.local_storage._save(*args, **kwargs)
        return name
