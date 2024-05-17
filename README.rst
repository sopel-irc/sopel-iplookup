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

Configure
=========

``sopel-iplookup`` can be configured by invoking Sopel's interactive wizard::

    $ sopel-plugins configure iplookup
    Configure Sopel GeoIP Lookup Plugin
    Please consult sopel-iplookup's README to learn about its settings.

    Path to existing GeoIP db files (leave empty to auto download): 
    MaxMind license key (optional): (hidden input)

If your OS distribution has GeoIP database files installed already, you can
provide a filesystem path to the folder where they are stored. The plugin will
auto-download the database files if it cannot find them locally.

By default, GeoIP database downloads will use an automated mirror on GitHub. You
can optionally provide your own MaxMind license key and the plugin will download
directly from them—useful in case the mirror breaks, or if you would simply like
to get database files from the source.

Notes
=====

This plugin replaces a built-in Sopel plugin formerly called ``ip``, you may need
to update your bot configuration to replace ``ip`` with ``iplookup`` if you are e.g.
excluding this plugin.
