%define debug_package %{nil}
%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	Postr is a Flickr uploading tool for the GNOME desktop
Name:		postr
Version:	0.13.1
Release:	4
License:	GPLv2+
Group:		Graphics
Url:		https://projects.gnome.org/postr/
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(nautilus-python) >= 0.6.1
BuildRequires:	pkgconfig(pygtk-2.0)
BuildRequires:	intltool
BuildRequires:	gnome-doc-utils
BuildRequires:	pkgconfig(gnome-doc-utils)
Requires:	pygtk2.0
Requires:	python-twisted-core
Requires:	python-twisted-web
Requires:	nautilus-python
Requires:	gnome-python-gconf

%description
Postr is a Flickr uploading tool for the GNOME desktop, which aims to
be simple to use but exposing enough of Flickr to be useful.

%prep
%setup -q

%build
%configure2_5x --with-nautilus-extension-dir=%{_datadir}/nautilus-python/extensions
%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc README AUTHORS COPYING TODO
%{_bindir}/postr
%{_iconsdir}/hicolor/*/apps/*
%{_datadir}/applications/*
%{_datadir}/nautilus-python/extensions/*
%{py_puresitedir}/%{name}


