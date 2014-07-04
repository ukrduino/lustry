$(function (){
//    alert('Подключено!!!');
    get_username();

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
            ai(newMessage);
        }

    });
});

var username = '';

function get_username(){
    send_message('Привет! Как тебя зовут?');

}
function ai(newMessage){
    if( username < 10 ){
        username = newMessage;
        send_message('Привет, '+ username + '! Как дела???');
    }
    if (newMessage.indexOf('как дела')>=0){
        send_message('Спасибо! Неплохо!');

    }
    if (newMessage.indexOf('час')>=0){
        var date = new Date();
        var h = date.getHours();
        var m = date.getMinutes();
        send_message('Текущее время: '+ h + ':' + m);
    }
}

function send_message(messageFromAI){
    var prevState = $('#display').html();

    if ( prevState.length > 10){
        prevState += '<br>';
    }

        $('#display').html(prevState + '<span class="currentMessage">' + '<span class="bot">Робот: </span>' + messageFromAI + '</span>');
        $('.currentMessage').hide();
        $('.currentMessage').delay(500).fadeIn();
        $('.currentMessage').removeClass('currentMessage');




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