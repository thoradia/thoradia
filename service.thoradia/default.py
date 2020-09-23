import os.path
import xbmc
import xbmcaddon
import xbmcgui
import xml.etree.ElementTree as etree

URL = 'https://raw.githubusercontent.com/thoradia/thoradia/{}/{}/{}/{}/'
REPOSITORIES = ['repository.libreelec.tv',
                'repository.coreelec',
                'repository.cenightly',
                'repository.rbrepo',
                ]

ADDON = xbmcaddon.Addon()
ADDON_STRINGS = ADDON.getLocalizedString
LOG_LEVEL = xbmc.LOGINFO
LOG_MESSAGE = 'thoradia: {}'


def get_xml(repo=''):
    return os.path.join(xbmcaddon.Addon(repo).getAddonInfo('path'), 'addon.xml')


def log(message):
    xbmc.log(LOG_MESSAGE.format(message), LOG_LEVEL)


def update():
    for repo in REPOSITORIES:
        try:
            vers, proj, arch = next(etree.parse(get_xml(repo)).iter(
                tag='datadir')).text.rstrip('/').split('/')[-3:]
        except:
            log('unable to parse {}'.format(repo))
            continue
        ADDON.setSetting('distribution', ADDON_STRINGS(
            30003).format(vers, proj, arch))
        log('found {}/{}/{} in {}'.format(vers, proj, arch, repo))
        if arch == 'x86_64':
            proj = 'Generic'
        else:
            if proj == 'Slice':
                proj = 'RPi'
            elif proj not in ['Amlogic', 'RPi', 'RPi4']:
                proj = 'RPi2'
        log('using {}/{}/{}'.format(vers, proj, arch))
        url = URL.format(vers, vers, proj, arch)
        xml = get_xml()
        tree = etree.parse(xml)
        datadir = next(tree.iter(tag='datadir'))
        if datadir.text != url:
            datadir.text = url
            next(tree.iter(tag='info')).text = url + 'addons.xml'
            next(tree.iter(tag='checksum')).text = url + 'addons.xml.md5'
            tree.write(xml)
            ADDON.setSetting('thoradia', ADDON_STRINGS(
                30004).format(vers, proj, arch))
            ADDON.setSetting('updated', 'true')
            log('updated repository')
            if xbmcgui.Dialog().yesno(ADDON.getAddonInfo('name'),
                                      ADDON_STRINGS(30010).format(
                                          vers, proj, arch),
                                      nolabel=ADDON_STRINGS(30011),
                                      yeslabel=ADDON_STRINGS(30012)) == False:
                xbmc.executebuiltin('RestartApp')
        else:
            ADDON.setSetting('thoradia', ADDON_STRINGS(
                30003).format(vers, proj, arch))
            if ADDON.getSetting('updated') == 'true':
                ADDON.setSetting('updated', 'false')
                xbmc.executebuiltin('UpdateAddonRepos')
                log('updated add-ons')
            else:
                log('repository is up to date')
        return
    log('unable to find a known distribution')
    ADDON.setSetting('distribution', ADDON_STRINGS(
        30005).format('?', '?', '?'))
    return


if __name__ == '__main__':
    update()
