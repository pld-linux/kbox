Summary:	Blackbox client for kwin
Summary(pl):	Klient Blackboksa dla kwin
Name:		kbox
Version:	0.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/kbox/%{name}-%{version}.tar.gz
# Source0-md5:	a158f1a74c0af7863f7cf7aeb89ab05f
Source1:        http://ep09.pld-linux.org/~djurban/kde/kde-common-admin.tar.bz2
# Source1-md5:	81e0b2f79ef76218381270960ac0f55f
URL:		http://kbox.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel <= 9:3.2.0
BuildRequires:	kdebase-devel <= 9:3.2.0
BuildRequires:	sed >= 4.0
BuildRequires:	unsermake >= 040805
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Blackbox windows decorations support for kwin.

%description -l pl
Obs³uga dekoracji okien z Blackboksa dla kwin.

%prep
%setup -q -a1

%{__sed} -i -e 's,$(TOPSUBDIRS),blackbox,g' Makefile.am

%build
cp -f /usr/share/automake/config.sub admin
export UNSERMAKE=/usr/share/unsermake/unsermake

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
