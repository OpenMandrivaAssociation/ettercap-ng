%define name ettercap-ng
%define version 0.7.3
%define release %mkrel 4

Summary: Ncurses/Gtk2 based sniffer/interceptor utility
Name: %{name}
Version: %{version}
Release: %{release}
Source:  http://ettercap.sourceforge.net/download/ettercap-NG-%{version}.tar.bz2
License: GPL 
Group: Networking/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:        http://ettercap.sourceforge.net/
BuildRequires: openssl-devel
Buildrequires: ncurses-devel
BuildRequires: gtk+2-devel
BuildRequires: pcre-devel
BuildRequires: libnet1.1.2-devel
BuildRequires:	libtool-devel
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	libpcap-devel

Provides: ettercap = %version-%release
# for compatibility
Provides: ettercap-NG = %version-%release
Obsoletes: ettercap < %version-%release
Obsoletes:	%mklibname %name 0
Provides:	%mklibname %name 0

%description
Ettercap is a network sniffer/interceptor/logger for ethernet 
LANs (both switched or not). It supports active and passive 
dissection of many protocols (even ciphered ones, like SSH and 
HTTPS). Data injection in an established connection and 
filtering (substitute or drop a packet) on the fly is also 
possible, keeping the connection sincronized. Many sniffing 
modes were implemented to give you a powerful and complete 
sniffing suite. Plugins are supported. It has the ability 
to check whether you are in a switched LAN or not, and to 
use OS fingerprints (active or passive) to let you know 
the geometry of the LAN. The passive scan of the lan retrives 
infos about: hosts in the lan, open ports, services version, 
type of the host (gateway, router or simple host) and 
extimated distance in hop.

%prep
%setup -q -n ettercap-NG-%{version}

%build

aclocal
libtoolize --copy --force
automake -a || :
autoconf

%configure2_5x \
	--disable-debug \
	--with-openssl=%{_prefix} \
	--enable-gtk \
	--enable-plugins
%make
%make plug-ins

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

rm -fr $RPM_BUILD_ROOT/%_datadir/doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS CHANGELOG INSTALL LICENSE README* THANKS TODO TODO.TESTING doc/*
%config(noreplace) %_sysconfdir/etter.conf
%{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/ettercap
%{_libexecdir}/ettercap


