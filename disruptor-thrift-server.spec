Name:          disruptor-thrift-server
Version:       0.3.8
Release:       2%{?dist}
Summary:       Thrift Server implementation backed by LMAX Disruptor
License:       ASL 2.0
URL:           https://github.com/xedin/disruptor_thrift_server
Source0:       https://github.com/xedin/disruptor_thrift_server/archive/%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.lmax:disruptor)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(net.java.dev.jna:jna)
BuildRequires: mvn(org.apache.thrift:libthrift)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-log4j12)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

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

%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin

%mvn_file : thrift-server %{name}

%build
# Could not create ServerSocket - skipping tests
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Thu Feb 11 2016 Tomas Repik <trepik@redhat.com> - 0.3.8-2
- Tests are skipped during build

* Wed Jul 22 2015 gil cattaneo <puntogil@libero.it> 0.3.8-1
- initial rpm
