///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Jun 30 2011)
// http://www.wxformbuilder.org/
//
// PLEASE DO "NOT" EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#ifndef __NONAME_H__
#define __NONAME_H__

#include <wx/artprov.h>
#include <wx/xrc/xmlres.h>
#include <wx/statusbr.h>
#include <wx/string.h>
#include <wx/gdicmn.h>
#include <wx/font.h>
#include <wx/colour.h>
#include <wx/settings.h>
#include <wx/bitmap.h>
#include <wx/image.h>
#include <wx/icon.h>
#include <wx/menu.h>
#include <wx/hyperlink.h>
#include <wx/aui/auibar.h>
#include <wx/listctrl.h>
#include <wx/gauge.h>
#include <wx/sizer.h>
#include <wx/frame.h>

///////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////
/// Class IvolutionTemplate
///////////////////////////////////////////////////////////////////////////////
class IvolutionTemplate : public wxFrame 
{
	private:
	
	protected:
		wxStatusBar* statusbar;
		wxMenuBar* menubar;
		wxMenu* filemenu;
		wxMenu* aboutmenu;
		wxAuiToolBar* toolbar;
		wxHyperlinkCtrl* helptool;
		wxListCtrl* filelist;
		wxGauge* progressgauge;
	
	public:
		
		IvolutionTemplate( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxEmptyString, const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 560,451 ), long style = wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );
		
		~IvolutionTemplate();
	
};

#endif //__NONAME_H__
