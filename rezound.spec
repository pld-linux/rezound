Summary:	ReZound - graphical audio file editor
Summary(pl):	ReZound - graficzny edytor plik�w d�wi�kowych
Name:		rezound
Version:	0.5.1
Release:	0.beta.2
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/rezound/%{name}-%{version}beta.tar.gz
Patch0:		%{name}-bison.patch
Patch1:		%{name}-fox-update.patch
Patch2:		%{name}-opt.patch
URL:		http://rezound.sourceforge.net/
BuildRequires:	audiofile-devel >= 0.2.3
BuildRequires:	autoconf
BuildRequires:	bison >= 1.875-3
BuildRequires:	fftw-devel >= 2.1.3
BuildRequires:	flex
BuildRequires:	fox-devel >= 1.1.25
BuildRequires:	libstdc++-devel
BuildRequires:	libvorbis-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# not used, but must be here because of GL-enabled fox
%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

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
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal} -I config/m4
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README docs/{AUTHORS,Features.txt,FrontendFoxFeatures.txt,NEWS,TODO*}
%attr(755,root,root) %{_bindir}/*
%{_datadir}/rezound
