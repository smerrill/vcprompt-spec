Name:           vcprompt
Version:        1.1
Release:        1%{?dist}
Summary:        An efficient program to print VCS information on your prompt

License:        GPLv2+
URL:            http://hg.gerg.ca/vcprompt/
Source0:        http://hg.gerg.ca/vcprompt/archive/%{version}.tar.gz

%description
vcprompt is a little C program that prints a short string, to be
included in your shell prompt, with bare-bones information about the
current working directory for various version control systems. It is
designed to be small and lightweight rather than comprehensive.

Currently, it has varying degrees of recognition for Mercurial, Git,
Subversion, CVS, and Fossil working copies.

vcprompt has no external dependencies: it does everything with the
standard C library and POSIX calls. It should work on any
POSIX-compliant system with a C99 compiler.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
%make_install PREFIX=%{_prefix} MANDIR=%{buildroot}%{_mandir}/man1

%files
%doc README.txt
%{_mandir}/man1/vcprompt.1*
%{_bindir}/vcprompt

%changelog
* Tue Jul 16 2013 Steven Merrill <steven.merrill@gmail.com> - 1.1-1
- Initial vcprompt RPM.

