"""Configuration section for plugin."""
from __future__ import annotations

from sopel.config.types import (
    FilenameAttribute,
    SecretAttribute,
    StaticSection,
)  # type: ignore


class GeoipSection(StaticSection):
    GeoIP_db_path = FilenameAttribute('GeoIP_db_path', directory=True)
    """Path of the directory containing the GeoIP database files.

    If the given value is not an absolute path, it will be interpreted relative
    to the directory containing the config file with which Sopel was started.
    """

    maxmind_license_key = SecretAttribute(
        'maxmind_license_key', default='JXBEmLjOzislFnh4')
    """License key for downloading GeoIP database files from MaxMind.

    The plugin ships with a default key, but this option is available in case
    overriding the inbuilt key is desired or required.
    """
