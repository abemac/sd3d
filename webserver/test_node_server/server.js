const express = require('express')
const app = express()
var cors = require('cors')
const spawn = require("child_process").spawn;
const url = require('url');

app.use(cors())
app.use(express.static('../big-print/dist/'))
var running = false
app.route('/startDemo').get((req,res)=>{
    var url_parts = url.parse(req.url, true);
    var query = url_parts.query;
    res.setHeader('content-type', 'text/plain');
    if(query.token == '6288260a217ca1838cd8c3f25d3fe475'){
        console.log('authenticated')
    }else{
        res.status(500).send("ERROR")
        return
    }
    if(running == false){
        running=true
        var pythonProcess = spawn('python3',["test.py"]);
        pythonProcess.stdout.on('data', function (data){
            console.log(String(data))
            running=false
        });
        res.status(200).send("SUCCESS")
    }else{
        res.status(500).send("ERROR")
    }
    
})
app.route('/status').get((req,res)=>{
    res.status(200).send(running)
    
    
})
app.listen(3000,'0.0.0.0', () => console.log('Started on port 3000'))