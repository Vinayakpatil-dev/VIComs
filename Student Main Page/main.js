let btn= document.querySelector('button');
let dgb= document.querySelector('.services');
let cross= document.querySelector('span');

btn.addEventListener('click',function(){
    dgb.style.display = 'flex';
})

cross.addEventListener('click',function(){
    dgb.style.display = 'none';
})
