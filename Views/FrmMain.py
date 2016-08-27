# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

#   wx.MessageBox("Are You Sure?","Checking",wx.YES_NO) == wx.YES
#
#
#
#


import wx
import wx.xrc

from Views.FrmSemanas import FrmSemanas
from Views.FrmArduino import FrmArduino
from Views.FrmRegistros import FrmRegistros
from Views.FrmLogin import FrmLogin
from Views.FrmPassword import FrmPassword
from Views.FrmPuerto import FrmPuerto
from Views.FrmRegistrosDiario import FrmRegistrosDiario
from Views.FrmAbout import FrmAbout
from Models.Parametros import Parametros

###########################################################################
## Class FrmMain
###########################################################################

class FrmMain(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Sorteo", pos=wx.DefaultPosition, size=wx.Size(800, 600),
                          style=wx.CAPTION | wx.CLOSE_BOX | wx.DEFAULT_FRAME_STYLE | wx.MAXIMIZE | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX)

        self.SetSizeHintsSz(wx.Size(-1, -1), wx.Size(-1, -1))

        self.m_menubar1 = wx.MenuBar(0)
        self.menu1 = wx.Menu()
        self.nenu_item_password = wx.MenuItem(self.menu1, wx.ID_ANY, u"Cambio Contraseña", wx.EmptyString,
                                              wx.ITEM_NORMAL)
        self.menu1.AppendItem(self.nenu_item_password)

        self.menu_item_puerto = wx.MenuItem(self.menu1, wx.ID_ANY, u"Puerto Dispositivo", wx.EmptyString,
                                            wx.ITEM_NORMAL)
        self.menu1.AppendItem(self.menu_item_puerto)

        self.menu_item = wx.MenuItem(self.menu1, wx.ID_ANY, u"Salir", wx.EmptyString, wx.ITEM_NORMAL)
        self.menu1.AppendItem(self.menu_item)

        self.m_menubar1.Append(self.menu1, u"Aplicación")

        self.menu2 = wx.Menu()
        self.menuItem2 = wx.MenuItem(self.menu2, wx.ID_ANY, u"Registro de Semanas", wx.EmptyString, wx.ITEM_NORMAL)
        self.menu2.AppendItem(self.menuItem2)

        self.m_menubar1.Append(self.menu2, u"Premios")

        self.menu3 = wx.Menu()
        self.menuItem3 = wx.MenuItem(self.menu3, wx.ID_ANY, u"Pulsaciones del Día", wx.EmptyString, wx.ITEM_NORMAL)
        self.menu3.AppendItem(self.menuItem3)

        self.menuItem4 = wx.MenuItem(self.menu3, wx.ID_ANY, u"Registro Total de Pulsaciones", wx.EmptyString,
                                     wx.ITEM_NORMAL)
        self.menu3.AppendItem(self.menuItem4)

        self.m_menubar1.Append(self.menu3, u"Registro de Pulsaciones")

        self.menu4 = wx.Menu()
        self.menu_item5 = wx.MenuItem(self.menu4, wx.ID_ANY, u"Acerca de", wx.EmptyString, wx.ITEM_NORMAL)
        self.menu4.AppendItem(self.menu_item5)

        self.m_menubar1.Append(self.menu4, u"Ayuda")

        self.SetMenuBar(self.m_menubar1)

        self.Centre(wx.HORIZONTAL)

        dlg = wx.PasswordEntryDialog(self, u"Ingrese contraseña", u"Semaforo")
        if(dlg.ShowModal() == wx.ID_OK):
            password = str(hash(dlg.GetValue()))
            p = Parametros.query.first()
            if (str(p.password) != password):
                self.Destroy()
            dlg.Destroy()
        else:
            self.Destroy()
            dlg.Destroy()

        # Connect Events
        self.Bind(wx.EVT_MENU, self.menu_itemOnMenuSelection, id=self.menu_item.GetId())
        self.Bind(wx.EVT_MENU, self.menuItem2OnMenuSelection, id=self.menuItem2.GetId())
        self.Bind(wx.EVT_MENU, self.menu3OnMenuSelection, id=self.menuItem3.GetId())
        self.Bind(wx.EVT_MENU, self.menu4OnMenuSelection, id=self.menuItem4.GetId())
        self.Bind(wx.EVT_MENU, self.nenu_item_passwordOnMenuSelection, id=self.nenu_item_password.GetId())
        self.Bind(wx.EVT_MENU, self.menu_item_puertoOnMenuSelection, id=self.menu_item_puerto.GetId())
        self.Bind(wx.EVT_MENU, self.menu_item_aboutOnMenuSelection, id=self.menu_item5.GetId())


    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def menu_itemOnMenuSelection(self, event):
        self.Close()

    def menuItem2OnMenuSelection(self, event):
        mfrm = FrmSemanas(None)
        mfrm.ShowModal()
        mfrm.Destroy()

    def menu3OnMenuSelection(self, event):
        mfrm = FrmRegistrosDiario(None)
        mfrm.ShowModal()
        mfrm.Destroy()

    def menu4OnMenuSelection(self, event):
        mfrm = FrmRegistros(None)
        mfrm.ShowModal()
        mfrm.Destroy()

    def nenu_item_passwordOnMenuSelection(self, event):
        mfrm = FrmPassword(None)
        mfrm.ShowModal()
        mfrm.Destroy()

    def menu_item_puertoOnMenuSelection(self, event):
        mfrm = FrmPuerto(None)
        mfrm.ShowModal()
        mfrm.Destroy()


    def menu_item_aboutOnMenuSelection(self, event):
        mfrm = FrmAbout(None)
        mfrm.ShowModal()
        mfrm.Destroy()