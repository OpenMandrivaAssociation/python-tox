# Created by pyp2rpm-3.3.5
# The tox documentation and the tox tests require a 
# working version of tox to run. If no such package 
# is available then you must first build with
# bootstrap enabled (the default) then build again
# once the basic tox package is built to run the 
# tests and to build the documentation.
# 

%global pypi_name tox
%bcond_with bootstrap
Name:           python-%{pypi_name}
Version:        4.23.2
Release:        1
Summary:        tox is a generic virtualenv management and test command line tool
Group:          Development/Python
License:        MIT
URL:            https://tox.readthedocs.org
Source0:        https://files.pythonhosted.org/packages/source/t/tox/tox-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python%{pyver}dist(colorama) >= 0.4.1
BuildRequires:  python%{pyver}dist(filelock) >= 3
BuildRequires:  python%{pyver}dist(flaky) >= 3.4
BuildRequires:  python%{pyver}dist(freezegun) >= 0.3.11
BuildRequires:  python-importlib-metadata >= 0.12
BuildRequires:  python%{pyver}dist(packaging) >= 14
BuildRequires:  python%{pyver}dist(pathlib2) >= 2.3.3
BuildRequires:  python%{pyver}dist(pluggy) >= 0.12
BuildRequires:  python%{pyver}dist(psutil) >= 5.6.1
BuildRequires:  python%{pyver}dist(py) >= 1.4.17
BuildRequires:  python-pygments-github-lexers >= 0.0.5
BuildRequires:  python%{pyver}dist(pytest) >= 4
BuildRequires:  python-pytest-cov >= 2.5.1
BuildRequires:  python-pytest-mock >= 1.10
BuildRequires:  python-pytest-randomly >= 1
BuildRequires:  python-pytest-xdist >= 1.22.2
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(six) >= 1.14
BuildRequires:  python%{pyver}dist(sphinx) >= 2
BuildRequires:  python-sphinxcontrib-autoprogram >= 0.1.5
BuildRequires:  python%{pyver}dist(toml) >= 0.9.4
BuildRequires:  python%{pyver}dist(towncrier) >= 18.5
BuildRequires:  (python%{pyver}dist(virtualenv) >= 16 with (python%{pyver}dist(virtualenv) < 20.0.7 or python%{pyver}dist(virtualenv) > 20.0.7) with (python%{pyver}dist(virtualenv) < 20.0.6 or python%{pyver}dist(virtualenv) > 20.0.6) with (python%{pyver}dist(virtualenv) < 20.0.5 or python%{pyver}dist(virtualenv) > 20.0.5) with (python%{pyver}dist(virtualenv) < 20.0.4 or python%{pyver}dist(virtualenv) > 20.0.4) with (python%{pyver}dist(virtualenv) < 20.0.3 or python%{pyver}dist(virtualenv) > 20.0.3) with (python%{pyver}dist(virtualenv) < 20.0.2 or python%{pyver}dist(virtualenv) > 20.0.2) with (python%{pyver}dist(virtualenv) < 20.0.1 or python%{pyver}dist(virtualenv) > 20.0.1) with (python%{pyver}dist(virtualenv) < 20 or python%{pyver}dist(virtualenv) > 20))
BuildRequires:  python%{pyver}dist(sphinx)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(hatch-vcs)

%description
tox is a generic virtualenv management and test command line tool

%if %{with bootstrap}
%package -n python-%{pypi_name}-doc
Summary:        tox documentation
%description -n python-%{pypi_name}-doc
Documentation for tox
BuildRequires:	tox
%endif

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
%if %{with bootstrap}
%BuildRequires:	tox
# generate html docs
PYTHONPATH=${PWD} sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%py3_install

%if %{with bootstrap}
%check
%{__python3} setup.py test
%endif

%files -n python-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/tox
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info

%if %{with bootstrap}
%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE
%endif
