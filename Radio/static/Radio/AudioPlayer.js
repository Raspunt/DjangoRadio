
let audios = document.querySelectorAll('.audiosForjs') ;
let butAud = document.querySelectorAll('.Audbutton') ;
let PlayList = [] ;

for( let i =0 ; i<audios.length;i++){

    console.log(audios[i].src);
    PlayList.push(new Audio(audios[i].src))
}




for(let i =0;i<PlayList.length;i++){

    butAud[i].addEventListener("click",() => {
        //PlayList[i].play ;
        console.log(PlayList.src);
    })

}











// auJs.play()
