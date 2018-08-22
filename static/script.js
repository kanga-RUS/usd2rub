$(document).ready(function(){
    $('#inputUSD').on('keydown', function(e){
            if(e.key.length > 0 && e.key.match(/[^0-9'".]/)){
            return false;
        };
    })
    $('button').click(function() {
        if ( !$('#inputUSD').val() ) {
               $('#error').html('Input can not be left blank');
        }
        else {
            $('#error').html(' ');
            $.ajax({
                url: '/convert',
                data: $('form').serialize(),
                type: 'POST',
                success: function(response) {
                    var result = JSON.parse(response);
                    $('#inputRUB').val(result.result)
                },
                error: function(error) {
                    console.log(error);
                    $('#error').html('Could not receive data from server');
                }
            });
        }
    });
});
