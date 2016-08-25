///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Jun 17 2015)
// http://www.wxformbuilder.org/
//
// PLEASE DO "NOT" EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#ifndef __NONAME_H__
#define __NONAME_H__

#include <wx/artprov.h>
#include <wx/xrc/xmlres.h>
#include <wx/string.h>
#include <wx/button.h>
#include <wx/gdicmn.h>
#include <wx/font.h>
#include <wx/colour.h>
#include <wx/settings.h>
#include <wx/sizer.h>
#include <wx/frame.h>
#include <wx/dataview.h>

///////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////
/// Class FrmMain
///////////////////////////////////////////////////////////////////////////////
class FrmMain : public wxFrame 
{
	private:
	
	protected:
		wxButton* btnPremios;
		wxButton* btnPulsa;
		
		// Virtual event handlers, overide them in your derived class
		virtual void btnPremiosOnButtonClick( wxCommandEvent& event ) { event.Skip(); }
		virtual void btnPulsaOnButtonClick( wxCommandEvent& event ) { event.Skip(); }
		
	
	public:
		
		FrmMain( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxT("Sorteo"), const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 200,300 ), long style = wxCAPTION|wxCLOSE_BOX|wxMINIMIZE|wxTAB_TRAVERSAL );
		
		~FrmMain();
	
};

///////////////////////////////////////////////////////////////////////////////
/// Class MyFrame2
///////////////////////////////////////////////////////////////////////////////
class MyFrame2 : public wxFrame 
{
	private:
	
	protected:
		wxDataViewListCtrl* m_dataViewListCtrl1;
		wxButton* btnAceptar;
	
	public:
		
		MyFrame2( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxEmptyString, const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 732,475 ), long style = wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );
		
		~MyFrame2();
	
};

#endif //__NONAME_H__
