# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.0.0-0-g0efcecf)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

BOX_SP_REQUEST = 2030

###########################################################################
## Class UiPersonalizedService
###########################################################################

class UiPersonalizedService ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		labelProcessInfo = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"Special Technique") ), wx.VERTICAL )

		fgSizer25 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer25.AddGrowableCol( 1 )
		fgSizer25.SetFlexibleDirection( wx.BOTH )
		fgSizer25.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.solder_paste_type_label = wx.StaticText( labelProcessInfo.GetStaticBox(), wx.ID_ANY, _(u"solder_paste_type"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.solder_paste_type_label.Wrap( -1 )

		fgSizer25.Add( self.solder_paste_type_label, 0, wx.ALL, 5 )

		solder_paste_typeChoices = []
		self.solder_paste_type = wx.Choice( labelProcessInfo.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, solder_paste_typeChoices, 0 )
		self.solder_paste_type.SetSelection( 0 )
		fgSizer25.Add( self.solder_paste_type, 0, wx.ALL|wx.EXPAND, 5 )

		self.is_assembly_weld_label = wx.StaticText( labelProcessInfo.GetStaticBox(), wx.ID_ANY, _(u"is_assembly_weld"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.is_assembly_weld_label.Wrap( -1 )

		fgSizer25.Add( self.is_assembly_weld_label, 0, wx.ALL, 5 )

		is_assembly_weldChoices = []
		self.is_assembly_weld = wx.Choice( labelProcessInfo.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, is_assembly_weldChoices, 0 )
		self.is_assembly_weld.SetSelection( 0 )
		fgSizer25.Add( self.is_assembly_weld, 0, wx.ALL|wx.EXPAND, 5 )

		self.x_ray_number_label = wx.StaticText( labelProcessInfo.GetStaticBox(), wx.ID_ANY, _(u"x_ray_number"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.x_ray_number_label.Wrap( -1 )

		fgSizer25.Add( self.x_ray_number_label, 0, wx.ALL, 5 )

		self.x_ray_number = wx.TextCtrl( labelProcessInfo.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer25.Add( self.x_ray_number, 0, wx.ALL|wx.EXPAND, 5 )

		self.x_ray_unit_number_label = wx.StaticText( labelProcessInfo.GetStaticBox(), wx.ID_ANY, _(u"x_ray_unit_number"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.x_ray_unit_number_label.Wrap( -1 )

		fgSizer25.Add( self.x_ray_unit_number_label, 0, wx.ALL, 5 )

		self.x_ray_unit_number = wx.TextCtrl( labelProcessInfo.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer25.Add( self.x_ray_unit_number, 0, wx.ALL|wx.EXPAND, 5 )

		self.is_layout_cleaning_label = wx.StaticText( labelProcessInfo.GetStaticBox(), wx.ID_ANY, _(u"is_layout_cleaning"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.is_layout_cleaning_label.Wrap( -1 )

		fgSizer25.Add( self.is_layout_cleaning_label, 0, wx.ALL, 5 )

		is_layout_cleaningChoices = []
		self.is_layout_cleaning = wx.Choice( labelProcessInfo.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, is_layout_cleaningChoices, 0 )
		self.is_layout_cleaning.SetSelection( 0 )
		fgSizer25.Add( self.is_layout_cleaning, 0, wx.ALL|wx.EXPAND, 5 )

		self.is_material_baking_label = wx.StaticText( labelProcessInfo.GetStaticBox(), wx.ID_ANY, _(u"is_material_baking"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.is_material_baking_label.Wrap( -1 )

		fgSizer25.Add( self.is_material_baking_label, 0, wx.ALL, 5 )

		is_material_bakingChoices = []
		self.is_material_baking = wx.Choice( labelProcessInfo.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, is_material_bakingChoices, 0 )
		self.is_material_baking.SetSelection( 0 )
		fgSizer25.Add( self.is_material_baking, 0, wx.ALL|wx.EXPAND, 5 )

		self.is_welding_wire_label = wx.StaticText( labelProcessInfo.GetStaticBox(), wx.ID_ANY, _(u"is_welding_wire"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.is_welding_wire_label.Wrap( -1 )

		fgSizer25.Add( self.is_welding_wire_label, 0, wx.ALL, 5 )

		is_welding_wireChoices = []
		self.is_welding_wire = wx.Choice( labelProcessInfo.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, is_welding_wireChoices, 0 )
		self.is_welding_wire.SetSelection( 0 )
		fgSizer25.Add( self.is_welding_wire, 0, wx.ALL|wx.EXPAND, 5 )

		self.is_test_label = wx.StaticText( labelProcessInfo.GetStaticBox(), wx.ID_ANY, _(u"functional test"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.is_test_label.Wrap( -1 )

		fgSizer25.Add( self.is_test_label, 0, wx.ALL, 5 )

		is_testChoices = []
		self.is_test = wx.Choice( labelProcessInfo.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, is_testChoices, 0 )
		self.is_test.SetSelection( 0 )
		fgSizer25.Add( self.is_test, 0, wx.ALL|wx.EXPAND, 5 )

		self.is_assemble_label = wx.StaticText( labelProcessInfo.GetStaticBox(), wx.ID_ANY, _(u"is_assemble"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.is_assemble_label.Wrap( -1 )

		fgSizer25.Add( self.is_assemble_label, 0, wx.ALL, 5 )

		is_assembleChoices = []
		self.is_assemble = wx.Choice( labelProcessInfo.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, is_assembleChoices, 0 )
		self.is_assemble.SetSelection( 0 )
		fgSizer25.Add( self.is_assemble, 0, wx.ALL|wx.EXPAND, 5 )

		self.is_program_burning_label = wx.StaticText( labelProcessInfo.GetStaticBox(), wx.ID_ANY, _(u"is_program_burning"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.is_program_burning_label.Wrap( -1 )

		fgSizer25.Add( self.is_program_burning_label, 0, wx.ALL, 5 )

		is_program_burningChoices = []
		self.is_program_burning = wx.Choice( labelProcessInfo.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, is_program_burningChoices, 0 )
		self.is_program_burning.SetSelection( 0 )
		fgSizer25.Add( self.is_program_burning, 0, wx.ALL|wx.EXPAND, 5 )

		self.need_split_label = wx.StaticText( labelProcessInfo.GetStaticBox(), wx.ID_ANY, _(u"need_split"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.need_split_label.Wrap( -1 )

		fgSizer25.Add( self.need_split_label, 0, wx.ALL, 5 )

		need_splitChoices = []
		self.need_split = wx.Choice( labelProcessInfo.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, need_splitChoices, 0 )
		self.need_split.SetSelection( 0 )
		fgSizer25.Add( self.need_split, 0, wx.ALL|wx.EXPAND, 5 )

		self.is_increase_tinning_label = wx.StaticText( labelProcessInfo.GetStaticBox(), wx.ID_ANY, _(u"is_increase_tinning"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.is_increase_tinning_label.Wrap( -1 )

		fgSizer25.Add( self.is_increase_tinning_label, 0, wx.ALL, 5 )

		is_increase_tinningChoices = []
		self.is_increase_tinning = wx.Choice( labelProcessInfo.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, is_increase_tinningChoices, 0 )
		self.is_increase_tinning.SetSelection( 0 )
		fgSizer25.Add( self.is_increase_tinning, 0, wx.ALL|wx.EXPAND, 5 )

		self.need_conformal_coating_label = wx.StaticText( labelProcessInfo.GetStaticBox(), wx.ID_ANY, _(u"need_conformal_coating"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.need_conformal_coating_label.Wrap( -1 )

		fgSizer25.Add( self.need_conformal_coating_label, 0, wx.ALL, 5 )

		need_conformal_coatingChoices = []
		self.need_conformal_coating = wx.Choice( labelProcessInfo.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, need_conformal_coatingChoices, 0 )
		self.need_conformal_coating.SetSelection( 0 )
		fgSizer25.Add( self.need_conformal_coating, 0, wx.ALL|wx.EXPAND, 5 )

		self.is_first_confirm_label = wx.StaticText( labelProcessInfo.GetStaticBox(), wx.ID_ANY, _(u"is_first_confirm"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.is_first_confirm_label.Wrap( -1 )

		fgSizer25.Add( self.is_first_confirm_label, 0, wx.ALL, 5 )

		is_first_confirmChoices = []
		self.is_first_confirm = wx.Choice( labelProcessInfo.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, is_first_confirmChoices, 0 )
		self.is_first_confirm.SetSelection( 0 )
		fgSizer25.Add( self.is_first_confirm, 0, wx.ALL|wx.EXPAND, 5 )

		self.packing_type_label = wx.StaticText( labelProcessInfo.GetStaticBox(), wx.ID_ANY, _(u"packing_type"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.packing_type_label.Wrap( -1 )

		fgSizer25.Add( self.packing_type_label, 0, wx.ALL, 5 )

		packing_typeChoices = []
		self.packing_type = wx.Choice( labelProcessInfo.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, packing_typeChoices, 0 )
		self.packing_type.SetSelection( 0 )
		fgSizer25.Add( self.packing_type, 0, wx.ALL|wx.EXPAND, 5 )


		labelProcessInfo.Add( fgSizer25, 0, wx.EXPAND, 5 )

		sp_box = wx.StaticBoxSizer( wx.StaticBox( labelProcessInfo.GetStaticBox(), BOX_SP_REQUEST, _(u"postscript") ), wx.VERTICAL )

		self.postscript = wx.TextCtrl( sp_box.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.postscript.SetMinSize( wx.Size( -1,60 ) )

		sp_box.Add( self.postscript, 1, wx.ALL|wx.EXPAND, 5 )


		labelProcessInfo.Add( sp_box, 1, wx.EXPAND, 5 )


		self.SetSizer( labelProcessInfo )
		self.Layout()
		labelProcessInfo.Fit( self )

	def __del__( self ):
		pass

