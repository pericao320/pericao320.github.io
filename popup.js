var btnAbrirpopup = document.getElementById('avance-edtd'),
    overlay = document.getElementById('overlay'),
    popup = document.getElementById('popup-edtd'),
    btnCerrarpopup = document.getElementById('btn-cerrar-popup');

btnAbrirpopup.addEventListener('click', function () {
    overlay.classList.add('active');
    popup.classList.add('active');
});

btnCerrarpopup.addEventListener('click', function () {
    overlay.classList.remove('active');
    popup.classList.remove('active');
});