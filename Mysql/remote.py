name = input("Enter UserName ")
database = input("Enter Database ")

print("CREATE USER '" + name + "'@'%';\n GRANT USAGE ON *.* TO '" + name + "'@'%';\n GRANT ALL PRIVILEGES ON `" + database + "`.* TO '" + name + "'@'%' WITH GRANT OPTION; ")
