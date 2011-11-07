Summary:	Thai XITERM - VT102 emulator for X Window System with Thai support
Summary(pl.UTF-8):	Tajski XITERM - emulator VT102 dla systemu X Window z obsługą języka tajskiego
Name:		xiterm+thai
Version:	1.09
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://linux.thai.net/pub/thailinux/software/xiterm+thai/%{name}-%{version}.tar.gz
# Source0-md5:	7d3662c8604ec599a184f392a613bc8d
URL:		http://linux.thai.net/
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xiterm+thai is a color VT102 emulator for X Window System with Thai
support.

%description -l pl.UTF-8
xiterm+thai to kolorowy emulator VT102 dla systemu X Window z obsługą
języka tajskiego.

%prep
%setup -q

%build
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
%doc Changelog README.thai doc/{BUGS,COPYRIGHT.HISTORY,FAQ,HISTORY,README*,TODO}
%attr(755,root,root) %{_bindir}/xiterm+thai
%{_pixmapsdir}/xiterm+thai.png
%{_mandir}/man1/xiterm+thai.1*
