<<<<<<< HEAD
// FAQ DOM
faqList = document.querySelectorAll('.faq-list-child')
faqParagraphText = document.querySelectorAll('.faq-paragraph-text')
faqPlus = document.querySelectorAll('.faq-plus-icon')
faqMinus = document.querySelectorAll('.faq-minus-icon')
faqToggle = false

faqPlus.forEach( (e, index) => {
    e.addEventListener('click', ()=>{
        faqParagraphText[index].classList.add("show-element")
        faqMinus[index].classList.add("show-element")
        e.classList.add("hide-element")
    })
});

faqMinus.forEach( (e, index) => {
    e.addEventListener('click', ()=>{
        faqParagraphText[index].classList.remove("show-element")
        faqPlus[index].classList.remove("hide-element")
        e.classList.remove("show-element")
    })
});

// FAQ DOM END
=======
function myFunction() {
    var x = document.getElementById('myInput');
    var y = document.getElementById('hide1');
    var z = document.getElementById('hide2');

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
}
>>>>>>> 4b08b4c7d1f46578ad96991880cc87776e1093bf
