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


%changelog
* Sun Feb 05 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.7.4.1-1
+ Revision: 771303
- version update 0.7.4.1
- build fixes

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Wed Apr 21 2010 Funda Wang <fwang@mandriva.org> 0.7.3-8mdv2010.1
+ Revision: 537451
- rebuild

* Thu Jun 04 2009 Oden Eriksson <oeriksson@mandriva.com> 0.7.3-7mdv2010.0
+ Revision: 382717
- rebuilt against libnet 1.1.3

* Mon Feb 02 2009 Funda Wang <fwang@mandriva.org> 0.7.3-6mdv2009.1
+ Revision: 336422
- fix linkage

* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 0.7.3-5mdv2009.1
+ Revision: 298542
- sync with ettercap-0.7.3-26.fc10.src.rpm
- use _disable_ld_as_needed and _disable_ld_no_undefined due
  to old and ugly autopoo
- rebuilt against libpcap-1.0.0

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.7.3-2mdv2008.1
+ Revision: 170821
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 0.7.3-1mdv2008.1
+ Revision: 136407
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

