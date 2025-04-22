// 1.字符串类型
// var name = "中国联通    ";
// var v1 = name.length;
// var v2 = name[0];// == name.charAt(0)
// var v3 = name.trim();//去除字符串两端空白字符
// var v4 = name.substring(0,2);//前取后不取
// console.log(name);
// console.log(v1);
// console.log(v2);
// console.log(v3);
// console.log(v4);
function showTxt1(){
    var tag1 = document.getElementById("txt1");
    var data1 = tag1.innerText;

    var firsttxt1 = data1[0];
    var othertxt1 = data1.substring(1,data1.length);
    var newtxt1 = othertxt1 + firsttxt1;
    tag1.innerText = newtxt1;
}
// setInterval(showTxt1, 180);