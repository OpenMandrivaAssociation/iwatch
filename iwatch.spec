%define name iwatch
%define version 0.2.2

Name:           %{name}
Summary:        Realtime filesystem monitoring program
Version:        %{version}
Release:        3
License:        GPLv2
Group:          Monitoring
Requires:       perl-Linux-Inotify2 perl-Event perl-Mail-Sendmail perl-XML-LibXML perl-XML-SimpleObject-LibXML
Url:            http://iwatch.sourceforge.net
Source0:	http://downloads.sourceforge.net/project/iwatch/%{name}/%{version}/%{name}-%{version}.tgz
BuildArch:      noarch

%description
iWatch monitor the filesystem's integrity in realtime and will send
alarm immediately to the system administrator when there is any changes
in the monitored filesystem. iWatch is written in Perl and based on
inotify, a file change notification system, a kernel feature that
allows applications to request the monitoring of a set of files against
a list of events.

Currently it can:

- run in command line mode as well as in daemon mode

- using an easy xml configuration file

- can watch directory recursively and watch new created directory

- can have a list of exceptions

- can use regex to compare the file/directory name

- can execute command if an event occures

- send email

- syslog

- print time stamp

%prep
%setup -q -n %{name}

%build

%install
install -d %buildroot/etc
install -p iwatch.xml %buildroot/etc/iwatch.xml
install -p iwatch.dtd %buildroot/etc/iwatch.dtd
install -d %buildroot/usr/bin
install -p iwatch %buildroot/usr/bin/iwatch

%clean

%files
%doc AUTHORS ChangeLog COPYING README iwatch.xml.example
%{_sysconfdir}/iwatch.xml
%{_sysconfdir}/iwatch.dtd
%{_bindir}/iwatch



%changelog
* Tue Aug 02 2011 Leonardo Coelho <leonardoc@mandriva.com> 0.2.2-1mdv2012.0
+ Revision: 692909
- import package into mdv and spec from suse
- Created package structure for iwatch.

