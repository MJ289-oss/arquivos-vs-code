function carregar() {
    var msg = window.document.getElementById('msg')
    var img = window.document.getElementById('imagem')
    var data = new Date()
    var hora = data.getHours()
    var min = data.getMinutes()
    msg.innerHTML = `Agora são ${hora} horas e ${min} minutos.`
     
    if (hora >= 0 && hora < 12) {
        img.src = 'img/manha.jpg'
        document.body.style.background = 'lightblue'
    } else if (hora >= 12 && hora < 18) {
        img.src = 'img/tarde.jpg'
        document.body.style.background = '#b9846f'
    }else {
        img.src = 'img/noite.jpg'
        document.body.style.background = 'darkblue'
    }
}
