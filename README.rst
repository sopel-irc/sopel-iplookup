==============
sopel-iplookup
==============

Sopel plugin ``.ip`` command::

    16:22 <SnoopJ> !ip 8.8.8.8
    16:22 <testibot> [IP/Host Lookup] Downloading GeoIP database, please wait...
    16:22 <testibot> [IP/Host Lookup] Hostname: dns.google | Location: United States | ISP: AS15169 GOOGLE

Install
=======

The recommended way to install this plugin is to use ``pip``::

    $ pip install sopel-iplookup

Note that this plugin requires Python 3.7+ and Sopel 7.1+. It won't work on
Python versions that are not supported by the version of Sopel you are using.

Notes
=====

This plugin replaces a built-in Sopel plugin formerly called ``ip``, you may need
to update your bot configuration to replace ``ip`` with ``iplookup`` if you are e.g.
excluding this plugin.
