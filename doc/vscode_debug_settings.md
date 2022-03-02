# vscode maven debug setting
``` json
{
    // See https://go.microsoft.com/fwlink/?LinkId=733558
    // for the documentation about the tasks.json format
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Tomcat debug",
            "type": "shell",
            "command": "mvn tomcat7:run",
            "group": "build",
            "problemMatcher": [],
            "isBackground": false,
            "options": {
                "env": {
                    "maven_opts": "-Xdebug -Xrunjdwp:transport=dt_socket,server=y,suspend=y,address=8000"
                }
            }
        }
    ]
}
```