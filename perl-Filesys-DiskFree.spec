%include	/usr/lib/rpm/macros.perl
Summary:	DiskFree perl module
Summary(pl):	Modu³ perla DiskFree
Name:		perl-Filesys-DiskFree
Version:	0.06
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Filesys/Filesys-DiskFree-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
Obsoletes:	perl-DiskFree
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Filesys-DiskFree - perform the Unix command 'df' in a portable
fashion.

%description -l pl
Filesys-DiskFree - 'df' dla perla.

%prep
%setup -q -n Filesys-DiskFree-%{version}
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
