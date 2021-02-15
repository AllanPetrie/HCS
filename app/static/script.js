function validate(id){
    img_src = document.getElementById(id).src;
    window.location.assign("imageselect")
    changeImage(img_src)
  
}

function changeImage(src){
    console.log("In next function")
    image = document.getElementById("image2")
    img.src = src
}

// function change_image(src){

// }