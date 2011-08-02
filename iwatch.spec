%define name iwatch
%define version 0.2.2

Name:           %{name}
Summary:        iWatch is a realtime filesystem monitoring program
Version:        %{version}
Release:        %mkrel 1
License:        GPLv2
Group:          Monitoring
Requires:       perl-Linux-Inotify2 perl-Event perl-Mail-Sendmail perl-XML-LibXML perl-XML-SimpleObject-LibXML
Url:            http://iwatch.sourceforge.net
Source0:	http://downloads.sourceforge.net/project/iwatch/%{name}/%{version}/%{name}-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README iwatch.xml.example
%{_sysconfdir}/iwatch.xml
%{_sysconfdir}/iwatch.dtd
%{_bindir}/iwatch

%changelog
* Thu Mar 22 2007 tpatzig@suse.de
- update to version 0.2.1
  * option -X added (exception with regular expression)
  * new string formats in command option
  * send email for all defined events
* Tue Mar  6 2007 tpatzig@suse.de
- initial package build
