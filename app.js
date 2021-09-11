const express = require('express');
const app = express();
const fs = require('fs');
const port = process.env.PORT || 3000;
app.get('/', (req, res) => res.sendFile(__dirname + '/index.html'));
app.get('/about', (req, res) => res.send('<h1>This is About Page</h1>'));
app.listen(port, ()=>console.log(`Example app listening on port ${port}!`));

const menuText = fs.readFileSync("menu.txt");
const menus = menuText.toString().split('\n');
console.log(menus[100]);