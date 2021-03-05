function validate(id){
    
    img_src = document.getElementById(id).src;
    img_src = img_src.slice(-25)

    new_src = "..".concat(img_src)

    sessionStorage.setItem("image", new_src)
    // window.open(img_src);
    // window.open(img_src),'Image','width=largeImage.stylewidth,height=largeImage.style.height,resizable=1');
    window.location.assign("imageselect")
    
  
}

function changeImage(){
    console.log("In next function")
    
    src = sessionStorage.getItem("image")
    console.log(src)
    image = document.getElementById("image2")
    image.src = src
}

// function change_image(src){

// }
