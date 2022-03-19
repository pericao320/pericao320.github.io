const btnAbrirpopup = document.getElementById('avance-edtd'),
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

overlay.addEventListener('click', function () {
    overlay.classList.remove('active');
    popup.classList.remove('active');
});

/*- OVERLAY DE DISPONIVILIDAD -*/

const btnAbrirPopUpDisp = document.getElementById('reproducir-edtd'),
    btnCerrarPopUpDisp = document.getElementById('cerrar-overlay-disp'),
    popUpDisp = document.getElementById('overlay-disp'),
    contentpopUpDisp = document.getElementById('contenedor-overlay-de-disponibilidad');

let cerrarPopUpDisp = function () {
    contentpopUpDisp.classList.remove('active');
    popUpDisp.classList.remove('active');
}

btnAbrirPopUpDisp.addEventListener('click', function () {
    contentpopUpDisp.classList.add('active');
    popUpDisp.classList.add('active');
    setTimeout(cerrarPopUpDisp, 3500);
});

btnCerrarPopUpDisp.addEventListener('click', cerrarPopUpDisp);
