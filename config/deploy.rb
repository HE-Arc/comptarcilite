# config valid for current version and patch releases of Capistrano
lock "~> 3.12.1"

set :application, "comptarcilite"
set :repo_url, "https://github.com/HE-Arc/comptarcilite.git"

after 'deploy:publishing', 'uwsgi:restart'

namespace :uwsgi do
    desc 'Restart application'
    task :restart do
        on roles(:web) do |h|
	    execute :sudo, 'sv reload uwsgi'
	end
    end
end

after 'deploy:updating', 'python:create_venv'
namespace :python do
    def venv_path
        File.join(shared_path, 'env')
    end

    desc 'Create venv'
    task :create_venv do
        on roles([:app, :web]) do |h|
	    execute "python3.6 -m venv #{venv_path}"
           execute "source #{venv_path}/bin/activate"
	    execute "#{venv_path}/bin/pip install -r #{release_path}/requirements.txt"
        end
    end
end

after 'deploy:symlink:release', 'django:configuration'


namespace :django do
    desc 'Gestion de la configuration'
	
    task :configuration do
        on roles(:web) do |h|
	    execute "cp /home/poweruser/valeurs /var/www/comptarcilite/current/.env"
		execute "cp /home/poweruser/settings_withcred.py /var/www/comptarcilite/current/comptarcilite/settings.py"
        end
    end
	   
	task :migration do
        on roles(:web) do |h|
	    execute "python3.6 -m venv #{venv_path}"
           execute "source #{venv_path}/bin/activate"
	    execute "#{venv_path}/bin/python3.6 #{release_path}/manage.py migrate"
		execute "#{venv_path}/bin/python3.6 #{release_path}/manage.py makemigrations"
		execute "#{venv_path}/bin/python3.6 #{release_path}/manage.py collectstatic"
		end
    end
	
	task :finishmigration do
        on roles(:web) do |h|
		execute "cp /home/poweruser/settings.py /var/www/comptarcilite/current/comptarcilite/settings.py"
		end
    end
end


after 'django:configuration', 'django:migration'
after 'django:migration', 'django:finishmigration'
after 'django:finishmigration', 'uwsgi:restart'

# Default branch is :master
# ask :branch, `git rev-parse --abbrev-ref HEAD`.chomp

# Default deploy_to directory is /var/www/my_app_name
# set :deploy_to, "/var/www/my_app_name"

# Default value for :format is :airbrussh.
# set :format, :airbrussh

# You can configure the Airbrussh format using :format_options.
# These are the defaults.
# set :format_options, command_output: true, log_file: "log/capistrano.log", color: :auto, truncate: :auto

# Default value for :pty is false
# set :pty, true

# Default value for :linked_files is []
# append :linked_files, "config/database.yml"

# Default value for linked_dirs is []
# append :linked_dirs, "log", "tmp/pids", "tmp/cache", "tmp/sockets", "public/system"

# Default value for default_env is {}
# set :default_env, { path: "/opt/ruby/bin:$PATH" }

# Default value for local_user is ENV['USER']
# set :local_user, -> { `git config user.name`.chomp }

# Default value for keep_releases is 5
# set :keep_releases, 5

# Uncomment the following to require manually verifying the host key before first deploy.
# set :ssh_options, verify_host_key: :secure
