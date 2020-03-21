

function gugu() {
    var dan = document.getElementById('dan').value;
    var str = '';
    for(var i=1;i<=9;i++) {
        str+=dan+'x'+i+'='+dan*i+'<br>';
    }
    document.getElementById('result').innerHTML=str;
}

function enter() {
    // 어떤게 눌러지는지 keyCode로 한번 찍어보자 => 콘솔에 출력됨
    console.log(window.event.keyCode);
    // 13은 엔터키!
    if(window.event.keyCode==13) {
        gugu();
    }

}