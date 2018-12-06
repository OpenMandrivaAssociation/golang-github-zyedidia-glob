# Run tests in check section
%bcond_without check

%global goipath         github.com/zyedidia/glob
%global commit          dd4023a66dc351ae26e592d21cd133b5b143f3d8

%global common_description %{expand:
A Go package for glob matching.}

%gometa

Name:    %{goname}
Version: 0
Release: 0.4%{?dist}
Summary: A Go package for glob matching
License: MIT
URL:     %{gourl}
Source:  %{gosource}

%description
%{common_description}


%package    devel
Summary:    %{summary}
BuildArch:  noarch
 
%description devel
%{common_description}
 
This package contains the source code needed for building packages that import
the %{goipath} Go namespace.


%prep
%gosetup -q


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.gitdd4023a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20180314gitdd4023a
- Update with the new Go packaging

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20170209gitdd4023a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20170209gitdd4023a
- First package for Fedora

