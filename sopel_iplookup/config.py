"""Configuration section for plugin."""
from __future__ import annotations

from sopel.config.types import FilenameAttribute, StaticSection  # type: ignore


class GeoipSection(StaticSection):
    GeoIP_db_path = FilenameAttribute('GeoIP_db_path', directory=True)
    """Path of the directory containing the GeoIP database files.

    If the given value is not an absolute path, it will be interpreted relative
    to the directory containing the config file with which Sopel was started.
    """
