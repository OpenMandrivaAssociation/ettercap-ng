Summary: Ncurses/Gtk2 based sniffer/interceptor utility
Name: ettercap-ng
Version: 0.7.4.1
Release: 1
Source:  http://ettercap.sourceforge.net/download/ettercap-%{version}.tar.gz
Patch0: ettercap-NG-0.7.3-UI.patch
Patch1: ettercap-NG-0.7.3-ec_log.patch
Patch2: ettercap-NG-0.7.3-daemon-ui.patch
Patch3: ettercap-NG-0.7.3-daemon-textmode.patch
Patch4: ettercap-NG-0.7.3-mitm-loop.patch
Patch5: ettercap-NG-0.7.3-linkage.patch
License: GPL 
Group: Networking/Other
URL:        http://ettercap.sourceforge.net/
BuildRequires: openssl-devel
Buildrequires: ncurses-devel
BuildRequires: gtk+2-devel
BuildRequires: pcre-devel
BuildRequires:	net-devel >= 1.1.3
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
%setup -q -n ettercap
%patch0 -p1
#%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p1 -b .link

%build
autoreconf -fi
libtoolize --copy --force
%configure2_5x \
	--disable-debug \
	--with-openssl=%{_prefix} \
	--enable-gtk \
	--without-included-ltdl \
	--disable-ltdl-install \
	--enable-plugins
%make
%make plug-ins

%install
%makeinstall_std

%files
%doc AUTHORS CHANGELOG INSTALL LICENSE README* THANKS TODO TODO.TESTING doc/*
%config(noreplace) %_sysconfdir/etter.conf
%{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/ettercap
%{_libexecdir}/ettercap
