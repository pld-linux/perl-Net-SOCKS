%include	/usr/lib/rpm/macros.perl
Summary:	Net-SOCKS perl module
Summary(pl):	Modu³ perla Net-SOCKS
Name:		perl-Net-SOCKS
Version:	0.03
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/SOCKS-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net-SOCKS - a SOCKS client.

%description -l pl
Net-SOCKS - klient SOCKS.

%prep
%setup -q -n SOCKS-%{version}
%patch -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz example
%{perl_sitelib}/Net/SOCKS.pm
%{perl_sitelib}/auto/Net/SOCKS
%{_mandir}/man3/*
