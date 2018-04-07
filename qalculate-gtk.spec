
# This spec file uses tab uniformly. If you touch this spec, ensure that
# you use tab in your changes.

%global srcnm Qalculate

Summary:	A multi-purpose desktop calculator for GNU/Linux
Name:		qalculate-gtk
Version:	2.2.1
Release:	1%{?dist}
License:	GPLv2+

URL:		https://qalculate.github.io/
Source0:	https://github.com/%{srcnm}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

Patch0:		qalculate-gtk-desktop.patch

BuildRequires:	gcc-c++
BuildRequires:	libgnome-devel
BuildRequires:	libglade2-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	libqalculate-devel
BuildRequires:	gettext
BuildRequires:	desktop-file-utils
BuildRequires:	scrollkeeper
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig
BuildRequires:	intltool
BuildRequires:	libappstream-glib
BuildRequires:	mpfr-devel
Requires:	gnuplot

%description
Qalculate! is a multi-purpose desktop calculator for GNU/Linux. It is
small and simple to use but with much power and versatility underneath.
Features include customizable functions, units, arbitrary precision, plotting.
This package provides a (GTK+) graphical interface for Qalculate! 

%prep
%setup -q
%patch0 -p0 -b .desktop

%build
%configure 
%make_build

%install
%make_install

desktop-file-install --delete-original			\
	--remove-category Application			\
	--dir %{buildroot}%{_datadir}/applications	\
	--mode 0644					\
	%{buildroot}%{_datadir}/applications/qalculate-gtk.desktop

appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog TODO
%{_defaultdocdir}/qalculate-gtk
%{_bindir}/qalculate-gtk
%{_datadir}/applications/qalculate-gtk.desktop
%{_datadir}/pixmaps/qalculate.png
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
* Sat Mar 10 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.2.1-1
- Update to 2.2.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 15 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0
- Add mpfr-devel as BR

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 28 2017 Mukundan Ragavan <nonamedotc@gmail.com> - 0.9.9-2
- rebuilt

* Mon Nov 28 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.9.9-1
- Update to 0.9.9
- spec file cleanup

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.7-12
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 24 2014 Deji Akingunola <dakingun@gmail.com> - 0.9.7-9
- Apply the Debian patch to fix the format-security build error (Bug 1037265)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 22 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.9.7-7
- Remove --vendor from desktop-file-install https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.9.7-3
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 29 2010 Deji Akingunola <dakingun@gmail.com> - 0.9.7-1
- Update to 0.9.7

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jul 05 2009 Deji Akingunola <dakingun@gmail.com> - 0.9.6-6
- Rebuild for cln-1.3.0

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Deji Akingunola <dakingun@gmail.com> - 0.9.6-4
- Rebuild (with patch) for cln-1.2

* Sun Feb 10 2008 Deji Akingunola <dakingun@gmail.com> - 0.9.6-3
- Rebuild for gcc43

* Sat Aug 25 2007 Deji Akingunola <dakingun@gmail.com> - 0.9.6-2
- Rebuild

* Fri Aug 03 2007 Deji Akingunola <dakingun@gmail.com> - 0.9.6-2
- License tag update

* Sun Jul 01 2007 Deji Akingunola <dakingun@gmail.com> - 0.9.6-1
- Update to new release

* Sat Jun 09 2007 Deji Akingunola <dakingun@gmail.com> - 0.9.5-2
- Modify the Name field in the desktop file to distinguish it from that of
  qalculate-kde (BZ #241024)
- Require 'yelp' for the Help menu (BZ #243395)

* Tue Jan 02 2007 Deji Akingunola <dakingun@gmail.com> - 0.9.5-1
- New release

* Wed Aug 30 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.4-5
- Add perl(XML::Parser) BR

* Mon Aug 28 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.4-4
- Rebuild for FC6

* Wed Jun 28 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.4-3
- Properly package up missing file

* Wed Jun 28 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.4-2
- Add missing BR on libgnomeui

* Tue Jun 27 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.4-1
- New version 0.9.4

* Thu Mar 30 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.3-1
- Update to newer version

* Mon Feb 13 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.2-2
- Rebuild for Fedora Extras 5

* Tue Dec 27 2005 Deji Akingunola <dakingun@gmail.com> - 0.9.2-1
- Upgrade to new version

* Sat Nov 05 2005 Deji Akingunola <dakingun@gmail.com> - 0.9.0.1
- Upgrade to new version

* Wed Nov 2 2005 Deji Akingunola <deji.aking@gmail.com> - 0.8.2.1-2
- Rebuild with new cln package

* Thu Oct 13 2005 Deji Akingunola <deji.aking@gmail.com> - 0.8.2.1-2
- Update to a new release that handles new behaviour in pango >= 1.10.0

* Thu Oct 13 2005 Deji Akingunola <deji.aking@gmail.com> - 0.8.2-4
- Fix for yelp error (Niklas Knutsson)

* Thu Oct 13 2005 Deji Akingunola <deji.aking@gmail.com> - 0.8.2-3
- Rmove explicit requires for gnome-vfs2 and libqalculate
- Install desktop file properly

* Tue Oct 11 2005 Paul Howarth <paul@city-fan.org> - 0.8.2-2
- Use "make DESTDIR=%%{buildroot}" instead of %%makeinstall
- Expand most references to %%{name} for clarity
- Make sure scriptlets complete successfully
- Add scriptlet deps
- Include license text
- Remove redundant doc files NEWS & README
- Fix directory ownership

* Tue Oct 11 2005 Deji Akingunola <deji.aking@gmail.com> - 0.8.2-1
- Upgraded to new version
- Remove redundant buildrequires - make libglade2 requires them all
- Remove the -export-dynamic configure option, now done upstream
- Add gnome-vfs2 to require.
- Install the desktop file

* Wed Oct 05 2005 Deji Akingunola <deji.aking@gmail.com> - 0.8.1
- Initial package
