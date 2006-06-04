%define		_plugin	quicksave
%define		mversion	1.1.0
Summary:	Plugin that protects messages during composition
Summary(pl):	Wtyczka chroni±ca wiadomo¶ci w czasie ich tworzenia
Name:		squirrelmail-plugin-%{_plugin}
Version:	2.3
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://www.squirrelmail.org/plugins/%{_plugin}-%{version}-%{mversion}.tar.gz
# Source0-md5:	c60c68aace4eb67ccba4282327b13fdc
URL:		http://www.squirrelmail.org/
Requires:	squirrelmail >= 1.4.6-2
Requires:	squirrelmail-compatibility-2.0.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_datadir}/squirrelmail/plugins/%{_plugin}

%description
This plugin automatically saves the email message being composed from
accidental wipe out by refreshing the right frame or otherwise leaving
the Compose page.

It's all javascript on the Compose page, plus a form that we're using
for storage in the left_main frame. User won't ever know that it's
installed unless he have lost a message and it can be recovered.

%description -l pl
Wtyczka automatycznie zapisuj±ca tre¶æ wiadomo¶ci w czasie jej
tworzenia. Chroni przed utrat± tworzonej wiadomo¶ci na skutek
przypadkowego od¶wie¿enia lub prze³adowania strony.

Na wtyczkê sk³ada siê javascript na stronie tworzenia wiadomo¶ci oraz
formularz u¿ywany do zapisywania w lewym panelu. U¿ytkownik nie bêdzie
nawet wiedzia³ o istnieniu wtyczki do czasu a¿ straci wiadomo¶æ i
bêdzie w stanie j± odzyskaæ.

%prep
%setup -q -n %{_plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir} $RPM_BUILD_ROOT%{_sysconfdir}

install *.php $RPM_BUILD_ROOT%{_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL README
%dir %{_plugindir}
%{_plugindir}/*.php
