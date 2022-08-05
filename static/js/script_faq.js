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
