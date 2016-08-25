///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Jun 17 2015)
// http://www.wxformbuilder.org/
//
// PLEASE DO "NOT" EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "noname.h"

///////////////////////////////////////////////////////////////////////////

FrmMain::FrmMain( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxSize( 200,300 ), wxSize( 200,300 ) );
	
	wxBoxSizer* bSizer1;
	bSizer1 = new wxBoxSizer( wxVERTICAL );
	
	btnPremios = new wxButton( this, wxID_ANY, wxT("Premios"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer1->Add( btnPremios, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	btnPulsa = new wxButton( this, wxID_ANY, wxT("Registro de Pulsaciones"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer1->Add( btnPulsa, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	
	this->SetSizer( bSizer1 );
	this->Layout();
	
	this->Centre( wxBOTH );
	
	// Connect Events
	btnPremios->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( FrmMain::btnPremiosOnButtonClick ), NULL, this );
	btnPulsa->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( FrmMain::btnPulsaOnButtonClick ), NULL, this );
}

FrmMain::~FrmMain()
{
	// Disconnect Events
	btnPremios->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( FrmMain::btnPremiosOnButtonClick ), NULL, this );
	btnPulsa->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( FrmMain::btnPulsaOnButtonClick ), NULL, this );
	
}

MyFrame2::MyFrame2( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );
	
	wxBoxSizer* bSizer2;
	bSizer2 = new wxBoxSizer( wxVERTICAL );
	
	m_dataViewListCtrl1 = new wxDataViewListCtrl( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer2->Add( m_dataViewListCtrl1, 1, wxALL|wxEXPAND, 5 );
	
	wxBoxSizer* bSizer5;
	bSizer5 = new wxBoxSizer( wxVERTICAL );
	
	wxBoxSizer* bSizer6;
	bSizer6 = new wxBoxSizer( wxHORIZONTAL );
	
	btnAceptar = new wxButton( this, wxID_ANY, wxT("Aceptar"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer6->Add( btnAceptar, 0, wxALL, 5 );
	
	
	bSizer5->Add( bSizer6, 0, 0, 5 );
	
	
	bSizer2->Add( bSizer5, 0, wxALIGN_RIGHT, 5 );
	
	
	this->SetSizer( bSizer2 );
	this->Layout();
	
	this->Centre( wxBOTH );
}

MyFrame2::~MyFrame2()
{
}
