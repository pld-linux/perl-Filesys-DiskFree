#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Filesys
%define	pnam	DiskFree
Summary:	Filesys::DiskFree - perform the UNIX command 'df' in a portable fashion
Summary(pl):	Filesys::DiskFree - przeno�na posta� uniksowego polecenia 'df'
Name:		perl-Filesys-DiskFree
Version:	0.06
Release:	11
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e39b3b10468fd98973ce76a97351f3c4
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
Obsoletes:	perl-DiskFree
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Filesys::DiskFree Perl module does about what the UNIX command df(1)
does, listing the mounted disks, and the amount of free space used and
available.

%description -l pl
Modu� Perla Filesys::DiskFree robi to samo, co uniksowe polecenie
df(1), wypisuje list� zamontowanych dysk�w oraz ilo�� u�ytego i
dost�pnego miejsca na nich.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -af eg $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README eg
%{perl_vendorlib}/Filesys/DiskFree.pm
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
