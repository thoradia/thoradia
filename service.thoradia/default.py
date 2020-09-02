import os.path
import subprocess
import xbmc
import xbmcaddon
import xbmcgui
import xml.etree.ElementTree as etree

ADDON = xbmcaddon.Addon()
DATADIR = 'https://raw.githubusercontent.com/thoradia/thoradia/master/{}/{}/{}/'
LOGLEVEL = xbmc.LOGNOTICE
RELEASE = ['-', '-', '-']
REPOSITORIES = [
    'repository.libreelec.tv',
    'repository.coreelec',
    'repository.cenightly',
    'repository.rbrepo',
]
STRINGS = ADDON.getLocalizedString


def get_datadir(*repository):
    return etree.parse(get_xml(*repository)).iter(tag='datadir').next().text


def get_xml(*repository):
    return os.path.join(xbmcaddon.Addon(*repository).getAddonInfo('path'),
                        'addon.xml')


def log(message):
    xbmc.log('Thoradia Add-ons: {}'.format(message), LOGLEVEL)


if __name__ == '__main__':
    release = RELEASE
    for repository in REPOSITORIES:
        try:
            release = get_datadir(repository).strip('/').split('/')[-3:]
            break
        except:
            pass
    log('found release {}/{}/{}'.format(*release))

    distribution = STRINGS(30005).format(*release)

    if release[0] == '9.0.1':
        release[0] = '9.1'

    if release[2] == 'aarch64':
        if release[1] in ['WeTek_Hub', 'WeTek_Play_2']:
            release[1] = 'Odroid_C2'
    elif release[2] == 'arm':
        if release[1] in ['Odroid_C2', 'S905', 'S912', 'Slice3']:
            release[1] = 'RPi2'
        elif release[1] in ['Slice']:
            release[1] = 'RPi'
        elif release[1] in ['S805', 'WeTek_Core', 'WeTek_Hub', 'WeTek_Play_2']:
            release[1] = 'WeTek_Play'
        elif release[1] in ['MiQi', 'RK3399', 'TinkerBoard']:
            release[1] = 'RK3328'
    elif release[2] == 'x86_64':
        release[1] = 'Generic'
    log('using release {}/{}/{}'.format(*release))

    datadir_old = get_datadir()
    datadir_new = DATADIR.format(*release)

    if datadir_new != datadir_old:
        xml = get_xml()
        tree = etree.parse(xml)
        tree.iter(tag='datadir').next().text = datadir_new
        tree.iter(tag='info').next().text = datadir_new + 'addons.xml'
        tree.iter(tag='checksum').next().text = datadir_new + 'addons.xml.md5'
        tree.write(xml)
        log('updated datadir to {}'.format(datadir_new))

        ADDON.setSetting('distribution', distribution)
        ADDON.setSetting('thoradia', STRINGS(30006).format(*release))
        ADDON.setSetting('updated', 'true')

        if xbmcgui.Dialog().yesno(ADDON.getAddonInfo('name'),
                                  STRINGS(30010).format(*release),
                                  nolabel=STRINGS(30011),
                                  yeslabel=STRINGS(30012)) == False:
            subprocess.call(['systemctl', 'restart', 'kodi'])

    else:
        if ADDON.getSetting('updated') == 'true':
            ADDON.setSetting('updated', 'false')
            ADDON.setSetting('thoradia', STRINGS(30005).format(*release))
            xbmc.executebuiltin('UpdateAddonRepos')
            log('updating add-ons')
        else:
            log('repository is up to date')
