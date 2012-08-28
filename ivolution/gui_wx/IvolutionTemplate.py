# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 30 2011)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui

inputid = 1000
settingsid = 1001
startid = 1002
stopid = 1003
helpid = 1004

###########################################################################
## Class IvolutionTemplate
###########################################################################

class IvolutionTemplate ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 560,645 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		self.statusbar = self.CreateStatusBar( 2, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.menubar = wx.MenuBar( 0 )
		self.filemenu = wx.Menu()
		self.exititem = wx.MenuItem( self.filemenu, wx.ID_ANY, u"Exit"+ u"\t" + u"CTRL + q", wx.EmptyString, wx.ITEM_NORMAL )
		self.filemenu.AppendItem( self.exititem )

		self.menubar.Append( self.filemenu, u"File" )

		self.aboutmenu = wx.Menu()
		self.helpitem = wx.MenuItem( self.aboutmenu, wx.ID_ANY, u"Help"+ u"\t" + u"CTRL + h", wx.EmptyString, wx.ITEM_NORMAL )
		self.aboutmenu.AppendItem( self.helpitem )

		self.aboutmenu.AppendSeparator()

		self.aboutitem = wx.MenuItem( self.aboutmenu, wx.ID_ANY, u"About"+ u"\t" + u"CTRL + F12", wx.EmptyString, wx.ITEM_NORMAL )
		self.aboutmenu.AppendItem( self.aboutitem )

		self.menubar.Append( self.aboutmenu, u"About" )

		self.SetMenuBar( self.menubar )

		mainsizer = wx.FlexGridSizer( 4, 1, 0, 0 )
		mainsizer.AddGrowableCol( 0 )
		mainsizer.AddGrowableRow( 2 )
		mainsizer.SetFlexibleDirection( wx.BOTH )
		mainsizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )

		self.toolbar = wx.aui.AuiToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,25 ), wx.aui.AUI_TB_HORZ_LAYOUT )
		self.toolbar.SetToolBitmapSize( wx.Size( 25,25 ) )
		self.toolbar.SetMinSize( wx.Size( -1,25 ) )
		self.toolbar.SetMaxSize( wx.Size( -1,25 ) )

		self.toolbar.AddTool( inputid, u"Input", wx.Bitmap( u"../Ivolution/ivolution/data/media/icons/folder_add_48.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )


		self.toolbar.AddTool( settingsid, u"Settings", wx.Bitmap( u"../Ivolution/ivolution/data/media/icons/spanner_48.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )


		self.toolbar.AddSeparator()

		self.toolbar.AddTool( startid, u"Go!", wx.Bitmap( u"../Ivolution/ivolution/data/media/icons/accepted_48.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )


		self.toolbar.AddTool( stopid, u"Stop!", wx.Bitmap( u"../Ivolution/ivolution/data/media/icons/cancel_48.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )


		self.toolbar.AddSeparator()

		self.helptool = wx.HyperlinkCtrl( self.toolbar, helpid, u"Ivolution online", u"http://jlengrand.github.com/FaceMovie/", wx.DefaultPosition, wx.DefaultSize, wx.HL_ALIGN_RIGHT )
		self.toolbar.AddControl( self.helptool )
		self.toolbar.Realize()

		mainsizer.Add( self.toolbar, 0, wx.EXPAND|wx.TOP, 0 )

		inputfoldergrid = wx.FlexGridSizer( 1, 2, 0, 0 )
		inputfoldergrid.AddGrowableCol( 1 )
		inputfoldergrid.SetFlexibleDirection( wx.BOTH )
		inputfoldergrid.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.inputtextfixed = wx.StaticText( self, wx.ID_ANY, u"Chosen Folder : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inputtextfixed.Wrap( -1 )
		self.inputtextfixed.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )

		inputfoldergrid.Add( self.inputtextfixed, 0, wx.ALL, 5 )

		self.inputtextbox = wx.StaticText( self, wx.ID_ANY, u"~/Documents", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inputtextbox.Wrap( -1 )
		inputfoldergrid.Add( self.inputtextbox, 0, wx.ALL, 5 )

		mainsizer.Add( inputfoldergrid, 1, wx.EXPAND, 5 )

		self.filelist = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_LIST )
		mainsizer.Add( self.filelist, 0, wx.EXPAND, 5 )

		self.progressgauge = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		mainsizer.Add( self.progressgauge, 0, wx.ALL|wx.EXPAND, 5 )

		self.SetSizer( mainsizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.on_exit, id = self.exititem.GetId() )
		self.Bind( wx.EVT_MENU, self.on_help, id = self.helpitem.GetId() )
		self.Bind( wx.EVT_MENU, self.on_about, id = self.aboutitem.GetId() )
		self.Bind( wx.EVT_TOOL, self.on_input, id = inputid )
		self.Bind( wx.EVT_TOOL, self.on_settings, id = settingsid )
		self.Bind( wx.EVT_TOOL, self.on_start, id = startid )
		self.Bind( wx.EVT_TOOL, self.on_stop, id = stopid )
		self.helptool.Bind( wx.EVT_HYPERLINK, self.on_help )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def on_exit( self, event ):
		event.Skip()

	def on_help( self, event ):
		event.Skip()

	def on_about( self, event ):
		event.Skip()

	def on_input( self, event ):
		event.Skip()

	def on_settings( self, event ):
		event.Skip()

	def on_start( self, event ):
		event.Skip()

	def on_stop( self, event ):
		event.Skip()



