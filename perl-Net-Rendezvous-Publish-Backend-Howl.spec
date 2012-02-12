%define upstream_name Net-Rendezvous-Publish-Backend-Howl
%define upstream_version 0.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Backend module using howl for Net::Rendezvous
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org//CPAN/authors/id/R/RC/RCLAMP/%{upstream_name}-%{upstream_version}.tar.bz2
Source1:	%{name}.rpmlintrc

BuildRequires:	howl-devel
BuildRequires:	perl(Net::Rendezvous)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(ExtUtils::ParseXS)
BuildRequires:	perl(ExtUtils::CBuilder)
BuildRequires:	perl(Module::Pluggable)
BuildRequires:	perl(Class::Accessor::Lvalue)
BuildRequires:	perl-devel 

%description
This module interfaces to the Porchdog's Howl library in order to allow 
service publishing.
It is used by Net::Rendezvous::Publish, in order to adapt to
different mDns implementation.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL INSTALLDIRS=vendor

%check
# requires mdns running
#./Build test

%install
./Build install destdir=%{buildroot} installdirs=vendor

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*
