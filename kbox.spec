Summary:	Blackbox client for kwin
Summary(pl):	Blackbox klient dla kwin
Name:		kbox
Version:	0.1
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	http://prdownloads.sourceforge.net/kbox/%{name}-%{version}.tar.gz
BuildRequires:	kdelibs-devel
BuildRequires:	kdebase-devel
Requires:	kdebase
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr/X11

%description

%description -l pl

%prep
%setup -q

%build
%{__make} -f Makefile.cvs
./configure --prefix=%{_prefix}
%{__make} RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
%attr(755,root,root) %{_libdir}/*
%{_datadir}/apps/kwin/*
