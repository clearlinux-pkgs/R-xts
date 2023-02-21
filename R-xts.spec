#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-xts
Version  : 0.13.0
Release  : 63
URL      : https://cran.r-project.org/src/contrib/xts_0.13.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/xts_0.13.0.tar.gz
Summary  : eXtensible Time Series
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-xts-lib = %{version}-%{release}
Requires: R-zoo
BuildRequires : R-zoo
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n xts
cd %{_builddir}/xts

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1677001122

%install
export SOURCE_DATE_EPOCH=1677001122
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


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
/usr/lib64/R/library/xts/benchmarks/benchmark.subset.R
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
/usr/lib64/R/library/xts/tests/tinytest.R
/usr/lib64/R/library/xts/tinytest/runit.rowSums-rowMeans.R
/usr/lib64/R/library/xts/tinytest/test-Ops.R
/usr/lib64/R/library/xts/tinytest/test-align.time.R
/usr/lib64/R/library/xts/tinytest/test-all.equal.R
/usr/lib64/R/library/xts/tinytest/test-binsearch.R
/usr/lib64/R/library/xts/tinytest/test-coredata.R
/usr/lib64/R/library/xts/tinytest/test-data.frame.R
/usr/lib64/R/library/xts/tinytest/test-diff.R
/usr/lib64/R/library/xts/tinytest/test-dimnames.R
/usr/lib64/R/library/xts/tinytest/test-endpoints.R
/usr/lib64/R/library/xts/tinytest/test-first-last.R
/usr/lib64/R/library/xts/tinytest/test-index.R
/usr/lib64/R/library/xts/tinytest/test-irts.R
/usr/lib64/R/library/xts/tinytest/test-isordered.R
/usr/lib64/R/library/xts/tinytest/test-lag.R
/usr/lib64/R/library/xts/tinytest/test-matrix.R
/usr/lib64/R/library/xts/tinytest/test-merge.R
/usr/lib64/R/library/xts/tinytest/test-na.fill.R
/usr/lib64/R/library/xts/tinytest/test-na.locf.R
/usr/lib64/R/library/xts/tinytest/test-na.omit.R
/usr/lib64/R/library/xts/tinytest/test-parseISO8601.R
/usr/lib64/R/library/xts/tinytest/test-period.apply.R
/usr/lib64/R/library/xts/tinytest/test-periodicity.R
/usr/lib64/R/library/xts/tinytest/test-plot.R
/usr/lib64/R/library/xts/tinytest/test-print.R
/usr/lib64/R/library/xts/tinytest/test-reclass.R
/usr/lib64/R/library/xts/tinytest/test-split.R
/usr/lib64/R/library/xts/tinytest/test-subset-time-of-day.R
/usr/lib64/R/library/xts/tinytest/test-subset.R
/usr/lib64/R/library/xts/tinytest/test-tclass.R
/usr/lib64/R/library/xts/tinytest/test-tformat.R
/usr/lib64/R/library/xts/tinytest/test-timeBasedSeq.R
/usr/lib64/R/library/xts/tinytest/test-timeSeries.R
/usr/lib64/R/library/xts/tinytest/test-to.period.R
/usr/lib64/R/library/xts/tinytest/test-ts.R
/usr/lib64/R/library/xts/tinytest/test-tzone.R
/usr/lib64/R/library/xts/tinytest/test-xts.R
/usr/lib64/R/library/xts/tinytest/test-xts.methods.R
/usr/lib64/R/library/xts/tinytest/test-zoo.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/xts/libs/xts.so
/usr/lib64/R/library/xts/libs/xts.so.avx2
/usr/lib64/R/library/xts/libs/xts.so.avx512
