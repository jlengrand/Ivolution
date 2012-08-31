# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 30 2011)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class SettingsTemplate
###########################################################################

class SettingsTemplate ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Settings", pos = wx.DefaultPosition, size = wx.Size( 342,451 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        fgSizer4 = wx.FlexGridSizer( 2, 1, 0, 0 )
        fgSizer4.AddGrowableCol( 0 )
        fgSizer4.AddGrowableRow( 0 )
        fgSizer4.SetFlexibleDirection( wx.BOTH )
        fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_notebook4 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.basicPage = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        fgSizer5 = wx.FlexGridSizer( 2, 1, 0, 0 )
        fgSizer5.SetFlexibleDirection( wx.BOTH )
        fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        fgSizer9 = wx.FlexGridSizer( 2, 1, 0, 0 )
        fgSizer9.SetFlexibleDirection( wx.BOTH )
        fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.outputLocationTitle = wx.StaticText( self.basicPage, wx.ID_ANY, u"Choose location where the video will be saved: ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.outputLocationTitle.Wrap( -1 )
        self.outputLocationTitle.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )

        fgSizer9.Add( self.outputLocationTitle, 0, wx.ALL|wx.EXPAND, 5 )

        fgSizer7 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer7.AddGrowableCol( 0 )
        fgSizer7.SetFlexibleDirection( wx.BOTH )
        fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.outputLocationLabel = wx.StaticText( self.basicPage, wx.ID_ANY, u"C:/Toussa", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.outputLocationLabel.Wrap( -1 )
        fgSizer7.Add( self.outputLocationLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.outputButton = wx.Button( self.basicPage, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer7.Add( self.outputButton, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        fgSizer9.Add( fgSizer7, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_staticline1 = wx.StaticLine( self.basicPage, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        fgSizer9.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

        fgSizer5.Add( fgSizer9, 1, wx.EXPAND, 5 )

        fgSizer10 = wx.FlexGridSizer( 2, 1, 0, 0 )
        fgSizer10.SetFlexibleDirection( wx.BOTH )
        fgSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.OutputName = wx.StaticText( self.basicPage, wx.ID_ANY, u"Choose the name of the generated video:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.OutputName.Wrap( -1 )
        self.OutputName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )

        fgSizer10.Add( self.OutputName, 0, wx.ALL, 5 )

        fgSizer8 = wx.FlexGridSizer( 1, 2, 0, 0 )
        fgSizer8.AddGrowableCol( 0 )
        fgSizer8.SetFlexibleDirection( wx.BOTH )
        fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.outputText = wx.TextCtrl( self.basicPage, wx.ID_ANY, u"Ivolution", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        fgSizer8.Add( self.outputText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.extentLabel = wx.StaticText( self.basicPage, wx.ID_ANY, u".avi", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.extentLabel.Wrap( -1 )
        fgSizer8.Add( self.extentLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 10 )

        fgSizer10.Add( fgSizer8, 1, wx.EXPAND, 5 )

        fgSizer5.Add( fgSizer10, 1, wx.EXPAND, 5 )

        self.basicPage.SetSizer( fgSizer5 )
        self.basicPage.Layout()
        fgSizer5.Fit( self.basicPage )
        self.m_notebook4.AddPage( self.basicPage, u"Basic", False )
        self.advancedPage = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        fgSizer11 = wx.FlexGridSizer( 4, 1, 0, 0 )
        fgSizer11.SetFlexibleDirection( wx.BOTH )
        fgSizer11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        speedSizer = wx.FlexGridSizer( 2, 1, 0, 0 )
        speedSizer.SetFlexibleDirection( wx.BOTH )
        speedSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.speedLabel = wx.StaticText( self.advancedPage, wx.ID_ANY, u"Choose the speed of the video :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.speedLabel.Wrap( -1 )
        self.speedLabel.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )

        speedSizer.Add( self.speedLabel, 0, wx.ALL, 5 )

        speedComboChoices = [ u"Slow", u"Medium", u"Fast" ]
        self.speedCombo = wx.ComboBox( self.advancedPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, speedComboChoices, wx.CB_READONLY )
        speedSizer.Add( self.speedCombo, 0, wx.ALL|wx.EXPAND, 5 )

        fgSizer11.Add( speedSizer, 1, wx.EXPAND, 10 )

        self.m_staticline2 = wx.StaticLine( self.advancedPage, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        fgSizer11.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

        modeSizer = wx.FlexGridSizer( 2, 1, 0, 0 )
        modeSizer.SetFlexibleDirection( wx.BOTH )
        modeSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.modeLabel = wx.StaticText( self.advancedPage, wx.ID_ANY, u"Choose the mode for processing pictures:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.modeLabel.Wrap( -1 )
        self.modeLabel.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )

        modeSizer.Add( self.modeLabel, 0, wx.ALL, 5 )

        gSizer7 = wx.GridSizer( 1, 2, 0, 0 )

        modeRadioBoxChoices = [ u"Conservative", u"Crop" ]
        self.modeRadioBox = wx.RadioBox( self.advancedPage, wx.ID_ANY, u"Available modes", wx.DefaultPosition, wx.DefaultSize, modeRadioBoxChoices, 1, wx.RA_SPECIFY_ROWS )
        self.modeRadioBox.SetSelection( 0 )
        gSizer7.Add( self.modeRadioBox, 0, wx.ALL, 5 )

        modeSizer.Add( gSizer7, 1, wx.EXPAND, 5 )

        fgSizer11.Add( modeSizer, 1, wx.EXPAND, 5 )

        self.m_staticline3 = wx.StaticLine( self.advancedPage, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        fgSizer11.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )

        typeSizer = wx.FlexGridSizer( 2, 1, 0, 0 )
        typeSizer.SetFlexibleDirection( wx.BOTH )
        typeSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.typeLabel = wx.StaticText( self.advancedPage, wx.ID_ANY, u"Choose the type of faces for the video :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.typeLabel.Wrap( -1 )
        self.typeLabel.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )

        typeSizer.Add( self.typeLabel, 0, wx.ALL, 5 )

        typeComboChoices = [ u"frontal_face", u"profile_face" ]
        self.typeCombo = wx.ComboBox( self.advancedPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, typeComboChoices, wx.CB_READONLY )
        typeSizer.Add( self.typeCombo, 0, wx.ALL, 5 )

        fgSizer11.Add( typeSizer, 1, wx.EXPAND, 5 )

        self.m_staticline4 = wx.StaticLine( self.advancedPage, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        fgSizer11.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )

        sortSizer = wx.FlexGridSizer( 2, 1, 0, 0 )
        sortSizer.SetFlexibleDirection( wx.BOTH )
        sortSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.sortLabel = wx.StaticText( self.advancedPage, wx.ID_ANY, u"Choose the method used to sort images:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.sortLabel.Wrap( -1 )
        self.sortLabel.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )

        sortSizer.Add( self.sortLabel, 0, wx.ALL, 5 )

        sortRadioBoxChoices = [ u"FileName", u"EXIF Metadata" ]
        self.sortRadioBox = wx.RadioBox( self.advancedPage, wx.ID_ANY, u"Available methods", wx.DefaultPosition, wx.DefaultSize, sortRadioBoxChoices, 1, wx.RA_SPECIFY_ROWS )
        self.sortRadioBox.SetSelection( 0 )
        sortSizer.Add( self.sortRadioBox, 0, wx.ALL, 5 )

        fgSizer11.Add( sortSizer, 1, wx.EXPAND, 5 )

        self.advancedPage.SetSizer( fgSizer11 )
        self.advancedPage.Layout()
        fgSizer11.Fit( self.advancedPage )
        self.m_notebook4.AddPage( self.advancedPage, u"Advanced", True )

        fgSizer4.Add( self.m_notebook4, 1, wx.ALL|wx.EXPAND, 5 )

        gSizer4 = wx.GridSizer( 0, 2, 0, 0 )

        self.cancelButton = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer4.Add( self.cancelButton, 0, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.saveButton = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer4.Add( self.saveButton, 0, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        fgSizer4.Add( gSizer4, 1, wx.ALIGN_BOTTOM|wx.EXPAND, 10 )

        self.SetSizer( fgSizer4 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.outputButton.Bind( wx.EVT_BUTTON, self.on_output )
        self.cancelButton.Bind( wx.EVT_BUTTON, self.on_cancel )
        self.saveButton.Bind( wx.EVT_BUTTON, self.on_save )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def on_output( self, event ):
        event.Skip()

    def on_cancel( self, event ):
        event.Skip()

    def on_save( self, event ):
        event.Skip()


