%define realname   Net-Rendezvous-Publish-Backend-Howl

Name:		perl-%{realname}
Version:    0.03
Release:    %mkrel 8
License:	GPL or Artistic
Group:		Development/Perl
Summary:    Backend module using howl for Net::Rendezvous
Source0:    http://search.cpan.org//CPAN/authors/id/R/RC/RCLAMP/%{realname}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel 
BuildRequires:  perl-Net-Rendezvous 
BuildRequires:	howl-devel
BuildRequires:  perl-Module-Build
BuildRequires:  perl-ExtUtils-ParseXS
BuildRequires:  perl-ExtUtils-CBuilder
BuildRequires:  perl-Module-Pluggable
BuildRequires:  perl-Class-Accessor-Lvalue
Provides:       perl-Net-Rendezvous-Publish-Backend

%description
This module interfaces to the Porchdog's Howl library in order to allow 
service publishing.
It is used by Net::Rendezvous::Publish, in order to adapt to
different mDns implementation.

%prep
%setup -q -n %{realname}-%{version}

%build
%{__perl} Build.PL INSTALLDIRS=vendor

%check
# requires mdns running
#./Build test

%install
rm -rf $RPM_BUILD_ROOT
./Build install destdir=%buildroot installdirs=vendor

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*


