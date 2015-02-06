%define mainver %(echo %{version} | sed -e "s/\\([0-9]*\\.[0-9]*\\).[0-9]*/\\1/")

Summary:	Simple yet powerful multi-track studio
Name:		jokosher
Version:	0.11.5
Release:	4
Group:		Sound
License:	GPLv2+
URL:		http://jokosher.org
Source0:	https://launchpad.net/jokosher/trunk/0.11.5/+download/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(python2)
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
Requires:	pygtk2.0-libglade
Requires:	python-pkg-resources
Requires:	yelp
Requires:	ladspa
Requires(post):	scrollkeeper
Requires(postun): scrollkeeper
Obsoletes:	%{name} < 0.9
BuildArch:	noarch

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
python2 setup.py build

%install
python2 setup.py install --skip-build --root=%{buildroot}

perl -pi -e 's,%{name}-icon.png,%{name}-icon,g' %{buildroot}%{_datadir}/applications/*

desktop-file-install \
    --remove-category="Application" \
    --remove-category="AudioVideo" \
    --add-category="Audio;Recorder;X-MandrivaLinux-CrossDesktop;" \
    --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

chmod 755 %{buildroot}%{py2_puresitedir}/Jokosher/Profiler.py

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING README help/*
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/Instruments
%dir %{_datadir}/%{name}/Instruments/images
%dir %{_datadir}/%{name}/extensions
%dir %{_datadir}/%{name}/pixmaps
%dir %{_datadir}/omf/%{name}
%dir %{py2_puresitedir}/Jokosher
%dir %{py2_puresitedir}/Jokosher/elements
%dir %{py2_puresitedir}/Jokosher/ui
%dir %{py2_puresitedir}/Jokosher/PlatformUtils
%{py2_puresitedir}/Jokosher/*.py*
%{py2_puresitedir}/Jokosher/elements/*.py*
%{py2_puresitedir}/Jokosher/PlatformUtils/*.py*
%{py2_puresitedir}/Jokosher/ui/*.py*
%{py2_puresitedir}/%{name}*egg-info
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

