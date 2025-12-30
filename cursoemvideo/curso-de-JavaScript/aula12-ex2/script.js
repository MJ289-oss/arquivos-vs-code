function verificar() {
    var data = new Date()
    var ano = data.getFullYear()
    var fano = document.getElementById('txtano')
    var res = document.querySelector('div#res')

    if (fano.value.length == 0 || Number(fano.value) > ano) {
        window.alert('Verifique os dados e tente novamente')
    } else {

        var fsex = document.getElementsByName('radsex')
        var idade = ano - Number(fano.value)
        var genero = ''
        var img = document.createElement('img')

        img.setAttribute('id', 'foto')
        img.style.width = '250px'
        img.style.height = '250px'

        if (fsex[0].checked) {
            genero = 'Homem'

            if (idade >= 0 && idade < 10) {
                img.setAttribute('src' , 'img/bebe.jpg')
                var genero = 'bebe'
            } else if ( idade < 21) {
                img.setAttribute('src' , 'img/adolescente-m.jpg')
                var genero = 'adolescente'
            } else if (idade < 50) {
                img.setAttribute('src' , 'img/homem.jpg')
                var genero = 'homem'
            } else {
                img.setAttribute('src' , 'img/idoso.jpg')
                var genero = 'idoso'
            }

        } else if (fsex[1].checked) {
            genero = 'Mulher'

            if (idade >= 0 && idade < 10) {
                img.setAttribute('src' , 'img/bebe.jpg')
                var genero = 'bebe'
            } else if ( idade < 21) {
                img.setAttribute('src' , 'img/adolescente-f.jpg')
                var genero = 'adolescente'
            } else if (idade < 50) {
                img.setAttribute('src' , 'img/mulher.jpg')
                var genero = 'mulher'
            } else {
                img.setAttribute('src' , 'img/idosa.jpg')
                var genero = 'idosa'
            }
        }
        res.style.textAlign = 'center'
        res.innerHTML = `Detectamos ${genero} com ${idade} anos`
        res.appendChild(img)
    }
}