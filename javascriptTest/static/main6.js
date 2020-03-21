function func(){
    var e = document.getElementById('test');
    // document.write를 쓰면 기존의 내용을 없애고 삽입하는 문제가 생김
    // document.write(typeof(e))
    // document.write('<br>')

    // 속성이름(ex> style)가지고 와서 바꾸면 됨
    e.style.color = 'red';
    e.style.background = 'yellow';
}