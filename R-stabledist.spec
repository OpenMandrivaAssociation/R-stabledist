%global packname stabledist
%global rlibdir %{_libdir}/R/library

Name: R-%{packname}
Version: 0.6_6
Release: 1
Summary: Stable Distribution Functions
Group: Sciences/Mathematics
License: GPLv2+
URL: http://cran.r-project.org/web/packages/%{packname}/index.html
Source0: http://cran.r-project.org/src/contrib/%{packname}_0.6-6.tar.gz
BuildArch: noarch
Requires: R-stats R-utils R-fBasics R-RUnit R-sfsmisc 
BuildRequires: R-devel Rmath-devel R-stats R-utils R-fBasics R-RUnit R-sfsmisc texlive-collection-latex

%description
Density, Probability and Quantile functions, and random
number generation for (skew) stable distributions, using the
parameterizations of Nolan.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/xtraR
