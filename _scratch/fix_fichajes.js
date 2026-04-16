const fs = require('fs');

let js = fs.readFileSync('app.js', 'utf8');

// Añadiremos la lógica para hacer fetch de los checks de TODOS los empleados.
// Busco donde se hace el fetchFallback de checks en app.js y lo sustituyo.
