#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-xts
Version  : 0.9.7
Release  : 1
URL      : https://cran.r-project.org/src/contrib/xts_0.9-7.tar.gz
Source0  : https://cran.r-project.org/src/contrib/xts_0.9-7.tar.gz
Summary  : eXtensible Time Series
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-xts-lib
Requires: R-zoo
BuildRequires : R-zoo
BuildRequires : clr-R-helpers

%description
This directory contains a skeleton example
of how to link to the C-API
The basic requirements to use the exported xts
C code is:

%package lib
Summary: lib components for the R-xts package.
Group: Libraries

%description lib
lib components for the R-xts package.


%prep
%setup -q -c -n xts

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1496162638

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1496162638
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library xts
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library xts


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/xts/DESCRIPTION
/usr/lib64/R/library/xts/INDEX
/usr/lib64/R/library/xts/Meta/Rd.rds
/usr/lib64/R/library/xts/Meta/data.rds
/usr/lib64/R/library/xts/Meta/features.rds
/usr/lib64/R/library/xts/Meta/hsearch.rds
/usr/lib64/R/library/xts/Meta/links.rds
/usr/lib64/R/library/xts/Meta/nsInfo.rds
/usr/lib64/R/library/xts/Meta/package.rds
/usr/lib64/R/library/xts/Meta/vignette.rds
/usr/lib64/R/library/xts/NAMESPACE
/usr/lib64/R/library/xts/NEWS
/usr/lib64/R/library/xts/R/xts
/usr/lib64/R/library/xts/R/xts.rdb
/usr/lib64/R/library/xts/R/xts.rdx
/usr/lib64/R/library/xts/api_example/DESCRIPTION
/usr/lib64/R/library/xts/api_example/NAMESPACE
/usr/lib64/R/library/xts/api_example/R/checkOrder.R
/usr/lib64/R/library/xts/api_example/README
/usr/lib64/R/library/xts/api_example/man/checkOrder.Rd
/usr/lib64/R/library/xts/api_example/man/linkXTS-package.Rd
/usr/lib64/R/library/xts/api_example/src/checkOrder.c
/usr/lib64/R/library/xts/data/sample_matrix.rda
/usr/lib64/R/library/xts/doc/index.html
/usr/lib64/R/library/xts/doc/xts-faq.R
/usr/lib64/R/library/xts/doc/xts-faq.Rnw
/usr/lib64/R/library/xts/doc/xts-faq.pdf
/usr/lib64/R/library/xts/doc/xts.R
/usr/lib64/R/library/xts/doc/xts.Rnw
/usr/lib64/R/library/xts/doc/xts.pdf
/usr/lib64/R/library/xts/help/AnIndex
/usr/lib64/R/library/xts/help/aliases.rds
/usr/lib64/R/library/xts/help/paths.rds
/usr/lib64/R/library/xts/help/xts.rdb
/usr/lib64/R/library/xts/help/xts.rdx
/usr/lib64/R/library/xts/html/00Index.html
/usr/lib64/R/library/xts/html/R.css
/usr/lib64/R/library/xts/include/xts.h
/usr/lib64/R/library/xts/include/xtsAPI.h
/usr/lib64/R/library/xts/include/xts_stubs.c
/usr/lib64/R/library/xts/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/xts/libs/xts.so
