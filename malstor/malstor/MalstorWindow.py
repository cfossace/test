# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

from locale import gettext as _

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('malstor')

from malstor_lib import Window
from malstor.AboutMalstorDialog import AboutMalstorDialog
from malstor.PreferencesMalstorDialog import PreferencesMalstorDialog

# See malstor_lib.Window.py for more details about how this class works
class MalstorWindow(Window):
    __gtype_name__ = "MalstorWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(MalstorWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutMalstorDialog
        self.PreferencesDialog = PreferencesMalstorDialog

        # Code for other initialization actions should be added here.

        self.button2 = self.builder.get_object("Exit")
    def on_button2_clicked(self,widget):
        exit();
