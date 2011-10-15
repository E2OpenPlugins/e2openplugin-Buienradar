from Plugins.Plugin import PluginDescriptor

def main(session, **kwargs):
	import ui
	session.open(ui.Radar)


def Plugins(**kwargs):
	return \
		[PluginDescriptor(name="BuienRadar", description=_("Buienradar demootje"), icon="plugin.png", where = PluginDescriptor.WHERE_PLUGINMENU, needsRestart = False, fnc=main)]
