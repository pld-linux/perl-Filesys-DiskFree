%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	DiskFree perl module
Summary(pl):	Modu³ perla DiskFree
Name:		perl-Filesys-DiskFree
Version:	0.06
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Filesys/Filesys-DiskFree-%{version}.tar.gz
Patch:		perl-Filesys-DiskFree-paths.patch
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
Obsoletes:	perl-DiskFree
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Filesys-DiskFree - perform the Unix command 'df' in a portable fashion.

%description -l pl
Filesys-DiskFree - 'df' dla perla.

%prep
%setup -q -n Filesys-DiskFree-%{version}
%patch -p1

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Filesys/DiskFree
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz eg

%{perl_sitelib}/Filesys/DiskFree.pm
%{perl_sitearch}/auto/Filesys/DiskFree

%{_mandir}/man3/*
