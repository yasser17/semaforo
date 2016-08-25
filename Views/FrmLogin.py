# -*- coding: utf-8 -*-



import wx
import wx.xrc
from Models.Parametros import Parametros


###########################################################################
## Class FrmLogin
###########################################################################

class FrmLogin(wx.Dialog):
    login = None
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Login", pos=wx.DefaultPosition, size=wx.Size(359, 128),
                           style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer26 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText12 = wx.StaticText(self, wx.ID_ANY, u"Ingrese Contraseña", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText12.Wrap(-1)
        bSizer26.Add(self.m_staticText12, 0, wx.ALL, 5)

        self.txtpass = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD)
        bSizer26.Add(self.txtpass, 0, wx.ALL | wx.EXPAND, 5)

        bSizer27 = wx.BoxSizer(wx.HORIZONTAL)

        self.btnAceptar = wx.Button(self, wx.ID_ANY, u"Aceptar", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer27.Add(self.btnAceptar, 0, wx.ALL, 5)

        self.btnCancelar = wx.Button(self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer27.Add(self.btnCancelar, 0, wx.ALL, 5)

        bSizer26.Add(bSizer27, 0, wx.ALIGN_RIGHT, 5)

        self.SetSizer(bSizer26)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.btnAceptar.Bind(wx.EVT_BUTTON, self.btnAceptarOnButtonClick)
        self.btnCancelar.Bind(wx.EVT_BUTTON, self.btnCancelarOnButtonClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def btnAceptarOnButtonClick(self, event):
        p = Parametros.query.first()
        texto = str(hash(self.txtpass.GetValue()))
        if(str(p.password) == texto):
            self.login = True
            self.Close()
        else:
            print "Contrasena incorrecta"

    def btnCancelarOnButtonClick(self, event):
        self.Close()