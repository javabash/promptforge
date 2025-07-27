<%*
const { execSync } = require("child_process");

// ⚠️ Update this to the relative path of your script
const scriptPath = tp.user.prompt("Enter relative path to Python script (e.g., scripts/test.py):");
const output = execSync(`python ${scriptPath}`, { encoding: 'utf8' });

tR += `\`\`\`output\n${output}\n\`\`\``;
%>
