(function($){
	var result;
	var rubro;
	var maiz = "Maíz"
	$(document).ready(function(){
		$("#id_productor").select2();

		$('.inline-group .tabular tr.add-row td a').addClass('adicional');
		$('#semillas_set-group .form-row .field-rubro select').addClass('select-monitoreo');
		$('#procedenciasemilla_set-group .form-row .field-rubro select').addClass('select-monitoreo');
		$('#pruebagerminacion_set-group .form-row .field-rubro select').addClass('select-monitoreo');
		$('#sobrecosecha_set-group .form-row .field-rubro select').addClass('select-monitoreo');

		x = $("#id_productor option:selected").text();
		rubro = x.split("-");
		result = rubro[1];

		$('#id_productor').change(function(){
			x = $("#id_productor option:selected").text();
			rubro = x.split("-");
			result = rubro[1];
		});

    //semillas
    if ($('#id_areas_0').is(':checked')) {
			if (result == ' Maíz ') {
				$(".select-monitoreo option[value='2']").hide();
				$(".select-monitoreo option[value='1']").show();
			}else if (result == ' Frijol '){
				$(".select-monitoreo option[value='1']").hide();
				$(".select-monitoreo option[value='2']").show();
			}else {
				$(".select-monitoreo option[value='1']").show();
				$(".select-monitoreo option[value='2']").show();
			}
      $('#semillas_set-group').show();
      $('#procedenciasemilla_set-group').show();
      $('#pruebagerminacion_set-group').show();
    }else{
      $('#semillas_set-group').hide();
      $('#procedenciasemilla_set-group').hide();
      $('#pruebagerminacion_set-group').hide();
    };

    $('#id_areas_0').change(function(){
        if ($('#id_areas_0').is(':checked')) {
					if (result == ' Maíz ') {
						$(".select-monitoreo option[value='2']").hide();
						$(".select-monitoreo option[value='1']").show();
					}else if (result == ' Frijol '){
						$(".select-monitoreo option[value='1']").hide();
						$(".select-monitoreo option[value='2']").show();
					}else {
						$(".select-monitoreo option[value='1']").show();
						$(".select-monitoreo option[value='2']").show();
					}
          $('#semillas_set-group').show();
          $('#procedenciasemilla_set-group').show();
          $('#pruebagerminacion_set-group').show();
        }else{
          $('#semillas_set-group').hide();
          $('#procedenciasemilla_set-group').hide();
          $('#pruebagerminacion_set-group').hide();
        }
		});

    //suelo
    if ($('#id_areas_1').is(':checked')) {
      $('#suelo_set-group').show();
    }else{
      $('#suelo_set-group').hide();
    };

    $('#id_areas_1').change(function(){
        if ($('#id_areas_1').is(':checked')) {
          $('#suelo_set-group').show();
        }else{
          $('#suelo_set-group').hide();
        }
    });

    //macrofauna
    if ($('#id_areas_2').is(':checked')) {
      $('#macrofauna_set-group').show();
    }else{
      $('#macrofauna_set-group').hide();
    };

    $('#id_areas_2').change(function(){
        if ($('#id_areas_2').is(':checked')) {
          $('#macrofauna_set-group').show();
        }else{
          $('#macrofauna_set-group').hide();
        }
		});

    //malezas
    if ($('#id_areas_3').is(':checked')) {
      $('#monitoreomalezas_set-group').show();
      $('#tablamalezas_set-group').show();
    }else{
      $('#monitoreomalezas_set-group').hide();
      $('#tablamalezas_set-group').hide();
    };

    $('#id_areas_3').change(function(){
        if ($('#id_areas_3').is(':checked')) {
          $('#monitoreomalezas_set-group').show();
          $('#tablamalezas_set-group').show();
        }else{
          $('#monitoreomalezas_set-group').hide();
          $('#tablamalezas_set-group').hide();
        }
		});

    //vigor
    if ($('#id_areas_4').is(':checked')) {
			if (result == ' Maíz ') {
				$('#vigormaiz_set-group').show();
				$('#vigorfrijol_set-group').hide();
			} else if (result == ' Frijol '){
				$('#vigorfrijol_set-group').show();
				$('#vigormaiz_set-group').hide();
			}else {
				$('#vigormaiz_set-group').show();
				$('#vigorfrijol_set-group').show();
			}

    }else{
      $('#vigorfrijol_set-group').hide();
      $('#vigormaiz_set-group').hide();
    };

    $('#id_areas_4').change(function(){
			if ($('#id_areas_4').is(':checked')) {
				if (result == ' Maíz ') {
						$('#vigormaiz_set-group').show();
						$('#vigorfrijol_set-group').hide();
					} else if (result == ' Frijol '){
						$('#vigorfrijol_set-group').show();
						$('#vigormaiz_set-group').hide();
					} else {
						$('#vigormaiz_set-group').show();
						$('#vigorfrijol_set-group').show();
					}
        }else{
          $('#vigorfrijol_set-group').hide();
          $('#vigormaiz_set-group').hide();
        }
    });

    //plagas y enfermedades
    if ($('#id_areas_5').is(':checked')) {
			if (result == ' Maíz ') {
				$('#plagasmaiz_set-group').show();
				$('#enfermedadesmaiz_set-group').show();
				$('#enfermedadesfrijol_set-group').hide();
				$('#plagasfrijol_set-group').hide();
			} else if (result == ' Frijol '){
				$('#plagasfrijol_set-group').show();
				$('#enfermedadesfrijol_set-group').show();
				$('#plagasmaiz_set-group').hide();
				$('#enfermedadesmaiz_set-group').hide();
			}else {
				$('#plagasfrijol_set-group').show();
	      $('#plagasmaiz_set-group').show();
	      $('#enfermedadesfrijol_set-group').show();
	      $('#enfermedadesmaiz_set-group').show();
			}

    }else{
      $('#plagasfrijol_set-group').hide();
      $('#plagasmaiz_set-group').hide();
      $('#enfermedadesfrijol_set-group').hide();
      $('#enfermedadesmaiz_set-group').hide();
    };

    $('#id_areas_5').change(function(){
        if ($('#id_areas_5').is(':checked')) {
					if (result == ' Maíz ') {
						$('#plagasmaiz_set-group').show();
						$('#enfermedadesmaiz_set-group').show();
						$('#enfermedadesfrijol_set-group').hide();
						$('#plagasfrijol_set-group').hide();
					} else if (result == ' Frijol '){
						$('#plagasfrijol_set-group').show();
						$('#enfermedadesfrijol_set-group').show();
						$('#plagasmaiz_set-group').hide();
						$('#enfermedadesmaiz_set-group').hide();
					}else {
						$('#plagasfrijol_set-group').show();
			      $('#plagasmaiz_set-group').show();
			      $('#enfermedadesfrijol_set-group').show();
			      $('#enfermedadesmaiz_set-group').show();
					}
        }else{
          $('#plagasfrijol_set-group').hide();
          $('#plagasmaiz_set-group').hide();
          $('#enfermedadesfrijol_set-group').hide();
          $('#enfermedadesmaiz_set-group').hide();
        }
    });

    //poblacion
    if ($('#id_areas_6').is(':checked')) {
			if (result == ' Maíz ') {
				$('#poblacionmaiz_set-group').show();
				$('#poblacionfrijol_set-group').hide();
			} else if (result == ' Frijol '){
				$('#poblacionfrijol_set-group').show();
				$('#poblacionmaiz_set-group').hide();
			} else {
				$('#poblacionmaiz_set-group').show();
				$('#poblacionfrijol_set-group').show();
			}
    }else{
      $('#poblacionfrijol_set-group').hide();
      $('#poblacionmaiz_set-group').hide();
    };

    $('#id_areas_6').change(function(){
			if ($('#id_areas_6').is(':checked')) {
				if (result == ' Maíz ') {
					$('#poblacionmaiz_set-group').show();
					$('#poblacionfrijol_set-group').hide();
				} else if (result == ' Frijol '){
					$('#poblacionfrijol_set-group').show();
					$('#poblacionmaiz_set-group').hide();
				} else {
					$('#poblacionmaiz_set-group').show();
					$('#poblacionfrijol_set-group').show();
				}
	    }else{
	      $('#poblacionfrijol_set-group').hide();
	      $('#poblacionmaiz_set-group').hide();
	    }
    });

    //estimado cosecha
    if ($('#id_areas_7').is(':checked')) {
			if (result == ' Maíz ') {
	      $('#estimadocosechamaiz_set-group').show();
	      $('#estimadocosechamaiz2_set-group').show();
				$('#estimadocosechafrijol_set-group').hide();
				$('#granosplanta_set-group').hide();
			} else if (result == ' Frijol '){
				$('#estimadocosechamaiz_set-group').hide();
	      $('#estimadocosechamaiz2_set-group').hide();
				$('#estimadocosechafrijol_set-group').show();
				$('#granosplanta_set-group').show();
			} else {
				$('#estimadocosechafrijol_set-group').show();
	      $('#granosplanta_set-group').show();
	      $('#estimadocosechamaiz_set-group').show();
	      $('#estimadocosechamaiz2_set-group').show();
			}
    }else{
      $('#estimadocosechafrijol_set-group').hide();
      $('#granosplanta_set-group').hide();
      $('#estimadocosechamaiz_set-group').hide();
      $('#estimadocosechamaiz2_set-group').hide();
    };

    $('#id_areas_7').change(function(){
        if ($('#id_areas_7').is(':checked')) {
					if (result == ' Maíz ') {
			      $('#estimadocosechamaiz_set-group').show();
			      $('#estimadocosechamaiz2_set-group').show();
						$('#estimadocosechafrijol_set-group').hide();
						$('#granosplanta_set-group').hide();
					} else if (result == ' Frijol '){
						$('#estimadocosechamaiz_set-group').hide();
			      $('#estimadocosechamaiz2_set-group').hide();
						$('#estimadocosechafrijol_set-group').show();
						$('#granosplanta_set-group').show();
					} else {
						$('#estimadocosechafrijol_set-group').show();
			      $('#granosplanta_set-group').show();
			      $('#estimadocosechamaiz_set-group').show();
			      $('#estimadocosechamaiz2_set-group').show();
					}
        }else{
          $('#estimadocosechafrijol_set-group').hide();
          $('#granosplanta_set-group').hide();
          $('#estimadocosechamaiz_set-group').hide();
          $('#estimadocosechamaiz2_set-group').hide();
        }
    });

    //almacenamiento
    if ($('#id_areas_8').is(':checked')) {
			if (result == ' Maíz ') {
				$(".select-monitoreo option[value='2']").hide();
				$("#sobrecosecha_set-group .adicional").hide();
			}else if (result == ' Frijol '){
				$(".select-monitoreo option[value='1']").hide();
				$("#sobrecosecha_set-group .adicional").hide();
			} else {
				$(".select-monitoreo option[value='1']").show();
				$(".select-monitoreo option[value='2']").show();
				$("#sobrecosecha_set-group .adicional").show();
			}
      $('#sobrecosecha_set-group').show();
      $('#curadosemilla_set-group').show();
    }else{
      $('#sobrecosecha_set-group').hide();
      $('#curadosemilla_set-group').hide();
    };

    $('#id_areas_8').change(function(){
        if ($('#id_areas_8').is(':checked')) {
					if (result == ' Maíz ') {
						$(".select-monitoreo option[value='2']").hide();
						$("#sobrecosecha_set-group .adicional").hide();
					}else if (result == ' Frijol '){
						$(".select-monitoreo option[value='1']").hide();
						$("#sobrecosecha_set-group .adicional").hide();
					} else {
						$(".select-monitoreo option[value='1']").show();
						$(".select-monitoreo option[value='2']").show();
						$("#sobrecosecha_set-group .adicional").show();
					}
          $('#sobrecosecha_set-group').show();
          $('#curadosemilla_set-group').show();
        }else{
          $('#sobrecosecha_set-group').hide();
          $('#curadosemilla_set-group').hide();
        }
    });

  });
})(jQuery || django.jQuery);
