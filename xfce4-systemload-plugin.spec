%define url_ver %(echo %{version} | cut -c 1-3 )

Summary:	System load plugin for the Xfce panel
Name:		xfce4-systemload-plugin
Version:	1.1.1
Release:	2
License:	BSD
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-systemload-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-systemload-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.7
BuildRequires:	xfce4-panel-devel >= 4.7
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig(libxfce4util-1.0)
BuildRequires:	pkgconfig(libxfcegui4-1.0)
BuildRequires:	pkgconfig(libxfce4ui-1) >= 4.7.0
Obsoletes:	xfce-systemload-plugin

%description
A system load panel plugin for the Xfce Desktop Environment.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std
chmod +x %{buildroot}%{_libdir}/xfce4/panel/plugins/*.so
%find_lang %{name}

%files -f %{name}.lang
%doc README ChangeLog AUTHORS
%{_libdir}/xfce4/panel/plugins/*
%{_datadir}/xfce4/panel/plugins/*


%changelog
* Tue Apr 17 2012 Crispin Boylan <crisb@mandriva.org> 1.0.0-3mdv2012.0
+ Revision: 791566
- Rebuild

* Mon Apr 09 2012 Crispin Boylan <crisb@mandriva.org> 1.0.0-2
+ Revision: 790058
- Rebuild for xfce 4.10

* Sun Dec 12 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.0-1mdv2011.0
+ Revision: 620597
- update to new version 1.0.0
- drop all patches
- update buildrequires
- update URL for Source0

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.2-11mdv2010.1
+ Revision: 543439
- rebuild for mdv 2010.1

* Mon Sep 21 2009 Thierry Vignaud <tv@mandriva.org> 0.4.2-10mdv2010.0
+ Revision: 446136
- rebuild

* Fri Mar 06 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.2-9mdv2009.1
+ Revision: 349480
- rebuild for xfce-4.6.0

* Sun Feb 01 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.2-8mdv2009.1
+ Revision: 336284
- drop patch 2, it looks ugly

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.2-7mdv2009.1
+ Revision: 295029
- rebuild for new Xfce4.6 beta1

* Sat Aug 09 2008 Thierry Vignaud <tv@mandriva.org> 0.4.2-6mdv2009.0
+ Revision: 269794
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 16 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.2-5mdv2009.0
+ Revision: 194752
- Patch2: remove not needed spacing
- Patch3: fix polish translation

* Wed Apr 16 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.2-4mdv2009.0
+ Revision: 194660
- Patch0: fix wrong bar colors on some gtk themes
- Patch1: fix wrong free memory value

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.2-3mdv2008.1
+ Revision: 110139
- correct buildrequires
- do not package COPYING file
- use upstream tarball name as a real name
- use upstream name

* Thu May 24 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.2-2mdv2008.0
+ Revision: 30479
- update url
- spec file clean

* Wed May 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.2-1mdv2008.0
+ Revision: 30256
- new version

