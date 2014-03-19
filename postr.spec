%define debug_package %{nil}

Summary:	Flickr uploading tool for the GNOME desktop
Name:		postr
Version:	0.12.4
Release:	4
License:	GPLv2+
Group:		Graphics
Url:		http://projects.gnome.org/postr/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
BuildRequires:	python-devel
Requires:	pygtk2.0
Requires:       python-twisted-core
Requires:       python-twisted-web
Requires:       nautilus-python
Requires:	gnome-python-gconf

%description
Postr is a Flickr uploading tool for the GNOME desktop, which aims to
be simple to use but exposing enough of Flickr to be useful.

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

#gw the extensions must be in the arch-dependant dir:
%if %_lib != lib
mkdir -p %{buildroot}%{_libdir}
mv %{buildroot}%{_prefix}/lib/nautilus %{buildroot}%{_libdir}
%endif

%files
%doc README AUTHORS COPYING TODO
%{_bindir}/postr
%{_libdir}/nautilus/extensions*/python/%{name}*
%{_iconsdir}/hicolor/*/apps/*
%{_datadir}/applications/*
%{py_puresitedir}/%{name}/*
%{py_puresitedir}/*.egg-info
