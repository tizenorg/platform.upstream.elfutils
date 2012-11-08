Name:           elfutils
Version:        0.153
Release:        0
License:        GPL-2.0-with-osi-exception
Summary:        Higher-level library to access ELF
Url:            http://elfutils.fedorahosted.org
Group:          System/Libraries
Source:         elfutils-%{version}.tar.bz2
Source2:        baselibs.conf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  bzip2-devel
BuildRequires:  flex
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package provides a higher-level library to access ELF files. This
is a part of elfutils package.

%package -n libasm
Summary:        A collection of utilities and DSOs to handle compiled objects
Group:          Development/Tools/Other

%description -n libasm
Elfutils is a collection of utilities, including ld (a linker), nm (for
listing symbols from object files), size (for listing the section sizes
of an object or archive file), strip (for discarding symbols), readline
(the see the raw ELF file structures), and elflint (to check for
well-formed ELF files).  Also included are numerous helper libraries
which implement DWARF, ELF, and machine-specific ELF handling.

%package -n libasm-devel
License:        GPL-2.0-with-osi-exception
Summary:        A collection of utilities and DSOs to handle compiled objects
Group:          Development/Tools/Other
Requires:       glibc-devel,
Requires:       libasm = %{version}

%description -n libasm-devel
Elfutils is a collection of utilities, including ld (a linker), nm (for
listing symbols from object files), size (for listing the section sizes
of an object or archive file), strip (for discarding symbols), readline
(the see the raw ELF file structures), and elflint (to check for
well-formed ELF files).  Also included are numerous helper libraries
which implement DWARF, ELF, and machine-specific ELF handling.

%package -n libebl
License:        GPL-2.0-with-osi-exception
Summary:        A collection of utilities and DSOs to handle compiled objects
Group:          Development/Tools/Other
Provides:       libebl = %{version}
Obsoletes:      libebl < %{version}

%description -n libebl
Elfutils is a collection of utilities, including ld (a linker), nm (for
listing symbols from object files), size (for listing the section sizes
of an object or archive file), strip (for discarding symbols), readline
(the see the raw ELF file structures), and elflint (to check for
well-formed ELF files).  Also included are numerous helper libraries
which implement DWARF, ELF, and machine-specific ELF handling.

%package -n libebl-devel
License:        GPL-2.0-with-osi-exception
Summary:        Include Files and Libraries mandatory for Development
Group:          Development/Libraries/C and C++
Requires:       glibc-devel,
Requires:       libdw-devel = %{version}
Requires:       libebl = %{version}

%description -n libebl-devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%package -n libelf
License:        GPL-2.0-with-osi-exception
Summary:        Library to read and write ELF files

%description -n libelf
This package provides a high-level library to read and write ELF files.
This is a part of elfutils package.

%package -n libelf-devel
License:        GPL-2.0-with-osi-exception
Summary:        Include Files and Libraries mandatory for Development
Group:          Development/Libraries/C and C++
Requires:       glibc-devel,
Requires:       libelf = %{version}
Conflicts:      libelf0-devel

%description -n libelf-devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%package -n libdw
License:        GPL-2.0-with-osi-exception
Summary:        Library to access DWARF debugging information

%description -n libdw
This package provides a high-level library to access the DWARF debugging
information.  This is a part of elfutils package.

%package -n libdw-devel
License:        GPL-2.0-with-osi-exception
Summary:        Include Files and Libraries mandatory for Development
Group:          Development/Libraries/C and C++
Requires:       glibc-devel,
Requires:       libdw = %{version}
Requires:       libelf-devel = %{version}

%description -n libdw-devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%prep
%setup -q -n elfutils-%{version}

%build
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{_sourcedir}/%{name}.spec")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
find . -type f -regex ".*\.c\|.*\.cpp\|.*\.h" -exec sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g" {} +
autoreconf -fi
%configure --program-prefix=eu-
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
%defattr(-,root,root)
%{_bindir}/*

%files -n libasm
%defattr(-,root,root)
%{_libdir}/libasm.so.*
%{_libdir}/libasm-%{version}.so

%files -n libasm-devel
%defattr(-,root,root)
%{_libdir}/libasm.so
%{_libdir}/libasm.a
%dir %{_includedir}/elfutils
%{_includedir}/elfutils/libasm.h

%files -n libebl
%defattr(-,root,root)
%{_libdir}/elfutils

%files -n libebl-devel
%defattr(-,root,root)
%{_libdir}/libebl.a
%dir %{_includedir}/elfutils
%{_includedir}/elfutils/libebl.h

%files -n libelf
%defattr(-,root,root)
%{_libdir}/libelf.so.*
%{_libdir}/libelf-%{version}.so

%files -n libelf-devel
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
%defattr(-,root,root)
%{_libdir}/libdw.so.*
%{_libdir}/libdw-%{version}.so

%files -n libdw-devel
%defattr(-,root,root)
%{_libdir}/libdw.a
%{_libdir}/libdw.so
%{_includedir}/dwarf.h
%dir %{_includedir}/elfutils
%{_includedir}/elfutils/libdw.h
%{_includedir}/elfutils/libdwfl.h

%changelog
