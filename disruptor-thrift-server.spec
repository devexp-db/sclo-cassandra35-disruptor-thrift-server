%{?scl:%scl_package disruptor-thrift-server}
%{!?scl:%global pkg_name %{name}}

Name:		%{?scl_prefix}disruptor-thrift-server
Version:	0.3.8
Release:	4%{?dist}
Summary:	Thrift Server implementation backed by LMAX Disruptor
License:	ASL 2.0
URL:		https://github.com/xedin/disruptor_thrift_server
Source0:	https://github.com/xedin/disruptor_thrift_server/archive/%{version}.tar.gz

BuildRequires:	%{?scl_prefix_maven}maven-local
BuildRequires:	%{?scl_prefix_maven}sonatype-oss-parent
BuildRequires:	%{?scl_prefix}disruptor
BuildRequires:	%{?scl_prefix}libthrift-java
# optional depenedencies
BuildRequires:	%{?scl_prefix_maven}jna
BuildRequires:	%{?scl_prefix_java_common}slf4j
BuildRequires:	%{?scl_prefix_java_common}log4j
# test dependency
BuildRequires:	%{?scl_prefix_java_common}junit
%{?scl:Requires: %scl_runtime}

BuildArch:     noarch

%description
Thrift Server implementation backed by LMAX Disruptor.
Shows better throughput/latency characteristics than build-in
THsHa and TThreadedSelector servers.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n disruptor_thrift_server-%{version}

%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin

# remove unnecessary dependency
%pom_remove_dep org.slf4j:slf4j-log4j12

%mvn_file : thrift-server %{pkg_name}
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
# Could not create ServerSocket - skipping tests
%mvn_build -f
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc README.md
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Thu Oct 20 2016 Tomas Repik <trepik@redhat.com> - 0.3.8-4
- use standard SCL macros

* Tue Aug 09 2016 Tomas Repik <trepik@redhat.com> - 0.3.8-3
- scl conversion

* Thu Feb 11 2016 Tomas Repik <trepik@redhat.com> - 0.3.8-2
- tests are skipped during build

* Wed Jul 22 2015 gil cattaneo <puntogil@libero.it> 0.3.8-1
- initial rpm
