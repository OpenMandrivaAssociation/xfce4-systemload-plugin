Summary:	System load plugin for the Xfce panel
Name:		xfce4-systemload-plugin
Version:	0.4.2
Release:	%mkrel 6
License:	BSD
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-systemload-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-systemload-plugin/%{name}-%{version}.tar.bz2
Patch0:		01_fix-bar-colors.patch
Patch1:		02_fix-wrong-free-memory-value.patch
Patch2:		%{name}-0.4.2-remove-extraneous-spacing.patch
Patch3:		%{name}-0.4.2-fix-uptime-polish-translation.patch
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	perl(XML::Parser)
Obsoletes:	xfce-systemload-plugin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A system load panel plugin for the Xfce Desktop Environment.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README ChangeLog AUTHORS
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*
