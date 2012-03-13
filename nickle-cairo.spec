Summary:	Cairo-5c - Nickle bindings for the Cairo graphics library
Summary(pl.UTF-8):	Cairo-5c - wiązania języka Nickle do biblioteki graficznej Cairo
Name:		nickle-cairo
Version:	1.5
Release:	1
License:	LGPL v2.1 or MPL v1.1
Group:		Libraries
Source0:	http://cairographics.org/releases/cairo-5c-%{version}.tar.gz
# Source0-md5:	aa0639e84d06afb82fabb9064980dc06
URL:		http://cairographics.org/cairo-nickle/
BuildRequires:	cairo-devel
BuildRequires:	fontconfig-devel
BuildRequires:	librsvg-devel >= 2.0
BuildRequires:	nickle
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
Requires:	nickle
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# refers to symbols provided by nickle
%define		skip_post_check_so	libcairo-5c\.so.*

%description
Cairo-5c - Nickle language binding for the cairo graphics library.

%description -l pl.UTF-8
Cairo-5c - wiązania języka Nickle do biblioteki graficznej Cairo.

%prep
%setup -q -n cairo-5c-%{version}

%build
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}
mv -f $RPM_BUILD_ROOT%{_datadir}/cairo-5c/examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# not used for linking
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcairo-5c.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libcairo-5c.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcairo-5c.so.0
%attr(755,root,root) %{_libdir}/libcairo-5c.so
%{_datadir}/nickle/cairo.5c
%{_datadir}/nickle/nichrome*.5c
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/cairo-5c.3*
