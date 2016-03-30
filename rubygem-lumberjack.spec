#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-lumberjack
Version  : 1.0.10
Release  : 6
URL      : https://rubygems.org/downloads/lumberjack-1.0.10.gem
Source0  : https://rubygems.org/downloads/lumberjack-1.0.10.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-devise
BuildRequires : rubygem-diff-lcs
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-rspec-mocks
BuildRequires : rubygem-rspec-support
BuildRequires : rubygem-timecop

%description
= Lumberjack
Lumberjack is a simple, powerful, and fast logging implementation in Ruby. It uses nearly the same API as the Logger class in the Ruby standard library and as ActiveSupport::BufferedLogger in Rails.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n lumberjack-1.0.10
gem spec %{SOURCE0} -l --ruby > rubygem-lumberjack.gemspec

%build
gem build rubygem-lumberjack.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
lumberjack-1.0.10.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/lumberjack-1.0.10
rspec -I.:lib spec/
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/lumberjack-1.0.10.gem
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/MIT_LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/README.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/VERSION
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/lib/lumberjack.rb
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/lib/lumberjack/device.rb
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/lib/lumberjack/device/date_rolling_log_file.rb
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/lib/lumberjack/device/log_file.rb
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/lib/lumberjack/device/null.rb
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/lib/lumberjack/device/rolling_log_file.rb
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/lib/lumberjack/device/size_rolling_log_file.rb
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/lib/lumberjack/device/writer.rb
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/lib/lumberjack/formatter.rb
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/lib/lumberjack/formatter/exception_formatter.rb
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/lib/lumberjack/formatter/inspect_formatter.rb
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/lib/lumberjack/formatter/pretty_print_formatter.rb
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/lib/lumberjack/formatter/string_formatter.rb
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/lib/lumberjack/log_entry.rb
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/lib/lumberjack/logger.rb
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/lib/lumberjack/rack.rb
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/lib/lumberjack/rack/unit_of_work.rb
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/lib/lumberjack/severity.rb
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/lib/lumberjack/template.rb
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/spec/device/date_rolling_log_file_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/spec/device/log_file_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/spec/device/null_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/spec/device/rolling_log_file_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/spec/device/size_rolling_log_file_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/spec/device/writer_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/spec/formatter/exception_formatter_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/spec/formatter/inspect_formatter_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/spec/formatter/pretty_print_formatter_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/spec/formatter/string_formatter_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/spec/formatter_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/spec/log_entry_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/spec/logger_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/spec/lumberjack_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/spec/rack/unit_of_work_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/spec/severity_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/lumberjack-1.0.10/spec/template_spec.rb
/usr/lib64/ruby/gems/2.3.0/specifications/lumberjack-1.0.10.gemspec
