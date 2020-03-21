// getElementById: 엘리먼트를 id값으로 들고 옴
// id는 페이지 안에서 중복되지 않게

// getElementByName엘리먼트를 name값으로 들고 옴

function calc(){
    var x = document.getElementById('x').value;
    var y = document.getElementById('y').value;
    // parseInt: string을 int로 바꿔주는 함수
    sum = parseInt(x)+parseInt(y);
    document.getElementById('sum').value = sum;
}