"""
Add data to registry.
"""

try:
    from .registry import InitialData, clean_lookup_tables, populate_lookup_tables
finally:
    from .entered_data import *
    from .generated_data import *
