%define		_plugin	quicksave
%define		mversion	1.1.0
Summary:	Plugin that protects messages during composition
Summary(pl.UTF-8):	Wtyczka chroniąca wiadomości w czasie ich tworzenia
Name:		squirrelmail-plugin-%{_plugin}
Version:	2.3
Release:	2
License:	GPL
Group:		Applications/Mail
Source0:	http://www.squirrelmail.org/plugins/%{_plugin}-%{version}-%{mversion}.tar.gz
# Source0-md5:	c60c68aace4eb67ccba4282327b13fdc
URL:		http://www.squirrelmail.org/plugin_view.php?id=8
Requires:	squirrelmail >= 1.4.6-2
Requires:	squirrelmail-compatibility >= 2.0.4
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

%description -l pl.UTF-8
Wtyczka automatycznie zapisująca treść wiadomości w czasie jej
tworzenia. Chroni przed utratą tworzonej wiadomości na skutek
przypadkowego odświeżenia lub przeładowania strony.

Na wtyczkę składa się javascript na stronie tworzenia wiadomości oraz
formularz używany do zapisywania w lewym panelu. Użytkownik nie będzie
nawet wiedział o istnieniu wtyczki do czasu aż straci wiadomość i
będzie w stanie ją odzyskać.

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
