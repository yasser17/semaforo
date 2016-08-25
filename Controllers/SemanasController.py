from wx.dataview import DataViewListCtrl
from Models.semana import Semana
from wx.dataview import DataViewItem

class SemanasController:

    @staticmethod
    def getAll(xlist):
        list = Semana.query.all()
        for s in list:
            xlist.AppendItem(s)