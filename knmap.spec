Summary:	kde frontend to nmap
Summary(pl):	frontend kde do nmap
Name:		knmap
Version:	2.0
Release:	0.beta1.1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/knmap/%{name}-%{version}-beta-1.tar.bz2
# Source0-md5:	9d7ccbde9e2a2fc818393535332809d1
URL:		http://www.sourceforge.net/projects/knmap/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Knmap is a KDE-based interface to the 'nmap' facility available at
http://www.insecure.org/nmap. The main Knmap window provides for the
entry of nmap options and the display of nmap-generated output.

%description -l pl
Knmap to oparty na KDE frontend do aplikacji nmap. G��wne okno knmap
dostarcza wygodnego interfejsu do opcji nmapa oraz wy�wietla wynik
dzia�ania programu.

%prep
%setup -q

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
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
%{_iconsdir}/*/*/apps/*
%{_datadir}/apps/%{name}