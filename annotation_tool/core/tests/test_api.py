# Local Application
from ..utils.test import BaseAPITestCase


class CoreAPITestCase(BaseAPITestCase):
    def test_root_links_to_app_apis(self):
        self.get('/api/', format='json')

        self.assertEqual(self.data['lookup'], self.url('/api/lookup/'))
        self.assertEqual(self.data['pubmed'], self.url('/api/pubmed/'))
        self.assertEqual(self.data['users'], self.url('/api/users/'))
