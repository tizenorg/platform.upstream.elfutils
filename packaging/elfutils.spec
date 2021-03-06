%define keepstatic 1
Name:           elfutils
Version:        0.160
Release:        0
License:        GPL-3.0+
Summary:        Higher-level library to access ELF
Url:            http://elfutils.fedorahosted.org
Group:          Base/Utilities
Source:         elfutils-%{version}.tar.bz2
Source2:        baselibs.conf
Source1001: 	elfutils.manifest
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  bzip2-devel
BuildRequires:  flex
BuildRequires:  xz-devel
BuildRequires:  zlib-devel

%description
This package provides a higher-level library to access ELF files. This
is a part of elfutils package.

%package -n libasm
Summary:        A collection of utilities and DSOs to handle compiled objects
License:        LGPL-3.0+ or GPL-2.0

%description -n libasm
Elfutils is a collection of utilities, including ld (a linker), nm (for
listing symbols from object files), size (for listing the section sizes
of an object or archive file), strip (for discarding symbols), readline
(the see the raw ELF file structures), and elflint (to check for
well-formed ELF files).  Also included are numerous helper libraries
which implement DWARF, ELF, and machine-specific ELF handling.

%package -n libasm-devel
Summary:        A collection of utilities and DSOs to handle compiled objects
Requires:       glibc-devel
Requires:       libasm = %{version}
License:        LGPL-3.0+ or GPL-2.0

%description -n libasm-devel
Elfutils is a collection of utilities, including ld (a linker), nm (for
listing symbols from object files), size (for listing the section sizes
of an object or archive file), strip (for discarding symbols), readline
(the see the raw ELF file structures), and elflint (to check for
well-formed ELF files).  Also included are numerous helper libraries
which implement DWARF, ELF, and machine-specific ELF handling.

%package -n libebl
Summary:        A collection of utilities and DSOs to handle compiled objects
License:        LGPL-3.0+ or GPL-2.0

%description -n libebl
Elfutils is a collection of utilities, including ld (a linker), nm (for
listing symbols from object files), size (for listing the section sizes
of an object or archive file), strip (for discarding symbols), readline
(the see the raw ELF file structures), and elflint (to check for
well-formed ELF files).  Also included are numerous helper libraries
which implement DWARF, ELF, and machine-specific ELF handling.

%package -n libebl-devel
Summary:        Include Files and Libraries mandatory for Development
License:        LGPL-3.0+ or GPL-2.0
Requires:       glibc-devel
Requires:       libdw-devel = %{version}
Requires:       libebl = %{version}

%description -n libebl-devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%package -n libelf
Summary:        Library to read and write ELF files
License:        LGPL-3.0+ or GPL-2.0

%description -n libelf
This package provides a high-level library to read and write ELF files.
This is a part of elfutils package.

%package -n libelf-devel
Summary:        Include Files and Libraries mandatory for Development
License:        LGPL-3.0+ or GPL-2.0
Requires:       glibc-devel
Requires:       libelf = %{version}
Conflicts:      libelf0-devel

%description -n libelf-devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%package -n libdw
Summary:        Library to access DWARF debugging information
License:        LGPL-3.0+ or GPL-2.0

%description -n libdw
This package provides a high-level library to access the DWARF debugging
information.  This is a part of elfutils package.

%package -n libdw-devel
Summary:        Include Files and Libraries mandatory for Development
License:        LGPL-3.0+ or GPL-2.0
Requires:       glibc-devel
Requires:       libdw = %{version}
Requires:       libelf-devel = %{version}

%description -n libdw-devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%prep
%setup -q -n elfutils-%{version}
cp %{SOURCE1001} .

%build
#modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{_sourcedir}/%{name}.changes")"
#DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
#TIME="\"$(date -d "${modified}" "+%%R")\""
#find . -type f -regex ".*\.c\|.*\.cpp\|.*\.h" -exec sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g" {} +
autoreconf -fi
%configure --program-prefix=eu- --disable-werror
make %{?_smp_mflags}

%install
%make_install
# remove unneeded files
ls -lR %{buildroot}%{_libdir}/libelf*

%post -n libebl -p /sbin/ldconfig

%post -n libelf -p /sbin/ldconfig

%post -n libdw -p /sbin/ldconfig

%postun -n libebl -p /sbin/ldconfig

%postun -n libelf -p /sbin/ldconfig

%postun -n libdw -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%{_bindir}/*

%files -n libasm
%manifest %{name}.manifest
%defattr(-,root,root)
%license COPYING
%{_libdir}/libasm.so.*
%{_libdir}/libasm-%{version}.so

%files -n libasm-devel
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/libasm.so
%{_libdir}/libasm.a
%dir %{_includedir}/elfutils
%{_includedir}/elfutils/libasm.h

%files -n libebl
%manifest %{name}.manifest
%defattr(-,root,root)
%license COPYING
%{_libdir}/elfutils

%files -n libebl-devel
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/libebl.a
%dir %{_includedir}/elfutils
%{_includedir}/elfutils/libebl.h

%files -n libelf
%manifest %{name}.manifest
%defattr(-,root,root)
%license COPYING
%{_libdir}/libelf.so.*
%{_libdir}/libelf-%{version}.so

%files -n libelf-devel
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/libelf.so
%{_libdir}/libelf.a
#%{_libdir}/libelf_pic.a
%{_includedir}/libelf.h
%{_includedir}/gelf.h
%{_includedir}/nlist.h
%dir %{_includedir}/elfutils
%{_includedir}/elfutils/elf-knowledge.h
%{_includedir}/elfutils/version.h

%files -n libdw
%manifest %{name}.manifest
%defattr(-,root,root)
%license COPYING
%{_libdir}/libdw.so.*
%{_libdir}/libdw-%{version}.so

%files -n libdw-devel
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/libdw.a
%{_libdir}/libdw.so
%{_includedir}/dwarf.h
%dir %{_includedir}/elfutils
%{_includedir}/elfutils/libdw.h
%{_includedir}/elfutils/libdwfl.h
%{_includedir}/elfutils/libdwelf.h

%changelog
