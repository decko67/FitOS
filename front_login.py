# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class LoginFrame
###########################################################################

class LoginFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"GymOS"), pos = wx.DefaultPosition, size = wx.Size( 281,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.nombre = wx.StaticText( self, wx.ID_ANY, _(u"Nombre:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.nombre.Wrap( -1 )

        bSizer1.Add( self.nombre, 0, wx.ALL, 5 )

        self.nombreCTRL = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.nombreCTRL, 0, wx.ALL, 5 )

        self.contraseñaCTRL = wx.StaticText( self, wx.ID_ANY, _(u"Contraseña:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.contraseñaCTRL.Wrap( -1 )

        bSizer1.Add( self.contraseñaCTRL, 0, wx.ALL, 5 )

        self.ContraseñaCTRL = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.ContraseñaCTRL, 0, wx.ALL, 5 )

        self.enviarBTN = wx.Button( self, wx.ID_ANY, _(u"Enviar"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.enviarBTN, 0, wx.ALL, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.enviarBTN.Bind( wx.EVT_BUTTON, self.on_press )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_press( self, event ):
        event.Skip()


