# -*- coding: utf-8 -*-
# Copyright (C) 2021 Héctor J. Benítez Corredera <xebolax@gmail.com>
# This file is covered by the GNU General Public License.

# import the necessary modules (NVDA)
import globalPluginHandler
import addonHandler
import api
import winUser
import globalVars
from scriptHandler import script
from nvwave import playWaveFile
from threading import Thread
import wx
import os
from . import keyFunc

addonHandler.initTranslation()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	@script(gesture=None, description= _("Simular tecla Aplicaciones"), category= _("RemapKeyAplication"))
	def script_RunAplicationn(self, gesture):
				HiloComplemento(1).start()

	@script(gesture=None, description= _("Simular clic izquierdo del ratón al foco"), category= _("RemapKeyAplication"))
	def script_RunLeftMouse(self, gesture):
				HiloComplemento(2).start()

	@script(gesture=None, description= _("Simular clic derecho del ratón al foco"), category= _("RemapKeyAplication"))
	def script_RunRightMouse(self, gesture):
				HiloComplemento(3).start()

class HiloComplemento(Thread):
	def __init__(self, opt):
		super(HiloComplemento, self).__init__()

		self.opt = opt
		self.daemon = True

	def run(self):
		def mouseClick(button="left"):
			if button == "left":
				winUser.mouse_event(winUser.MOUSEEVENTF_LEFTDOWN,0,0,None,None)
				winUser.mouse_event(winUser.MOUSEEVENTF_LEFTUP,0,0,None,None)
			if button == "right":
				winUser.mouse_event(winUser.MOUSEEVENTF_RIGHTDOWN,0,0,None,None)
				winUser.mouse_event(winUser.MOUSEEVENTF_RIGHTUP,0,0,None,None)

		def btnAplication():
			obj=api.getFocusObject()
			api.moveMouseToNVDAObject(obj)
			keyFunc.key_aplicacion()

		def btnLeftMouse():
			obj=api.getFocusObject()
			api.moveMouseToNVDAObject(obj)
			mouseClick("left")
			playWaveFile(os.path.join(globalVars.appArgs.configPath, "addons", "RemapKeyAplication", "globalPlugins", "RemapKeyAplication", "sonidos", "Click.wav"))

		def btnRightMouse():
			obj=api.getFocusObject()
			api.moveMouseToNVDAObject(obj)
			mouseClick("right")
			playWaveFile(os.path.join(globalVars.appArgs.configPath, "addons", "RemapKeyAplication", "globalPlugins", "RemapKeyAplication", "sonidos", "Click.wav"))

		if self.opt == 1:
			wx.CallAfter(btnAplication)
		elif self.opt == 2:
			wx.CallAfter(btnLeftMouse)
		elif self.opt == 3:
			wx.CallAfter(btnRightMouse)