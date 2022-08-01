function myFunction() {
    var x = document.getElementById('myInput');
    var k = document.getElementById('myInput1');
    var y = document.getElementById('hide1');
    var z = document.getElementById('hide2');
    var b = document.getElementById('hide3');
    var c = document.getElementById('hide4');


    if(x.type === 'password'){
        x.type = 'text'
        y.style.display = 'block';
        z.style.display = 'none'
    }
    else{
        x.type = 'password' 
        y.style.display = 'none';
        z.style.display = 'block'
    }
    if(k.type === 'password2' ){
        k.type = 'text'
        b.style.display = 'block';
        c.style.display = 'none'
    }
    else{
        k.type = 'password3' 
        b.style.display = 'none';
        c.style.display = 'block'
    }
}