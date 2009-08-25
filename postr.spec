Summary:	Postr is a Flickr uploading tool for the GNOME desktop.
Name:		postr
Version:	0.12.3
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphics
Url:		http://burtonini.com/blog/computers/postr
Source0:	http://burtonini.com/computing/%{name}-%{version}.tar.gz
Patch0:		fix_upload_button.patch
%py_requires -d
Requires:	pygtk2.0
Requires:       python-twisted-core
Requires:       python-twisted-web
Requires:       nautilus-python
Requires:	gnome-python-gconf
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Postr is a Flickr uploading tool for the GNOME desktop, which aims to
be simple to use but exposing enough of Flickr to be useful.

%prep
%setup -q
%patch0 -p1

%build
python setup.py build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

python setup.py install --root=%{buildroot}

#gw the extensions must be in the arch-dependant dir:
%if %_lib != lib
mkdir -p %buildroot%_libdir
mv %buildroot%_prefix/lib/nautilus %buildroot%_libdir
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%if %mdkversion < 200900
%post  
%update_icon_cache hicolor
%postun
%clean_icon_cache hicolor
%endif

%files
%defattr(-,root,root)
%doc README AUTHORS COPYING TODO
%{_bindir}/postr
%{_libdir}/nautilus/extensions*/python/%{name}*
%{_iconsdir}/hicolor/*/apps/*
%{_datadir}/applications/*
%{py_puresitedir}/%{name}/*
%{py_puresitedir}/*.egg-info
