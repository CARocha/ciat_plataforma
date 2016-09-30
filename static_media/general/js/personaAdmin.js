(function($){

    $(document).ready(function(){

        var valor_tipo1 = $('#id_tipo_persona').val();

        if (valor_tipo1 == '1') {
            $('#productor_set-group').show();
        }else{
            $('#productor_set-group').hide();
        };

        if (valor_tipo1 == '2') {
            $('#lideres_set-group').show();
        }else{
            $('#lideres_set-group').hide();
        };

         if (valor_tipo1 == '3' || valor_tipo1 == '4' || valor_tipo1 == '5') {
            $('#tecnicoespinvestigador_set-group').show();
        }else{
            $('#tecnicoespinvestigador_set-group').hide();
        };

        if (valor_tipo1 == '6') {
            $('#decisor_set-group').show();
        }else{
            $('#decisor_set-group').hide();
        };

        $('#id_tipo_persona').change(function(){
            var valor_tipo1 = $('#id_tipo_persona').val();
            if (valor_tipo1 == '1') {
                $('#productor_set-group').show();
            }else{
                $('#productor_set-group').hide();
            };

            if (valor_tipo1 == '2') {
                $('#lideres_set-group').show();
            }else{
                $('#lideres_set-group').hide();
            };

            if (valor_tipo1 == '3' || valor_tipo1 == '4' || valor_tipo1 == '5') {
                $('#tecnicoespinvestigador_set-group').show();
            }else{
                $('#tecnicoespinvestigador_set-group').hide();
            };

            if (valor_tipo1 == '6') {
                $('#decisor_set-group').show();
            }else{
                $('#decisor_set-group').hide();
            };

        });


    });
})(jQuery || django.jQuery)
