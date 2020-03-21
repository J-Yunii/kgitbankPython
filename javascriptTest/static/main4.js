user = confirm('게속할까요??')
if(user==true) {
    // document는 html문서
    document.write('확인')
}
else {
    document.write(user)
}

// 디폴트값 안 적어도 됨, 적어도 되고...
user = prompt('프롬프트입니다. 이름을 입력하세요')
document.write('<br>'+user)