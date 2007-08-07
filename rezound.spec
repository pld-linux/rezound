#
# Conditional build:
%bcond_without	alsa	# without ALSA support
%bcond_without	jack	# without JACK support
#
Summary:	ReZound - graphical audio file editor
Summary(pl.UTF-8):	ReZound - graficzny edytor plików dźwiękowych
Name:		rezound
Version:	0.12.3
Release:	0.beta.1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/rezound/%{name}-%{version}beta.tar.gz
# Source0-md5:	df109c9d9ad6d27214a7417df583115d
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-opt.patch
Patch1:		%{name}-flac.patch
Patch2:		%{name}-nosource.patch
URL:		http://rezound.sourceforge.net/
%{?with_alsa:BuildRequires:	alsa-lib-devel >= 1.0.0}
BuildRequires:	audiofile-devel >= 1:0.2.3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison >= 1.875-3
BuildRequires:	fftw-devel >= 2.1.5-4
BuildRequires:	flac-c++-devel >= 1.1.3
BuildRequires:	flex
BuildRequires:	fox-devel >= 1.2
%{?with_jack:BuildRequires:	jack-audio-connection-kit-devel}
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	soundtouch-devel >= 1.3.0
Requires:	fox >= 1.2
Requires:	lame
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# not used, but must be here because of GL-enabled fox
%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
ReZound aims to be a stable, open source, and graphical audio file
editor primarily for but not limited to the Linux operating system.

%description -l pl.UTF-8
ReZound ma stać się stabilnym, otwartym, graficznym edytorem plików
dźwiękowych głównie, choć nie tylko, dla systemu Linux.

%prep
%setup -q -n %{name}-%{version}beta
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal} -I config/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	OPTFLAGS="%{rpmcflags}" \
	--%{?with_alsa:en}%{!?with_alsa:dis}able-alsa \
	--%{?with_jack:en}%{!?with_jack:dis}able-jack \
	--disable-portaudio

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README docs/{AUTHORS,Features.txt,FrontendFoxFeatures.txt,NEWS,TODO*}
%attr(755,root,root) %{_bindir}/*
%{_datadir}/rezound
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
