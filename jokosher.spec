%define mainver %(echo %{version} | sed -e "s/\\([0-9]*\\.[0-9]*\\).[0-9]*/\\1/")

Summary:	Simple yet powerful multi-track studio
Name:		jokosher
Version:	0.11.4
Release:	%mkrel 2
Group:		Sound
License:	GPLv2+
URL:		http://jokosher.org
Source0:	http://launchpad.net/jokosher/%{mainver}/%{version}/+download/%{name}-%{version}.tar.gz
BuildRequires:	python-devel >= %{py_ver}
BuildRequires:	desktop-file-utils
BuildRequires:	python-setuptools
BuildRequires:	gettext
BuildRequires:	scrollkeeper
Requires:	python-dbus
Requires:	gnonlin >= 0.10.8
Requires:	gstreamer0.10-plugins-base >= 0.10.11
Requires:	gstreamer0.10-plugins-good >= 0.10.4
Requires:	gstreamer0.10-python
Requires:	gstreamer0.10-plugins-ugly >= 0.10.6
Requires:	gstreamer0.10-plugins-bad >= 0.10.5
Requires:	gnome-python
Requires:	pygtk2.0-libglade
%if %mdkversion > 200900
Requires:	python-pkg-resources
%else
Requires:	python-setuptools
%endif
Requires:	python-pyxml
Requires:	yelp
Requires:	ladspa
Requires(post):	scrollkeeper
Requires(postun): scrollkeeper
Obsoletes:	%{name} < 0.9
BuildArch:	noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Jokosher is a simple and poweful multi-track studio.Jokosher provides 
a complete application for recording, editing, mixing and exporting audio,
and has been specifically designed with usability in mind. The developers 
behind Jokosher have re-thought audio production at every level, and created 
something devilishly simple to use.

Jokosher offers a strong featureset:
* Easy to use interface, designed from the ground up. Jokosher uses concepts 
  and language familiar to musicians, and is a breeze to use.
* Simple editing with splitting, trimming and moving tools.
* Multi-track volume mixing with VU sliders.
* Import audio (Ogg Vorbis, MP3, FLAC, WAV and anything else supported by 
  GStreamer) into your projects.
* A range of instruments can be added to a project, and instruments can be 
  renamed.Instruments can also be muted and soloed easily.
* Export to MP3, Ogg Vorbis, FLAC, WAV and anything else GStreamer supports.
* Documentation (User Guide, FAQ, Tutorial) and User Community (Forums, IRC).

%prep
%setup -q

sed -i '1d' Jokosher/JokosherApp.py
sed -i s/"Version=0.9"/"Version=1.0"/g bin/jokosher.desktop

%build
python setup.py build

%install
python setup.py install --skip-build --root=%{buildroot}

