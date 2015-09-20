"""
Load all the important models and factories into current scope.

Usage:

```
from shell_model_loader import *
```
"""

from annotation_tool.users.models import User
from annotation_tool.pubmed import Entry
from annotation_tool.pubmed.factories import EntryFactory
from annotation_tool.users.factories import UserFactory, SuperUserFactory

__all__ = ['User', 'Entry', 'EntryFactory', 'UserFactory', 'SuperUserFactory']
