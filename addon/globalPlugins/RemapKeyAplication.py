# -*- coding: utf-8 -*-
# Copyright (C) 2021 Héctor J. Benítez Corredera <xebolax@gmail.com>
# This file is covered by the GNU General Public License.

# import the necessary modules (NVDA)
import globalPluginHandler
import addonHandler
import keyboardHandler
import api
from scriptHandler import script
from threading import Thread

addonHandler.initTranslation()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	@script(gesture=None, description= _("Simular tecla Aplicaciones"), category= _("RemapKeyAplication"))
	def script_Run(self, gesture):
				self.mainThread = HiloComplemento()
				self.mainThread.start()

class HiloComplemento(Thread):
	def __init__(self):
		super(HiloComplemento, self).__init__()

		self.daemon = True

	def run(self):

		obj=api.getFocusObject()
		api.moveMouseToNVDAObject(obj)
		keyboardHandler.KeyboardInputGesture.fromName("applications").send()
