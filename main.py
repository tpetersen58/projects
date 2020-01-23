outFile = open('outputFile.txt', 'w')
outFile.truncate(0)
#inFile = open('inFile.txt','r')
print('This application will create a script that creates logins/databases for students in MIS3330.')
pw = input('Please type the desired password for student logins and press enter: ')
nameList = []
name = ''
while name != 'done':
    name = input('Enter the name of each login/database, pressing enter between each one. Enter \'done\' when finished: ')
    if name == 'done':
        break
    nameList.append(name)

for i in nameList:
    string = ''
    string = ('''CREATE DATABASE [''' + (i).strip('\n') + ''']
 CONTAINMENT = NONE
 ON  PRIMARY
( NAME = N\'''' + (i).strip('\n') + '''\', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL12.TOHEAVEN\MSSQL\DATA\\''' + (i).strip('\n') + '''.mdf' , SIZE = 4096KB , FILEGROWTH = 1024KB )
 LOG ON
( NAME = N\'''' + (i).strip('\n') + '''_log\', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL12.TOHEAVEN\MSSQL\DATA\\''' + (i).strip('\n') + '''_log.ldf' , SIZE = 6144KB , FILEGROWTH = 10%)
GO
ALTER DATABASE [''' + ((i).strip('\n')) + '''] SET COMPATIBILITY_LEVEL = 130
GO
ALTER DATABASE [''' + ((i).strip('\n')) + '''] SET ANSI_NULL_DEFAULT OFF
GO
ALTER DATABASE [''' + ((i).strip('\n')) + '''] SET ANSI_NULLS OFF
GO
ALTER DATABASE [''' + ((i).strip('\n')) + '''] SET ANSI_PADDING OFF
GO
ALTER DATABASE [''' + ((i).strip('\n')) + '''] SET ANSI_WARNINGS OFF
GO
ALTER DATABASE [''' + ((i).strip('\n')) + '''] SET ARITHABORT OFF
GO
ALTER DATABASE [''' + ((i).strip('\n')) + '''] SET AUTO_CLOSE OFF
GO
ALTER DATABASE [''' + ((i).strip('\n')) + '''] SET AUTO_SHRINK OFF
GO
ALTER DATABASE [''' + ((i).strip('\n')) + '''] SET AUTO_CREATE_STATISTICS ON(INCREMENTAL = OFF)
GO
ALTER DATABASE [''' + ((i).strip('\n')) + '''] SET AUTO_UPDATE_STATISTICS ON
GO
ALTER DATABASE [''' + ((i).strip('\n')) + '''] SET CURSOR_CLOSE_ON_COMMIT OFF
GO
ALTER DATABASE [''' + ((i).strip('\n')) + '''] SET CURSOR_DEFAULT  GLOBAL
GO
ALTER DATABASE [''' + ((i).strip('\n')) + '''] SET CONCAT_NULL_YIELDS_NULL OFF
GO
ALTER DATABASE [''' + ((i).strip('\n')) + '''] SET NUMERIC_ROUNDABORT OFF
GO
ALTER DATABASE [''' + ((i).strip('\n')) + '''] SET QUOTED_IDENTIFIER OFF
GO
ALTER DATABASE [''' + ((i).strip('\n')) + '''] SET RECURSIVE_TRIGGERS OFF
GO
ALTER DATABASE [''' + ((i).strip('\n')) + '''] SET  DISABLE_BROKER
GO
ALTER DATABASE [''' + ((i).strip('\n')) + '''] SET AUTO_UPDATE_STATISTICS_ASYNC OFF
GO
ALTER DATABASE [''' + ((i).strip('\n')) + '''] SET DATE_CORRELATION_OPTIMIZATION OFF
GO
ALTER DATABASE [''' + ((i).strip('\n')) + '''] SET PARAMETERIZATION SIMPLE
GO
ALTER DATABASE [''' + ((i).strip('\n')) + '''] SET READ_COMMITTED_SNAPSHOT OFF
GO
ALTER DATABASE [''' + ((i).strip('\n')) + '''] SET  READ_WRITE
GO
ALTER DATABASE [''' + ((i).strip('\n')) + '''] SET RECOVERY FULL
GO
ALTER DATABASE [''' + ((i).strip('\n')) + '''] SET  MULTI_USER
GO
ALTER DATABASE [''' + ((i).strip('\n')) + '''] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [''' + ((i).strip('\n')) + '''] SET TARGET_RECOVERY_TIME = 0 SECONDS
GO
ALTER DATABASE [''' + ((i).strip('\n')) + '''] SET DELAYED_DURABILITY = DISABLED
GO
USE [''' + ((i).strip('\n')) + ''']
GO
ALTER DATABASE SCOPED CONFIGURATION SET LEGACY_CARDINALITY_ESTIMATION = Off;
GO
ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET LEGACY_CARDINALITY_ESTIMATION = Primary;
GO
ALTER DATABASE SCOPED CONFIGURATION SET MAXDOP = 0;
GO
ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET MAXDOP = PRIMARY;
GO
ALTER DATABASE SCOPED CONFIGURATION SET PARAMETER_SNIFFING = On;
GO
ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET PARAMETER_SNIFFING = Primary;
GO
ALTER DATABASE SCOPED CONFIGURATION SET QUERY_OPTIMIZER_HOTFIXES = Off;
GO
ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET QUERY_OPTIMIZER_HOTFIXES = Primary;
GO
USE [''' + ((i).strip('\n')) + ''']
GO
IF NOT EXISTS (SELECT name FROM sys.filegroups WHERE is_default=1 AND name = N'PRIMARY') ALTER DATABASE [''' + ((i).strip('\n')) + '''] MODIFY FILEGROUP [PRIMARY] DEFAULT
GO

USE[master]
GO
CREATE LOGIN [''' + ((i).strip('\n')) + '''] WITH PASSWORD=N\'''' + pw + '''\', DEFAULT_DATABASE=[''' + ((i).strip('\n')) + '''], CHECK_EXPIRATION=OFF, CHECK_POLICY=OFF
GO
USE[''' + ((i).strip('\n')) + ''']
GO
CREATE USER [''' + ((i).strip('\n')) + '''] FOR LOGIN[''' + ((i).strip('\n')) + ''']
GO
USE[''' + ((i).strip('\n')) + ''']
GO
ALTER ROLE[db_owner] ADD MEMBER[''' + ((i).strip('\n')) + ''']
GO
''')
    outFile.write(string)
    outFile.write(";\r\n")

print('Finished. Output file (outputFile.txt) placed in directory you ran this application from.')
outFile.close()
input('In order to complete login/database creation, copy the contents of the output file into a Microsoft SQL Server Query and Execute. ')