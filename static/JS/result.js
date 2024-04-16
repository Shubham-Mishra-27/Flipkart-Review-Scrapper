var rolla = gsap.timeline();
rolla.from('.row1',{
    y:-1000,
    opacity:0,
    // scale:0,
    duration:2,
    stagger:0.5
})
rolla.from('th',{
    scale:0
})
rolla.from('.row2',{
    y:-1000,
    opacity:0,
    duration:1
})
rolla.from('p',{
    x:-100,
    opacity:0,
    stagger:0.2
})
var nextbtn = document.querySelector('.next-btn');
var product = document.querySelector('#product');
var name11 = document.querySelector('#name');
var rating = document.querySelector('#rating');
var heading = document.querySelector('#heading');
var comment = document.querySelector('#comment');

function next(){
product.innerText = reviews[0];
name1.innerText = reviews[1];
rating.innerText = reviews[2];
heading.innerText = reviews[3];
comment.innerText = reviews[4];
}

next();
nextbtn.addEventListener('click',next);