var myWindow;

function openWin(){
    // url,창 name, size
    myWindow = window.open("https://www.naver.com/","myWindow",
    'top=250,left=800,width=200,height=300');
    myWindow.document.write("<p>This is 'myWindow'</p>");
}

function closeWin(){
    myWindow.close();
}