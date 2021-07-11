# -*- coding: utf-8 -*-
# Copyright (C) 2021 Héctor J. Benítez Corredera <xebolax@gmail.com>
# This file is covered by the GNU General Public License.

# import the necessary modules (NVDA)
import globalPluginHandler
import addonHandler
import keyboardHandler
import api
from scriptHandler import script

addonHandler.initTranslation()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	@script(gesture=None, description= _("Simular tecla Aplicaciones"), category= _("RemapKeyAplication"))
	def script_Run(self, gesture):
		obj=api.getFocusObject()
		api.moveMouseToNVDAObject(obj)
		keyboardHandler.KeyboardInputGesture.fromName("applications").send()
