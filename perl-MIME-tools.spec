%include	/usr/lib/rpm/macros.perl
Summary:	MIME-tools perl module
Summary(pl):	Modu³ perla MIME-tools
Name:		perl-MIME-tools
Version:	5.410
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/MIME/MIME-tools-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.6
BuildRequires:	perl-MailTools
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-IO-stringy
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MIME-tools - modules for parsing (and creating!) MIME entities.

%description -l pl
MIME-tools - zestaw modu³ów do operacji na danych w formacie MIME.

%prep
%setup -q -n MIME-tools-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf README*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/MIME/*.pm
%{perl_sitelib}/MIME/Parser
%{perl_sitelib}/MIME/Decoder
%{perl_sitelib}/MIME/Field
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
