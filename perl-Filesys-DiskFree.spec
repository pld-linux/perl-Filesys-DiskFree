%include	/usr/lib/rpm/macros.perl
%define	pdir	Filesys
%define	pnam	DiskFree
Summary:	DiskFree perl module
Summary(pl):	Modu³ perla DiskFree
Name:		perl-Filesys-DiskFree
Version:	0.06
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
Obsoletes:	perl-DiskFree
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Filesys-DiskFree - perform the Unix command 'df' in a portable
fashion.

%description -l pl
Filesys-DiskFree - 'df' dla perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz eg
%{perl_sitelib}/Filesys/DiskFree.pm
%{_mandir}/man3/*
