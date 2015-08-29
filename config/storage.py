#!/usr/bin/env python
# coding=utf-8
from django.core.files.storage import get_storage_class
from storages.backends.s3boto import S3BotoStorage
from whitenoise.django import GzipManifestStaticFilesStorage

'whitenoise.django.GzipManifestStaticFilesStorage'


class CompressorStorageMixin(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.local_storage = get_storage_class(
            'compressor.storage.CompressorFileStorage')()

    def save(self, name, content, max_length=None):
        name = super().save(name, content, max_length)
        self.local_storage._save(name, content)
        return name


class CachedS3BotoStorage(CompressorStorageMixin, S3BotoStorage):
    pass


class CachedGzipManifestStaticFilesStorage(CompressorStorageMixin,
                                           GzipManifestStaticFilesStorage):
    pass
