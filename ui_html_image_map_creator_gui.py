# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'html_image_map_creator_dialog_base.ui'
#
# Created: Mon Jul 17 15:22:14 2017
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_HTMLImageMapCreatorGUI(object):
    def setupUi(self, HTMLImageMapCreatorGUI):
        HTMLImageMapCreatorGUI.setObjectName(_fromUtf8("HTMLImageMapCreatorGUI"))
        HTMLImageMapCreatorGUI.resize(921, 441)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(HTMLImageMapCreatorGUI.sizePolicy().hasHeightForWidth())
        HTMLImageMapCreatorGUI.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HTMLImageMapCreatorGUI.setWindowIcon(icon)
        HTMLImageMapCreatorGUI.setModal(True)
        self.gridLayout = QtGui.QGridLayout(HTMLImageMapCreatorGUI)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(HTMLImageMapCreatorGUI)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/html_image_map_creator.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 3, 1)
        self.line1 = QtGui.QFrame(HTMLImageMapCreatorGUI)
        self.line1.setMaximumSize(QtCore.QSize(2, 32767))
        self.line1.setFrameShape(QtGui.QFrame.VLine)
        self.line1.setFrameShadow(QtGui.QFrame.Sunken)
        self.line1.setFrameShape(QtGui.QFrame.VLine)
        self.line1.setFrameShadow(QtGui.QFrame.Sunken)
        self.line1.setObjectName(_fromUtf8("line1"))
        self.gridLayout.addWidget(self.line1, 0, 1, 3, 1)
        self.progressBar = QtGui.QProgressBar(HTMLImageMapCreatorGUI)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout.addWidget(self.progressBar, 3, 0, 1, 3)
        self.textEdit = QtGui.QTextEdit(HTMLImageMapCreatorGUI)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout.addWidget(self.textEdit, 0, 2, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(HTMLImageMapCreatorGUI)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 3)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.spinBoxInfo = QtGui.QSpinBox(HTMLImageMapCreatorGUI)
        self.spinBoxInfo.setEnabled(False)
        self.spinBoxInfo.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spinBoxInfo.setMinimum(-99)
        self.spinBoxInfo.setObjectName(_fromUtf8("spinBoxInfo"))
        self.gridLayout_3.addWidget(self.spinBoxInfo, 7, 1, 1, 1)
        self.txtDimensions = QtGui.QLabel(HTMLImageMapCreatorGUI)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtDimensions.sizePolicy().hasHeightForWidth())
        self.txtDimensions.setSizePolicy(sizePolicy)
        self.txtDimensions.setObjectName(_fromUtf8("txtDimensions"))
        self.gridLayout_3.addWidget(self.txtDimensions, 1, 1, 1, 3)
        self.lblLabelOffset = QtGui.QLabel(HTMLImageMapCreatorGUI)
        self.lblLabelOffset.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblLabelOffset.sizePolicy().hasHeightForWidth())
        self.lblLabelOffset.setSizePolicy(sizePolicy)
        self.lblLabelOffset.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lblLabelOffset.setBaseSize(QtCore.QSize(0, 0))
        self.lblLabelOffset.setObjectName(_fromUtf8("lblLabelOffset"))
        self.gridLayout_3.addWidget(self.lblLabelOffset, 5, 0, 1, 1)
        self.txtLayerName = QtGui.QLineEdit(HTMLImageMapCreatorGUI)
        self.txtLayerName.setEnabled(False)
        self.txtLayerName.setObjectName(_fromUtf8("txtLayerName"))
        self.gridLayout_3.addWidget(self.txtLayerName, 2, 1, 1, 3)
        self.featureTotal = QtGui.QLabel(HTMLImageMapCreatorGUI)
        self.featureTotal.setObjectName(_fromUtf8("featureTotal"))
        self.gridLayout_3.addWidget(self.featureTotal, 2, 4, 1, 1)
        self.chkBoxSelectedOnly = QtGui.QCheckBox(HTMLImageMapCreatorGUI)
        self.chkBoxSelectedOnly.setEnabled(False)
        self.chkBoxSelectedOnly.setObjectName(_fromUtf8("chkBoxSelectedOnly"))
        self.gridLayout_3.addWidget(self.chkBoxSelectedOnly, 11, 0, 1, 2)
        self.featureCount = QtGui.QLabel(HTMLImageMapCreatorGUI)
        self.featureCount.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.featureCount.sizePolicy().hasHeightForWidth())
        self.featureCount.setSizePolicy(sizePolicy)
        self.featureCount.setObjectName(_fromUtf8("featureCount"))
        self.gridLayout_3.addWidget(self.featureCount, 11, 1, 1, 4)
        self.lblInfoOffset = QtGui.QLabel(HTMLImageMapCreatorGUI)
        self.lblInfoOffset.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblInfoOffset.sizePolicy().hasHeightForWidth())
        self.lblInfoOffset.setSizePolicy(sizePolicy)
        self.lblInfoOffset.setObjectName(_fromUtf8("lblInfoOffset"))
        self.gridLayout_3.addWidget(self.lblInfoOffset, 7, 0, 1, 1)
        self.lblActiveLayer = QtGui.QLabel(HTMLImageMapCreatorGUI)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblActiveLayer.sizePolicy().hasHeightForWidth())
        self.lblActiveLayer.setSizePolicy(sizePolicy)
        self.lblActiveLayer.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lblActiveLayer.setObjectName(_fromUtf8("lblActiveLayer"))
        self.gridLayout_3.addWidget(self.lblActiveLayer, 2, 0, 1, 1)
        self.lblFilename = QtGui.QLabel(HTMLImageMapCreatorGUI)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblFilename.sizePolicy().hasHeightForWidth())
        self.lblFilename.setSizePolicy(sizePolicy)
        self.lblFilename.setMaximumSize(QtCore.QSize(130, 16777215))
        self.lblFilename.setObjectName(_fromUtf8("lblFilename"))
        self.gridLayout_3.addWidget(self.lblFilename, 3, 0, 1, 1)
        self.btnBrowse = QtGui.QPushButton(HTMLImageMapCreatorGUI)
        self.btnBrowse.setSizeIncrement(QtCore.QSize(0, 0))
        self.btnBrowse.setObjectName(_fromUtf8("btnBrowse"))
        self.gridLayout_3.addWidget(self.btnBrowse, 3, 4, 1, 1)
        self.chkBoxLabel = QtGui.QCheckBox(HTMLImageMapCreatorGUI)
        self.chkBoxLabel.setObjectName(_fromUtf8("chkBoxLabel"))
        self.gridLayout_3.addWidget(self.chkBoxLabel, 4, 0, 1, 1)
        self.cmbLabelAttributes = QtGui.QComboBox(HTMLImageMapCreatorGUI)
        self.cmbLabelAttributes.setEnabled(False)
        self.cmbLabelAttributes.setObjectName(_fromUtf8("cmbLabelAttributes"))
        self.gridLayout_3.addWidget(self.cmbLabelAttributes, 4, 1, 1, 4)
        self.chkBoxInfoBox = QtGui.QCheckBox(HTMLImageMapCreatorGUI)
        self.chkBoxInfoBox.setObjectName(_fromUtf8("chkBoxInfoBox"))
        self.gridLayout_3.addWidget(self.chkBoxInfoBox, 6, 0, 1, 1)
        self.cmbInfoBoxAttributes = QtGui.QComboBox(HTMLImageMapCreatorGUI)
        self.cmbInfoBoxAttributes.setEnabled(False)
        self.cmbInfoBoxAttributes.setObjectName(_fromUtf8("cmbInfoBoxAttributes"))
        self.gridLayout_3.addWidget(self.cmbInfoBoxAttributes, 6, 1, 1, 4)
        self.txtFileName = QtGui.QLineEdit(HTMLImageMapCreatorGUI)
        self.txtFileName.setObjectName(_fromUtf8("txtFileName"))
        self.gridLayout_3.addWidget(self.txtFileName, 3, 1, 1, 3)
        self.lblDimensions = QtGui.QLabel(HTMLImageMapCreatorGUI)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDimensions.sizePolicy().hasHeightForWidth())
        self.lblDimensions.setSizePolicy(sizePolicy)
        self.lblDimensions.setObjectName(_fromUtf8("lblDimensions"))
        self.gridLayout_3.addWidget(self.lblDimensions, 1, 0, 1, 1)
        self.spinBoxLabel = QtGui.QSpinBox(HTMLImageMapCreatorGUI)
        self.spinBoxLabel.setEnabled(False)
        self.spinBoxLabel.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spinBoxLabel.setMinimum(-99)
        self.spinBoxLabel.setObjectName(_fromUtf8("spinBoxLabel"))
        self.gridLayout_3.addWidget(self.spinBoxLabel, 5, 1, 1, 1)
        self.lblLabelPixel = QtGui.QLabel(HTMLImageMapCreatorGUI)
        self.lblLabelPixel.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblLabelPixel.sizePolicy().hasHeightForWidth())
        self.lblLabelPixel.setSizePolicy(sizePolicy)
        self.lblLabelPixel.setObjectName(_fromUtf8("lblLabelPixel"))
        self.gridLayout_3.addWidget(self.lblLabelPixel, 5, 2, 1, 2)
        self.lblInfoPixel = QtGui.QLabel(HTMLImageMapCreatorGUI)
        self.lblInfoPixel.setEnabled(False)
        self.lblInfoPixel.setObjectName(_fromUtf8("lblInfoPixel"))
        self.gridLayout_3.addWidget(self.lblInfoPixel, 7, 2, 1, 2)
        self.gridLayout.addLayout(self.gridLayout_3, 1, 2, 1, 1)

        self.retranslateUi(HTMLImageMapCreatorGUI)
        QtCore.QMetaObject.connectSlotsByName(HTMLImageMapCreatorGUI)

    def retranslateUi(self, HTMLImageMapCreatorGUI):
        HTMLImageMapCreatorGUI.setWindowTitle(_translate("HTMLImageMapCreatorGUI", "HTML Image Map Creator", None))
        self.textEdit.setHtml(_translate("HTMLImageMapCreatorGUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:10pt;\">This plugin will create an HTML file along with a corresponding PNG file taken from the current map view. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:6pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:10pt;\">- It can be used on any active (multi-)point or (multi-)polygon vector layer (GeoPackage, Shapefile etc.).</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:10pt;\">- The label and the body of the infobox will use the chosen field (attribute) as their text. An example of this is shown in the picture on the left.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:10pt;\">- The blue/orange arrows in the image indicate how the label and the infobox are moved from their anchor points, according to their offset values.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:10pt;\">- In the &quot;templates&quot; directory, you\'ll find the CSS/JS templates used in this plugin. Feel free to change them to suit your needs.</span></p></body></html>", None))
        self.lblLabelOffset.setText(_translate("HTMLImageMapCreatorGUI", "Label offset", None))
        self.chkBoxSelectedOnly.setText(_translate("HTMLImageMapCreatorGUI", "Selected features only", None))
        self.lblInfoOffset.setText(_translate("HTMLImageMapCreatorGUI", "Infobox offset", None))
        self.lblActiveLayer.setText(_translate("HTMLImageMapCreatorGUI", "Active layer", None))
        self.lblFilename.setText(_translate("HTMLImageMapCreatorGUI", "Export path and filename", None))
        self.btnBrowse.setText(_translate("HTMLImageMapCreatorGUI", "Browse", None))
        self.chkBoxLabel.setText(_translate("HTMLImageMapCreatorGUI", "Label", None))
        self.chkBoxInfoBox.setText(_translate("HTMLImageMapCreatorGUI", "Infobox body", None))
        self.txtFileName.setText(_translate("HTMLImageMapCreatorGUI", "Path and name without extension", None))
        self.lblDimensions.setText(_translate("HTMLImageMapCreatorGUI", "Map view size", None))
        self.lblLabelPixel.setText(_translate("HTMLImageMapCreatorGUI", "pixels", None))
        self.lblInfoPixel.setText(_translate("HTMLImageMapCreatorGUI", "pixels", None))

import html_image_map_creator_rc
