import xbmc
import xbmcgui
import sqlite3

addons27path = xbmc.translatePath('special://database/Addons27.db')
addons27 = sqlite3.connect(addons27path)

addons27.cursor().execute('''delete from addons where addonID='script.extendedinfo' and name like '%Wraith%';''')
addons27.commit()
addons27.close()
xbmcgui.Dialog().notification('Hide Wraith', 'Dunzoed!')
