var rolla = gsap.timeline();
var name1 = document.querySelector('#name');
var comment = document.querySelector('#Comment');

rolla.from('.long-bar',{
    x:-100,
    opacity:0,
    duration:1
})
rolla.from('.big-text h1',{
    x:-300,
    opacity:0,
    scale:0,
    duration:1,
    stagger:0.5
})
rolla.to('.big-text h1 , .long-bar',{
    x:-800,
    opacity:0,
    delay:1,
    duration:1
})
rolla.from('#search-area,#search-btn',{
    opacity:0,
    scale:0,
    duration:1,
    stagger:0.5
})