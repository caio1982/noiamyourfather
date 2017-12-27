%define name fortune-noiamyourfather
%define version 42
%define release %mkrel 1

Summary: Random translations for the most famous quote from Darth Vader
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}.tar.bz2
License: GPL
Group: Toys
URL: http://noiamyourfather.org/fortune/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Requires: fortune-mod
BuildRequires: fortune-mod
BuildRequires: recode

%description
This package include some fortunes with Anakin Skywalker spilling the beans.

%prep
%setup -q -c %name
rm -f noiamyourfather/*.dat
for fortune in noiamyourfather/*;do recode l1..u8 $fortune; done

%build
%make clean
%make 

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
cd %buildroot%_datadir/games/fortunes/noiamyourfather
for x in *.dat; do 
  ln -s $(echo $x|sed s/.dat//) $(echo $x|sed s/.dat/.u8/) 
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
 %_datadir/games/fortunes/noiamyourfather*

%changelog
* Fri Oct 17 2008 Caio Begotti <caio@mandriva.com> 20081017-1mdv2009.0
	- Initial release :-)
