%include	/usr/lib/rpm/macros.perl
Summary:	MIME-tools perl module
Summary(pl):	Modu³ perla MIME-tools
Name:		perl-MIME-tools
Version:	4.124
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/MIME/MIME-tools-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-MailTools
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-IO-stringy
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MIME-tools - modules for parsing (and creating!) MIME entities.

%description -l pl
MIME-tools - zestaw modu³ów do operacji na danych w formacie MIME.

%prep
%setup -q -n MIME-tools-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}

make install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/MIME-tools
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*.gz

%{perl_sitelib}/MIME/*.pm
%{perl_sitelib}/MIME/Decoder
%{perl_sitelib}/MIME/Field
%{perl_sitearch}/auto/MIME-tools

%{_mandir}/man3/*

%{_prefix}/src/examples/%{name}
