<%*
const script = tp.user.prompt("Which Python file do you want to run?")
const vaultPath = app.vault.adapter.getBasePath()
const exec = require('child_process').exec
exec(`start cmd /k python "${vaultPath}\\${script}"`)
%>
