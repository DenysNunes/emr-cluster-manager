CREATE DATABASE cluster_manager;

CREATE USER 'cluster_manager_user'@localhost IDENTIFIED BY 'default_password';

GRANT ALL PRIVILEGES ON cluster_manager.* TO 'cluster_manager_user'@'localhost';