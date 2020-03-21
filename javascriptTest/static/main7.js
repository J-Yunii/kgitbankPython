function seasonimg(){
    var season = prompt('좋아하는 계절은?','봄');
    var message = "";
    var img = "";
    switch(season) {
        case '봄':
            message='봄을 좋아하시네요.';
            img='spring.jpg';
            break;
        case '여름':
            message='여름을 좋아하시네요.';
            img='summer.jpeg';
            break;
        case '가을':
            message='가을을 좋아하시네요.';
            img='fall.jpg';
            break;
        case '겨울':
            message='겨울을 좋아하시네요.';
            img='winter.jpg';
            break;
        default:
            alert('번호를 잘못 입력했습니다.(1-4를 눌러주세요.)');
    }

    document.getElementById('message').innerHTML = message;
    document.getElementById('img').src = '/static/img/'+img;
}