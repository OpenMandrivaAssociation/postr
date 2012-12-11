Summary:	Postr is a Flickr uploading tool for the GNOME desktop
Name:		postr
Version:	0.12.4
Release:	%mkrel 3
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
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Postr is a Flickr uploading tool for the GNOME desktop, which aims to
be simple to use but exposing enough of Flickr to be useful.

%prep
%setup -q

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


%changelog
* Mon Oct 31 2011 Götz Waschk <waschk@mandriva.org> 0.12.4-3mdv2012.0
+ Revision: 707977
- rebuild
- update build deps
- update URL

* Sat Oct 30 2010 Götz Waschk <waschk@mandriva.org> 0.12.4-2mdv2011.0
+ Revision: 590552
- rebuild for new python

* Fri Nov 06 2009 Götz Waschk <waschk@mandriva.org> 0.12.4-1mdv2010.1
+ Revision: 460726
- new version
- drop patch

* Tue Aug 25 2009 Götz Waschk <waschk@mandriva.org> 0.12.3-1mdv2010.0
+ Revision: 420833
- fix summary
- fix upload button
- fix installation on 64 bit
- fix license
- add missing deps

  + Eugeni Dodonov <eugeni@mandriva.com>
    - 0.12.3
    - Created package structure for postr.

