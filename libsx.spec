Name:           libsx
Version:        2.08
Release:        0%{?dist}
Summary:        The Simple X library

Group:          Applications/Engineering
# gxeps is under the MIT, other programs are GPLv2
License:        GPLv2 and MIT
URL:            http://cola.gmu.edu/grads/gadoc/supplibs.html

Source0:        https://sourceforge.net/projects/opengrads/files/supplibs/2.4.0/libsx-2.08.tar.gz
# Correct source0:        https://sourceforge.net/projects/opengrads/files/supplibs/2.4.0/supplibs-2.4.0.tar.gz

BuildRequires:  gcc gcc-c++ automake autoconf libtool make
BuildRequires:  libXaw3dXft-devel libXpm-devel

Requires:  libXaw3dXft libXpm


%description
Libsx (the Simple X library) is a library of code that sits on top of and
 to the side of the Athena widget set.  Its purpose is to make writing X
 applications *much* easier.


%prep
%setup -q
autoreconf -f -i

%build
#./bootstrap
%configure

make


%install

libtool --finish /usr/lib64

rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%{__install} -d -m755 $RPM_BUILD_ROOT%{_datadir}/%{name}

%files
%{_includedir}/libsx.h
%exclude %{_libdir}/libsx.la
%{_libdir}/libsx.a
%{_libdir}/libsx.so
%{_libdir}/libsx.so.0
%{_libdir}/libsx.so.0.0.0
%{_libdir}/pkgconfig/libsx.pc
%{_datadir}/libsx/dialogs.de
%{_datadir}/libsx/dialogs.en
%{_datadir}/libsx/dialogs.fr

%changelog
* Fri Oct 6 2023 Paolo Oliveri <paul@oliveri.info> 2.08-0
- Built for RHEL 9
