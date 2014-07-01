$(function (){
//    alert('Подключено!!!');
    username();
    $('#textbox').keypress(function(event){
        if ( event.which == 13){
            if ( $('#enter').prop('checked')){
                $('#submit').click();
                event.preventDefault();
            }
        }
    });
    $('#submit').click(function(){
        var newMessage = $('#textbox').val();

        var username = '<span class="you">Вы: </span>';

        $('#textbox').val('');

        var prevState = $('#display').html();
//        console.log('prevState.length = ' + prevState.length);
//        console.log('newMessage.length = ' + newMessage.length);
        if ( prevState.length > 10){
            prevState += '<br>';
        }
        if ( newMessage.length != 0 ){
            $('#display').html(prevState + username + newMessage);
            $('#display').scrollTop($('#display').prop('scrollHeight'));
        }

    });
});

function username(){
    $('#display').html('<span class="bot">Робот: </span> Привет! Как тебя зовут?')
}


//
//function trial(){
//    document.getElementById('demo').innerHTML = 'Hi, I am your javascript from an external source';
//}
//
//function trial_t(){
//    document.getElementById('demo').innerHTML = 'Привет єто я ';
//}
//function trial_h(){
//    $('#demo').hide();
//}
//function trial_s(){
//    $('#demo').show();
//}
//$('.btn-success').click(function(){
//        $('.btn-info').hide();
//        $(this).css('font-size', '55px');
//        $(this).css('color', 'black');