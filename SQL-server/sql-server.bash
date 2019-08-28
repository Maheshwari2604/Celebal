#Install SQL Server
sudo curl -o /etc/yum.repos.d/mssql-server.repo https://packages.microsoft.com/config/rhel/7/mssql-server-preview.repo

#Run the following commands to install SQL Server:
sudo yum install -y mssql-server

#After the package installation finishes, run mssql-conf setup and follow the prompts to set the SA password and choose your edition.
sudo /opt/mssql/bin/mssql-conf setup

systemctl status mssql-server

sudo firewall-cmd --zone=public --add-port=1433/tcp --permanent
sudo firewall-cmd --reload

#CREATE TABLE Inventory (id INT, name NVARCHAR(50), quantity INT)