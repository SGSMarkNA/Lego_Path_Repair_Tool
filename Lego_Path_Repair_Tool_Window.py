
import os
import sys
from . import scan_and_replace_paths
from PySide2 import QtWidgets,QtCore,QtUiTools

_UI_Loader = QtUiTools.QUiLoader()

_current_dir = os.path.dirname(__file__)

_ui_file = os.path.join(_current_dir,"Lego_Path_Repair_Tool.ui")


########################################################################
class Drop_Label(QtWidgets.QLabel):
	""""""
	#----------------------------------------------------------------------
	def __init__(self,parent):
		"""Constructor"""
		super(Drop_Label,self).__init__(parent)
		self.setAcceptDrops(True)
	#----------------------------------------------------------------------
	def dropEvent(self,event):
		""""""
		data = event.mimeData()
		fp = data.urls()[0].toString().replace("file:///","").replace("file://","")
		scan_and_replace_paths.run_scan_and_replace(fp)
		fp = os.path.join(fp,"Corrected")
		os.startfile(fp)
		super(Drop_Label,self).dropEvent(event)
		
	def dragEnterEvent(self, e):

		if e.mimeData().hasUrls():
			e.accept()
		else:
			e.ignore()
			
_UI_Loader.registerCustomWidget(Drop_Label)
		
def make_ui(parent=None):
	Qfile = QtCore.QFile(_ui_file)
	Qfile.open(QtCore.QFile.ReadOnly)
	ui_wig = _UI_Loader.load(Qfile)
	Qfile.close()
	if parent is not None:
		ui_wig.setParent(parent)
	return ui_wig


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	win = make_ui()
	#win.setWindowFlags(QtCore.Qt.WindowTitleHint)
	win.show()
	sys.exit(app.exec_())