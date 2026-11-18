///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "MyProjectBase.h"

///////////////////////////////////////////////////////////////////////////

LoginFrame::LoginFrame( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );

	wxBoxSizer* bSizer1;
	bSizer1 = new wxBoxSizer( wxVERTICAL );

	nombre = new wxStaticText( this, wxID_ANY, _("Nombre:"), wxDefaultPosition, wxDefaultSize, 0 );
	nombre->Wrap( -1 );
	bSizer1->Add( nombre, 0, wxALL, 5 );

	nombreCTRL = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer1->Add( nombreCTRL, 0, wxALL, 5 );

	contraseñaCTRL = new wxStaticText( this, wxID_ANY, _("Contraseña:"), wxDefaultPosition, wxDefaultSize, 0 );
	contraseñaCTRL->Wrap( -1 );
	bSizer1->Add( contraseñaCTRL, 0, wxALL, 5 );

	ContraseñaCTRL = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer1->Add( ContraseñaCTRL, 0, wxALL, 5 );

	enviarBTN = new wxButton( this, wxID_ANY, _("Enviar"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer1->Add( enviarBTN, 0, wxALL, 5 );


	this->SetSizer( bSizer1 );
	this->Layout();

	this->Centre( wxBOTH );

	// Connect Events
	enviarBTN->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( LoginFrame::on_press ), NULL, this );
}

LoginFrame::~LoginFrame()
{
}
