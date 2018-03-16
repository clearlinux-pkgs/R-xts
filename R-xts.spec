#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-xts
Version  : 0.10.2
Release  : 14
URL      : https://cran.r-project.org/src/contrib/xts_0.10-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/xts_0.10-2.tar.gz
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
export SOURCE_DATE_EPOCH=1521225473

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521225473
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library xts
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library xts
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library xts
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library xts|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


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
/usr/lib64/R/library/xts/unitTests/Makefile
/usr/lib64/R/library/xts/unitTests/runit.Ops.R
/usr/lib64/R/library/xts/unitTests/runit.coredata.R
/usr/lib64/R/library/xts/unitTests/runit.data.frame.R
/usr/lib64/R/library/xts/unitTests/runit.diff.R
/usr/lib64/R/library/xts/unitTests/runit.endpoints.R
/usr/lib64/R/library/xts/unitTests/runit.fts.R
/usr/lib64/R/library/xts/unitTests/runit.indexClass.R
/usr/lib64/R/library/xts/unitTests/runit.irts.R
/usr/lib64/R/library/xts/unitTests/runit.isordered.R
/usr/lib64/R/library/xts/unitTests/runit.lag.R
/usr/lib64/R/library/xts/unitTests/runit.matrix.R
/usr/lib64/R/library/xts/unitTests/runit.merge.R
/usr/lib64/R/library/xts/unitTests/runit.na.locf.R
/usr/lib64/R/library/xts/unitTests/runit.na.omit.R
/usr/lib64/R/library/xts/unitTests/runit.period.apply.R
/usr/lib64/R/library/xts/unitTests/runit.plot.R
/usr/lib64/R/library/xts/unitTests/runit.split.R
/usr/lib64/R/library/xts/unitTests/runit.subset.R
/usr/lib64/R/library/xts/unitTests/runit.timeBasedSeq.R
/usr/lib64/R/library/xts/unitTests/runit.timeSeries.R
/usr/lib64/R/library/xts/unitTests/runit.to.period.R
/usr/lib64/R/library/xts/unitTests/runit.ts.R
/usr/lib64/R/library/xts/unitTests/runit.xts.R
/usr/lib64/R/library/xts/unitTests/runit.xts.methods.R
/usr/lib64/R/library/xts/unitTests/runit.zoo.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/xts/libs/xts.so
/usr/lib64/R/library/xts/libs/xts.so.avx2
/usr/lib64/R/library/xts/libs/xts.so.avx512
