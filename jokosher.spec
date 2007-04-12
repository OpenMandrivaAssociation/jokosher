%define snapshot 20070228

Summary:	Jokosher is a simple yet powerful multi-track studio
Name:		jokosher
Version:	0.9
Release:	%mkrel 0.%{snapshot}.1
Group:		Sound
License:	GPL
URL:		http://jokosher.org
Source0:	http://www.jokosher.org/downloads/source/%{name}-%{version}-%{snapshot}.tar.bz2
BuildRequires:	python-devel
BuildRequires:	desktop-file-utils
Requires:	dbus-python
Requires:	gnonlin >= 0.10.6
Requires:	gstreamer0.10-plugins-base >= 0.10.11
Requires:	gstreamer0.10-plugins-good >= 0.10.4
Requires:	gstreamer0.10-python
Requires:	gnome-python
Requires:	pygtk2.0-libglade
Requires:	python-setuptools
BuildArch:	noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Jokosher is a simple yet powerful multi-track studio. 
With it you can create and record music, podcasts and more, 
all from an integrated simple environment.

%prep
%setup -qn %{name}-%{version}-%{snapshot}

for i in `find . -type d -name .svn` ; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

chmod 644 doc/userguide/images/*
chmod 644 doc/api/update.sh
sed -i 's/\r//' doc/userguide/jokosheruserguide.de.html
sed -i '1d' Jokosher/JokosherApp.py

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

#rm -f %{buildroot}/%{_datadir}/applications/%{name}.desktop

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --remove-category="AudioVideo" \
  --add-category="X-MandrivaLinux-Multimedia-Sound" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*


%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING README help/* doc/*
%attr(755,root,root) %{_bindir}/%{name}
%{py_sitedir}/Jokosher/*.py*
%{py_sitedir}/%{name}*egg-info
%{_datadir}/applications/jokosher.desktop
%{_datadir}/gnome/help/jokosher/C/figures/*.png
%{_datadir}/gnome/help/jokosher/C/*.xml
%{_iconsdir}/hicolor/48x48/apps/jokosher-icon.png
%{_datadir}/jokosher/Instruments/*.instr
%{_datadir}/jokosher/Instruments/images/*.png
%{_datadir}/jokosher/Jokosher.glade
%{_datadir}/jokosher/extensions/*py*
%{_datadir}/jokosher/jokosher-logo.png
%{_datadir}/jokosher/pixmaps/*.png
%{_datadir}/mime/packages/jokosher.xml
%exclude /usr/share/pixmaps/jokosher-icon.png


