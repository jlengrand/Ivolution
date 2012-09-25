///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Jun 30 2011)
// http://www.wxformbuilder.org/
//
// PLEASE DO "NOT" EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "noname.h"

///////////////////////////////////////////////////////////////////////////

IvolutionTemplate::IvolutionTemplate( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );
	
	statusbar = this->CreateStatusBar( 2, wxST_SIZEGRIP, wxID_ANY );
	menubar = new wxMenuBar( 0 );
	filemenu = new wxMenu();
	wxMenuItem* exitmenu;
	exitmenu = new wxMenuItem( filemenu, wxID_ANY, wxString( wxT("Exit") ) + wxT('\t') + wxT("CTRL + q"), wxEmptyString, wxITEM_NORMAL );
	filemenu->Append( exitmenu );
	
	menubar->Append( filemenu, wxT("File") ); 
	
	aboutmenu = new wxMenu();
	wxMenuItem* helpmenu;
	helpmenu = new wxMenuItem( aboutmenu, wxID_ANY, wxString( wxT("Help") ) + wxT('\t') + wxT("CTRL + h"), wxEmptyString, wxITEM_NORMAL );
	aboutmenu->Append( helpmenu );
	
	wxMenuItem* aboutseparator;
	aboutseparator = aboutmenu->AppendSeparator();
	
	wxMenuItem* aboutmenu1;
	aboutmenu1 = new wxMenuItem( aboutmenu, wxID_ANY, wxString( wxT("About") ) + wxT('\t') + wxT("CTRL + F12"), wxEmptyString, wxITEM_NORMAL );
	aboutmenu->Append( aboutmenu1 );
	
	menubar->Append( aboutmenu, wxT("About") ); 
	
	this->SetMenuBar( menubar );
	
	toolbar = new wxAuiToolBar( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxAUI_TB_HORZ_LAYOUT );
	toolbar->SetToolBitmapSize( wxSize( 25,25 ) );
	toolbar->AddTool( wxID_ANY, wxT("Input"), wxBitmap( wxT("../Ivolution/ivolution/data/media/icons/folder_add_48.png"), wxBITMAP_TYPE_ANY ), wxNullBitmap, wxITEM_NORMAL, wxEmptyString, wxEmptyString, NULL ); 
	
	toolbar->AddTool( wxID_ANY, wxT("Settings"), wxBitmap( wxT("../Ivolution/ivolution/data/media/icons/spanner_48.png"), wxBITMAP_TYPE_ANY ), wxNullBitmap, wxITEM_NORMAL, wxEmptyString, wxEmptyString, NULL ); 
	
	toolbar->AddSeparator(); 
	
	toolbar->AddTool( wxID_ANY, wxT("Go!"), wxBitmap( wxT("../Ivolution/ivolution/data/media/icons/accepted_48.png"), wxBITMAP_TYPE_ANY ), wxNullBitmap, wxITEM_NORMAL, wxEmptyString, wxEmptyString, NULL ); 
	
	toolbar->AddTool( wxID_ANY, wxT("Stop!"), wxBitmap( wxT("../Ivolution/ivolution/data/media/icons/cancel_48.png"), wxBITMAP_TYPE_ANY ), wxNullBitmap, wxITEM_NORMAL, wxEmptyString, wxEmptyString, NULL ); 
	
	toolbar->AddSeparator(); 
	
	helptool = new wxHyperlinkCtrl( toolbar, wxID_ANY, wxT("Ivolution online"), wxT("http://jlengrand.github.com/FaceMovie/"), wxDefaultPosition, wxDefaultSize, wxHL_ALIGN_RIGHT );
	toolbar->AddControl( helptool );
	toolbar->Realize(); 
	
	wxFlexGridSizer* mainsizer;
	mainsizer = new wxFlexGridSizer( 3, 1, 0, 0 );
	mainsizer->AddGrowableCol( 0 );
	mainsizer->AddGrowableRow( 0 );
	mainsizer->SetFlexibleDirection( wxBOTH );
	mainsizer->SetNonFlexibleGrowMode( wxFLEX_GROWMODE_ALL );
	
	filelist = new wxListCtrl( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxLC_LIST );
	mainsizer->Add( filelist, 0, wxALL|wxEXPAND, 5 );
	
	progressgauge = new wxGauge( this, wxID_ANY, 100, wxDefaultPosition, wxDefaultSize, wxGA_HORIZONTAL );
	mainsizer->Add( progressgauge, 0, wxALL|wxEXPAND, 5 );
	
	this->SetSizer( mainsizer );
	this->Layout();
	
	this->Centre( wxBOTH );
}

IvolutionTemplate::~IvolutionTemplate()
{
}
