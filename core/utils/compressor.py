from django.core.files.storage import get_storage_class
from storages.backends.s3boto import S3BotoStorage


class CachedS3BotoStorage(S3BotoStorage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.local_storage = get_storage_class('compressor.storage.CompressorFileStorage')()

    def save(self, name, content, max_length=None):
        name = super(CachedS3BotoStorage, self).save(name, content, max_length=max_length)
        self.local_storage._save(name, content, max_length=max_length)
        return name
