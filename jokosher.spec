Summary:	Simple yet powerful multi-track studio
Name:		jokosher
Version:	0.11
Release:	%mkrel 2
Group:		Sound
License:	GPLv2+
URL:		http://jokosher.org
Source0:	http://www.jokosher.org/downloads/source/%{name}-%{version}.tar.bz2
BuildRequires:	python-devel >= %{py_ver}
BuildRequires:	desktop-file-utils
BuildRequires:	python-setuptools
BuildRequires:	gettext
BuildRequires:	scrollkeeper
Requires:	dbus-python
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
%{py_sitedir}/Jokosher/*.py*
%{py_sitedir}/Jokosher/elements/*.py*
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
