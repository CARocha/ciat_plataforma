(function($){
	$(document).ready(function(){
    valor = $('#id_acceso_agua').val();
    if (valor == 1) {
      $('.field-acceso_agua .inline').show();
      $('.field-acceso_agua #id_fuente_agua').show();
      $('.field-distancia #id_distancia').show();
    } else {
			$('.field-acceso_agua .inline').hide();
			$('.field-acceso_agua #id_fuente_agua').hide();
			$('.field-distancia #id_distancia').hide();
    }

    $('#id_acceso_agua').change(function(){
      valor = $('#id_acceso_agua').val();
      if (valor == 1) {
        $('.field-acceso_agua .inline').show();
        $('.field-acceso_agua #id_fuente_agua').show();
        $('.field-distancia #id_distancia').show();
      } else {
        $('.field-acceso_agua .inline').hide();
        $('.field-acceso_agua #id_fuente_agua').hide();
        $('.field-distancia #id_distancia').hide();
      }
    });

		// js de cultivo
		// add classes
		$('.inline-group .tabular tr.add-row td a').addClass('adicional');
		$('#datosmonitoreo_set-group .form-row select').addClass('select-monitoreo');
		$('#recursossiembra_set-group .form-row .field-rubro select').addClass('select-monitoreo');
		$('#historialrendimiento_set-group .form-row .field-rubro select').addClass('select-monitoreo');

		$('#datosmonitoreo_set-group .adicional').click(function(){
			valor = $('#id_cultivo').val();
			if (valor == 1) {
				$(".select-monitoreo option[value='2']").hide();
				$(".select-monitoreo option[value='1']").show();
			} else if (valor == 2){
				$(".select-monitoreo option[value='1']").hide();
				$(".select-monitoreo option[value='2']").show();
			} else {
				$(".select-monitoreo option[value='1']").show();
				$(".select-monitoreo option[value='2']").show();
			}
		});

		$('#id_cultivo').change(function(){
			valor = $('#id_cultivo').val();
			if (valor == 1) {
				$(".select-monitoreo option[value='2']").hide();
				$(".select-monitoreo option[value='1']").show();
			} else if (valor == 2){
				$(".select-monitoreo option[value='1']").hide();
				$(".select-monitoreo option[value='2']").show();
			} else {
				$(".select-monitoreo option[value='1']").show();
				$(".select-monitoreo option[value='2']").show();
			}
		});


  });
})(jQuery || django.jQuery);
