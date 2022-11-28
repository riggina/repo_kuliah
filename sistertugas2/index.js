const express = require("express")
const app = express()

const port = 4000;

app.listen(port, () => {
    console.log(`Example App for Assignment listening on port ${port}`)
});

app.use(express.urlencoded({extended: true}))

app.get('/', (req, res) => {
    res.send("Welcome to Sistem Terdistribusi App")
})

app.get('/distribute', (req,res) => {
    res.json({
        "Mata Kuliah" : "Sistem Terdistribusi",
        "Kelas" : "B"
    })
});

app.post('/adding', (req, res) => {
    var body = req.body;
    console.log(req.body.dist);
    res.send(req.body.dist);
})

