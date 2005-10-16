Summary: A multi-purpose desktop calculator for GNU/Linux
Name: qalculate-gtk
Version: 0.8.2
Release: 4%{?dist}
License: GPL
Group: Applications/Engineering
URL: http://qalculate.sourceforge.net/
Source: http://dl.sf.net/qalculate/qalculate-gtk-%{version}.tar.gz
Patch0: qalculate-gtk-help_fix.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: libgnome-devel, libglade2-devel, libqalculate-devel
BuildRequires: gettext, desktop-file-utils, scrollkeeper
Requires: gnuplot
Requires(post): scrollkeeper
Requires(postun): scrollkeeper

%description
Qalculate! is a multi-purpose desktop calculator for GNU/Linux. It is
small and simple to use but with much power and versatility underneath.
Features include customizable functions, units, arbitrary precision, plotting.
This package provides a (GTK+) graphical interface for Qalculate! 

%prep
%setup -q
%patch0 -p0 -b .help_fix

%build
%configure 
make %{?_smp_mflags}
										
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

desktop-file-install --delete-original                   \
        --vendor fedora                                  \
        --dir %{buildroot}%{_datadir}/applications       \
	--mode 0644				         \
        --add-category X-Fedora                          \
        %{buildroot}%{_datadir}/applications/qalculate-gtk.desktop

%find_lang qalculate-gtk
rm -rf %{buildroot}/%{_bindir}/qalculate

install -D -m 0644 data/icon.xpm %{buildroot}%{_datadir}/pixmaps/qalculate.xpm

%post
scrollkeeper-update -q -o %{_datadir}/omf/qalculate-gtk || :

%postun
scrollkeeper-update -q || :

%clean
rm -rf %{buildroot}

%files -f qalculate-gtk.lang
%defattr(-, root, root, -)
%doc AUTHORS ChangeLog COPYING TODO
%doc %{_datadir}/gnome/help/qalculate-gtk/
%{_bindir}/qalculate-gtk
%{_datadir}/applications/fedora-qalculate-gtk.desktop
%{_datadir}/pixmaps/qalculate.xpm
%{_datadir}/omf/qalculate-gtk/
%{_datadir}/qalculate-gtk/

%changelog
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