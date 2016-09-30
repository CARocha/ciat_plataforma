(function($){
  $(document).ready(function(){
    var s0;
    $('#id_usosuelo_set-0-uso').change(function(){
      s0 = $('#id_usosuelo_set-0-uso').val();
    });

    $('#usosuelo_set-group .add-row').click(function(){
      var s1;
      $('#id_usosuelo_set-1-uso').change(function(){
        s1 = $('#id_usosuelo_set-1-uso').val();
        alert(s1);
      });

      for (var i = 0; i < 5; i++) {
        // $('#id_usosuelo_set-'+(i+1)+'-uso option[value="'+s0+'"]').hide();
        $('#id_usosuelo_set-'+(i+1)+'-uso option[value="'+s1+'"]').hide();
      }
    });
  });
})(jQuery || django.jQuery);
