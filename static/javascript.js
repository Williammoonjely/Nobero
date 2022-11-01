let menu=document.getElementById('s_0_1')

menu.addEventListener("click",function(){
    // console.log('button is clicked')

    document.getElementById('s_5').style.display="block"
    document.getElementById('s_4').style.display="none"

})
let close=document.getElementById('s_0_2')

close.addEventListener("click",function(){
    // console.log('close is clicked')

    document.getElementById('s_4').style.display="block"
    document.getElementById('s_5').style.display="none"
})
