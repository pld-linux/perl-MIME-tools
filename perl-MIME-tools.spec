#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	MIME
%define		pnam	tools
Summary:	MIME::tools Perl module
Summary(cs):	Modul MIME::tools pro Perl
Summary(da):	Perlmodul MIME::tools
Summary(de):	MIME::tools Perl Modul
Summary(es):	Módulo de Perl MIME::tools
Summary(fr):	Module Perl MIME::tools
Summary(it):	Modulo di Perl MIME::tools
Summary(ja):	MIME::tools Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	MIME::tools ÆÞ ¸ðÁÙ
Summary(nb):	Perlmodul MIME::tools
Summary(pl):	Modu³ Perla MIME::tools
Summary(pt):	Módulo de Perl MIME::tools
Summary(pt_BR):	Módulo Perl MIME::tools
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl MIME::tools
Summary(sv):	MIME::tools Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl MIME::tools
Summary(zh_CN):	MIME::tools Perl Ä£¿é
Name:		perl-MIME-tools
Version:	5.411
Release:	10
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}a.tar.gz
# Source0-md5:	e7cb1f8e146171103640e3a5516afb1a
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl(File::Path) >= 1
BuildRequires:	perl(File::Spec) >= 0.6
BuildRequires:	perl-MailTools >= 1.05
BuildRequires:	perl-MIME-Base64 >= 2.04
BuildRequires:	perl(MIME::QuotedPrint) >= 2.03
BuildRequires:	perl-IO-stringy >= 1.211
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MIME::tools - modules for parsing (and creating!) MIME entities.

%description -l pl
MIME::tools - zestaw modu³ów do operacji na danych w formacie MIME.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%{perl_vendorlib}/MIME/*.pm
%{perl_vendorlib}/MIME/Parser
%{perl_vendorlib}/MIME/Decoder
%{perl_vendorlib}/MIME/Field
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
