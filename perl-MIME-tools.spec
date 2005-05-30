#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	MIME
%define		pnam	tools
Summary:	MIME::tools - modules for parsing (and creating!) MIME entities
Summary(pl):	MIME::tools - zestaw modu³ów do operacji na danych w formacie MIME
Name:		perl-MIME-tools
Version:	5.417
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a92299db8729f0f7886ada6e3539b265
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl(File::Path) >= 1
BuildRequires:	perl(File::Spec) >= 0.6
BuildRequires:	perl-MailTools >= 1.05
BuildRequires:	perl-MIME-Base64 >= 2.20
BuildRequires:	perl-IO-stringy >= 1.211
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# optional
%define		_noautoreq	'perl(Convert::BinHex)'

%description
MIME-tools is a collection of Perl5 MIME:: modules for parsing,
decoding and generating single- or multipart (even nested
multipart) MIME messages. (Yes, kids, that means you can send messages
with attached GIF files).

%description -l pl
MIME::tools to zestaw modu³ów MIME:: dla Perla 5 do analizy,
dekodowania oraz tworzenia jedno- i wieloczê¶ciowych (a nawet
zagnie¿d¿onych wieloczê¶ciowych) wiadomo¶ci MIME (tak, to znaczy, ¿e
mo¿na wysy³aæ wiadomo¶ci z do³±czonymi plikami GIF).

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
