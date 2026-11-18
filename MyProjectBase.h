///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#pragma once

#include <wx/artprov.h>
#include <wx/xrc/xmlres.h>
#include <wx/intl.h>
#include <wx/string.h>
#include <wx/stattext.h>
#include <wx/gdicmn.h>
#include <wx/font.h>
#include <wx/colour.h>
#include <wx/settings.h>
#include <wx/textctrl.h>
#include <wx/button.h>
#include <wx/bitmap.h>
#include <wx/image.h>
#include <wx/icon.h>
#include <wx/sizer.h>
#include <wx/frame.h>

///////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
/// Class LoginFrame
///////////////////////////////////////////////////////////////////////////////
class LoginFrame : public wxFrame
{
	private:

	protected:
		wxStaticText* nombre;
		wxTextCtrl* nombreCTRL;
		wxStaticText* contraseñaCTRL;
		wxTextCtrl* ContraseñaCTRL;
		wxButton* enviarBTN;

		// Virtual event handlers, override them in your derived class
		virtual void on_press( wxCommandEvent& event ) { event.Skip(); }


	public:

		LoginFrame( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = _("GymOS"), const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 281,300 ), long style = wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );

		~LoginFrame();

};