perl -pi -e 's,%{name}-icon.png,%{name}-icon,g' %{buildroot}%{_datadir}/applications/*

desktop-file-install \
    --remove-category="Application" \
    --remove-category="AudioVideo" \
    --add-category="Audio;Recorder;X-MandrivaLinux-CrossDesktop;" \
    --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

chmod 755 %{buildroot}%{py_sitedir}/Jokosher/Profiler.py

#(tpg) wtf?
#mkdir -p %{buildroot}%{_datadir}/omf/%{name}
#mv -f %{buildroot}%{_prefix}/jokosher/* %{buildroot}%{_datadir}/omf/%{name}

%find_lang %{name}

%if %mdkversion < 200900
%post
%{update_menus}
%{update_desktop_database}
%{update_mime_database}
%{update_scrollkeeper}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_desktop_database}
%{clean_mime_database}
%{clean_scrollkeeper}
%clean_icon_cache hicolor
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING README help/*
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/Instruments
%dir %{_datadir}/%{name}/Instruments/images
%dir %{_datadir}/%{name}/extensions
%dir %{_datadir}/%{name}/pixmaps
%dir %{_datadir}/omf/%{name}
%dir %{py_sitedir}/Jokosher
%dir %{py_sitedir}/Jokosher/elements
%dir %{py_sitedir}/Jokosher/ui
%dir %{py_sitedir}/Jokosher/PlatformUtils
%{py_sitedir}/Jokosher/*.py*
%{py_sitedir}/Jokosher/elements/*.py*
%{py_sitedir}/Jokosher/PlatformUtils/*.py*
%{py_sitedir}/Jokosher/ui/*.py*
%{py_sitedir}/%{name}*egg-info
%{_datadir}/applications/jokosher.desktop
%{_datadir}/gnome/help/jokosher/C/figures/*.png
%{_datadir}/gnome/help/jokosher/C/*.xml
%{_datadir}/omf/jokosher/jokosher-C.omf
%{_iconsdir}/hicolor/*/apps/*.png
%{_datadir}/jokosher/Instruments/*.instr
%{_datadir}/jokosher/Instruments/images/*.png
%{_datadir}/jokosher/Jokosher.glade
%{_datadir}/jokosher/extensions/*py*
%{_datadir}/jokosher/jokosher-logo.png
%{_datadir}/jokosher/pixmaps/*.png
%{_datadir}/mime/packages/jokosher.xml
%{_datadir}/pixmaps/jokosher.png


%changelog
* Tue Nov 02 2010 Michael Scherer <misc@mandriva.org> 0.11.4-2mdv2011.0
+ Revision: 592408
- rebuild for python 2.7

* Mon Mar 01 2010 Frederik Himpe <fhimpe@mandriva.org> 0.11.4-1mdv2010.1
+ Revision: 513256
- update to new version 0.11.4

* Sat Jun 13 2009 Frederik Himpe <fhimpe@mandriva.org> 0.11.3-1mdv2010.0
+ Revision: 385721
- update to new version 0.11.3

* Wed May 13 2009 Frederik Himpe <fhimpe@mandriva.org> 0.11.2-1mdv2010.0
+ Revision: 375514
- Update to new version 0.11.2
- Fix source URL

* Tue May 12 2009 Frederik Himpe <fhimpe@mandriva.org> 0.11-2mdv2010.0
+ Revision: 374978
- rebuild

* Sun Mar 08 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.11-1mdv2009.1
+ Revision: 352867
- update to new version 0.11
- fix file list

* Mon Dec 29 2008 Götz Waschk <waschk@mandriva.org> 0.10-3mdv2009.1
+ Revision: 320971
- rebuild for new python

* Sat Nov 29 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.10-2mdv2009.1
+ Revision: 308014
- require python-pkg-resources for mdv version greater than 200900, instead of python-setuptools which requires bunch of useless python stuff and python-devel

* Mon Sep 01 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.10-1mdv2009.0
+ Revision: 278188
- drop patch 0, fixed upstream
- fix file list
- update to new version 0.10

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.9-10mdv2009.0
+ Revision: 247416
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sat Mar 08 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9-8mdv2008.1
+ Revision: 182205
- new license policy

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.9-7mdv2008.1
+ Revision: 170905
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Sep 24 2007 Anne Nicolas <ennael@mandriva.org> 0.9-6mdv2008.0
+ Revision: 92569
- Fix menu

* Thu Sep 13 2007 Emmanuel Andry <eandry@mandriva.org> 0.9-5mdv2008.0
+ Revision: 85339
- fix desktop file validation
- remove omf files location workaround

* Wed Aug 08 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9-4mdv2008.0
+ Revision: 60179
- fix omf files directory
- tune up the desktop file
- add python-pyxml to requires
- add gstreamer-plugins-bad to enable LADSPA effect support
- add gstreamer-plugins-ugly to enable mp3 files playback

* Wed Jul 25 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9-3mdv2008.0
+ Revision: 55269
- provide patch, which should fix #31976

* Mon Jul 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9-2mdv2008.0
+ Revision: 54506
- add provides on yelp (should close 31976)
- set buildrequires on gettext and scrollkeeper
- add requires on ladspa
- fix desktop file
- add post and postun scriplets
- own missing directories and files
- extend the description

* Wed May 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9-1mdv2008.0
+ Revision: 30341
- update to the stable version


* Wed Feb 28 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9-0.20070228.1mdv2007.0
+ Revision: 127068
- update to version 0.9 svn
- spec file clean

* Sun Feb 18 2007 Götz Waschk <waschk@mandriva.org> 0.2-2mdv2007.1
+ Revision: 122366
- replace deps by package names that exist on Mandriva and not Debian
- make it a noarch package
- change the executable name to match the menu entry
- this is still unusable, stay tuned

* Sat Feb 17 2007 Jérôme Soyer <saispo@mandriva.org> 0.2-1mdv2007.1
+ Revision: 122087
- Fix build
- Import jokosher

