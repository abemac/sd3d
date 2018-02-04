const express = require('express')
const app = express()
app.use(express.static('../big-print/dist/'))
app.listen(3000,'0.0.0.0', () => console.log('Started on port 3000'))