%include	/usr/lib/rpm/macros.perl
%define	pdir	Filesys
%define	pnam	DiskFree
Summary:	Filesys::DiskFree Perl module
Summary(cs):	Modul Filesys::DiskFree pro Perl
Summary(da):	Perlmodul Filesys::DiskFree
Summary(de):	Filesys::DiskFree Perl Modul
Summary(es):	Módulo de Perl Filesys::DiskFree
Summary(fr):	Module Perl Filesys::DiskFree
Summary(it):	Modulo di Perl Filesys::DiskFree
Summary(ja):	Filesys::DiskFree Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Filesys::DiskFree ÆÞ ¸ðÁÙ
Summary(nb):	Perlmodul Filesys::DiskFree
Summary(pl):	Modu³ perla Filesys::DiskFree
Summary(pt_BR):	Módulo Perl Filesys::DiskFree
Summary(pt):	Módulo de Perl Filesys::DiskFree
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Filesys::DiskFree
Summary(sv):	Filesys::DiskFree Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Filesys::DiskFree
Summary(zh_CN):	Filesys::DiskFree Perl Ä£¿é
Name:		perl-Filesys-DiskFree
Version:	0.06
Release:	11
License:	GPL
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
Filesys::DiskFree - perform the Unix command 'df' in a portable
fashion.

%description -l pl
Filesys::DiskFree - 'df' dla perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
