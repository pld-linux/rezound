Summary:	ReZound - graphical audio file editor
Summary(pl):	ReZound - graficzny edytor plik�w d�wi�kowych
Name:		rezound
Version:	0.8.3
Release:	0.beta.1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/rezound/%{name}-%{version}beta.tar.gz
# Source0-md5:	b127f0643e5e3035831bd316104921eb
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-opt.patch
Patch1:		%{name}-flex.patch
URL:		http://rezound.sourceforge.net/
BuildRequires:	audiofile-devel >= 0.2.3
BuildRequires:	autoconf
BuildRequires:	bison >= 1.875-3
BuildRequires:	fftw-devel >= 2.1.3
BuildRequires:	flac-devel >= 1.1.0
BuildRequires:	flex
BuildRequires:	fox-devel >= 1.1.25
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libvorbis-devel
Requires:	fox >= 1.1.25
Requires:	lame
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# not used, but must be here because of GL-enabled fox
%define 	_noautoreqdep	libGL.so.1 libGLU.so.1 libFOX-1.1.so.*

%description
ReZound aims to be a stable, open source, and graphical audio file
editor primarily for but not limited to the Linux operating system.

%description -l pl
ReZound ma sta� si� stabilnym, otwartym, graficznym edytorem plik�w
d�wi�kowych g��wnie, cho� nie tylko, dla systemu Linux.

%prep
%setup -q -n %{name}-%{version}beta
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I config/m4
%{__autoconf}
%{__automake}
%configure \
	OPTFLAGS="%{rpmcflags}" \
	--enable-jack
	
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
