Summary:	Blackbox client for kwin
Summary(pl):	Klient Blackboksa dla kwin
Name:		kbox
Version:	0.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/kbox/%{name}-%{version}.tar.gz
# Source0-md5:	f7cea66964f6959b4649356c65f949fb
URL:		http://kbox.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	kdebase-devel
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Blackbox client for kwin.

%description -l pl
Klient Blackboksa dla kwin.

%prep
%setup -q

%build
%{__make} -f Makefile.cvs
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*
%{_datadir}/apps/kwin/*
