s = 'hello world';
t = 'how are you ' + 'today';

document.write(s+'<br>')
document.write(t+'<br>')
document.write(s)
document.write(t)
// 소스상에서는 줄바꿈이 되나 웹브라우져 상에서는 줄바꿈이 되지 않는다. => 모두 태그 처리
document.writeln(s)
document.writeln(t)