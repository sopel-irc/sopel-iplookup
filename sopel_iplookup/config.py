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

    maxmind_license_key = SecretAttribute('maxmind_license_key', default=None)
    """License key for downloading GeoIP database files from MaxMind.

    The plugin downloads from a keyless source by default, but this option is
    available if you wish to download the files using your own MaxMind account.
    """
