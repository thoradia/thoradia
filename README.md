# Thoradia Add-ons Repository

The Thoradia Add-ons repository is a collection of add-ons for [LibreELEC](https://libreelec.tv/) or forks thereof.

## Disclaimers

### Keep it legal and carry on

Responsibility for the installation, the configuration and the operation of add-ons of the Thoradia Add-ons repository, and for the consequences thereof, lies exclusively with the user.

### System Resources

LibreELEC runs on many hardware, some of which have just enough resources for Kodi. Add-ons of the Thoradia Add-ons repository will compete with Kodi for these resources, especially if they are limited. Therefore, consider using appropriate hardware or limiting the number of installed add-ons. As an indication, at the moment of writing, a Raspberry Pi 4 with 2 GB of RAM appears suitable to concurrently run all the add-ons of the Thoradia Add-ons repository without disturbing Kodi.

### Support

The add-ons are built with the LibreELEC build system to run on the LibreELEC operating system. The Thoradia Add-ons repository is however not otherwise related to the LibreELEC project. Do therefore not expect any support from the LibreELEC project with add-ons of the Thoradia Add-ons repository.

## Installation

The Thoradia Add-ons repository needs to be installed from a zip file. The zip file depends on the version of LibreELEC on which it is installed, as listed below:

-   for LibreELEC version 9.2.x or lower, use [this zip file](https://github.com/thoradia/thoradia/raw/bootstrap/service.thoradia.9.2.0.23.zip),
-   for LibreELEC version 9.80.x or higher, use [this zip file](https://github.com/thoradia/thoradia/raw/bootstrap/service.thoradia.9.80.4.24.zip).

First, download the appropriate zip file to a location that can be accessed from LibreELEC, for example to the downloads [SMB share](https://wiki.libreelec.tv/accessing_libreelec#tab__sambasmb) LibreELEC.

Then, use Kodi on LibreELEC to install the Thoradia Add-ons repository from the downloaded zip file, as described [here](https://kodi.wiki/view/Add-on_manager#How_to_install_from_a_ZIP_file).

The Thoradia Add-ons repository will reconfigure itself to use the add-ons corresponding to the release of Libreelec on which it is installed.

Finally, restart Kodi to take the reconfiguration into account.

You can now manage (install, update, uninstall, etc.) all the add-ons of the Thoradia Add-ons repository with the Kodi Add-on manager, as described [here](https://kodi.wiki/view/Add-on_manager).

## Add-on Summary

| Port                                | Add-on                                            | Function                 |
| ----------------------------------- | ------------------------------------------------- | ------------------------ |
|                                     | [aria2](https://aria2.github.io/)                 | download client          |
| [6767](http://libreelec.local:6767) | [Bazarr](https://github.com/morpheus65535/bazarr) | subtitle manager         |
|                                     | [btfs](https://github.com/johang/btfs)            | bittorrent client        |
| [8112](http://libreelec.local:8112) | [Deluge](https://deluge-torrent.org/)             | bittorrent client        |
|                                     | [FlexGet](https://flexget.com/)                   | download client          |
| [9117](http://libreelec.local:9117) | [Jackett](https://github.com/Jackett/Jackett)     | media indexer            |
| [8686](http://libreelec.local:8686) | [Lidarr](https://lidarr.audio/)                   | music manager            |
| [8081](8081)                        | [Medusa](https://github.com/pymedusa/Medusa)      | series manager           |
|                                     | [Mono](https://www.mono-project.com/)             | software platform        |
|                                     | [NordVPN](https://nordvpn.com/)                   | virtual private network  |
| [6789](http://libreelec.local:6789) | [NZBGet](https://nzbget.net/)                     | usenet client            |
| [8880](http://libreelec.local:8880) | [qBittorrent](https://www.qbittorrent.org/)       | bittorrent client        |
| [7878](http://libreelec.local:7878) | [Radarr](https://radarr.video/)                   | movie manager            |
| [8085](http://libreelec.local:8085) | [SABnzbd](https://sabnzbd.org/)                   | usenet client            |
| [8989](http://libreelec.local:8989) | [Sonarr](https://sonarr.tv/)                      | series manager           |
|                                     | Thoradia                                          | add-on repository        |
|                                     | Thoradia Mono Tools                               | software libraries       |
|                                     | Thoradia VPN Interface                            | virtual private network  |
| [9091](http://libreelec.local:9091) | [Transmission](https://transmissionbt.com/)       | bittorrent manager       |
|                                     | [WebGrab+Plus](http://webgrabplus.com/)           | electronic program guide |
|                                     | [ZeroTier One](https://www.zerotier.com/)         | virtual private network  |

## GitHub

### Source code

The source code of the Thoradia add-ons for LibreELEC can be found [here](https://github.com/thoradia/LibreELEC.tv/branches). At the time of writing, only the following branches are maintained:

-   [9.80.4](https://github.com/thoradia/LibreELEC.tv/tree/9.80.4) for [LibreELEC nightly builds](https://test.libreelec.tv/),
-   [9.2](https://github.com/thoradia/LibreELEC.tv/tree/9.2/) for LibreELEC 9.2.x,
-   [coreelec-9.2](https://github.com/thoradia/LibreELEC.tv/tree/coreelec-9.2/) for CoreELEC 9.2.x.

### Add-ons

The add-ons can be found [here](https://github.com/thoradia/thoradia/branches), in particular:

-   [9.80.4](https://github.com/thoradia/thoradia/tree/9.80.4) for [LibreELEC nightly builds](https://test.libreelec.tv/),
-   [master](https://github.com/thoradia/thoradia/tree/master) for LibreELEC 9.2.x and CoreELEC 9.2.x.

## Feedback

The preferred way to submit bugs, comments and feature requests are [GitHub issues](https://github.com/thoradia/LibreELEC.tv/issues).

[Pull requests](https://github.com/thoradia/LibreELEC.tv/pulls) are welcome too.

As a last resort, post a reply at in [the Thoradia Add-ons thread of the LibreELEC forum](https://forum.libreelec.tv/thread/2707-thoradia-add-ons/).
