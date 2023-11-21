//scrip de validacion de seguridad
const fs = require("fs");
const path = require("path");

const files = fs.readdirSync(path.join(__dirname, "src"));

files.forEach((file) => {
  const filePath = path.join(__dirname, "src", file);
  if (file.endsWith(".js")) {
    const content = fs.readFileSync(filePath, "utf8");
    const vulnerabilities = snyk.analyze(content);
    if (vulnerabilities.length > 0) {
      console.log(`Encontradas vulnerabilidades en el archivo ${file}`);
      vulnerabilities.forEach((vulnerability) => {
        console.log(`- ${vulnerability.description}`);
      });
    }
  }
});
