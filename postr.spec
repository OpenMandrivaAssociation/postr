%define oname postr

Summary:	Postr is a Flickr uploading tool for the GNOME desktop.
Name:		%{oname}
Version:	0.12.3
Release:	%mkrel 1
License:	LGPLv2+
Group:		Graphics
Url:		http://burtonini.com/blog/computers/postr
Source0:	http://burtonini.com/computing/%{oname}-%{version}.tar.gz
%py_requires -d
Requires:	pygtk2
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Postr is a Flickr uploading tool for the GNOME desktop, which aims to be simple to use but exposing enough of Flickr to be useful.

%prep
%setup -qn %{oname}-%{version}

%build
python setup.py build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

python setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README AUTHORS COPYING TODO
%{_bindir}/postr
%{_libdir}/nautilus/extensions*/python/%{oname}*
%{_iconsdir}/hicolor/*/apps/*
%{_datadir}/applications/*
%{python_sitearch}/%{oname}/*
%{python_sitearch}/*.egg-info
