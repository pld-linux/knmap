Summary:	KDE frontend to nmap
Summary(pl.UTF-8):	Frontend KDE do nmapa
Name:		knmap
Version:	2.1
Release:	1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/knmap/%{name}-%{version}.tar.bz2
# Source0-md5:	5b03d149b5d0694eae172507469c7cf6
Patch0:		%{name}-ac_am.patch
URL:		http://www.sourceforge.net/projects/knmap/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Knmap is a KDE-based interface to the 'nmap' facility available at
http://www.insecure.org/nmap/. The main Knmap window provides for the
entry of nmap options and the display of nmap-generated output.

%description -l pl.UTF-8
Knmap to oparty na KDE frontend do aplikacji nmap. Główne okno knmapa
dostarcza wygodnego interfejsu do opcji nmapa oraz wyświetla wynik
działania programu.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	kdelnkdir=%{_desktopdir} \

mv -f $RPM_BUILD_ROOT{%{_datadir}/applnk/Utilities,%{_desktopdir}}/knmap.desktop

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_iconsdir}/*/*/apps/*
%{_datadir}/apps/%{name}
