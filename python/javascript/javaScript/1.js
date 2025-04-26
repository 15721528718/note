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

// 2.数组
var v1 = [11,22,33,4,55,6];
var v2 = Array([2,1,3,4,5,6]);

//操作
v1.push('连通');//尾部追加   [11, 22, 33, 4, 55, 6, '连通']
console.log(v1);
v1.unshift("连通");//首部追加  ['连通', 11, 22, 33, 4, 55, 6, '连通']
console.log(v1);
v1.splice(1,0,'z');// ['连通', 'z', 11, 22, 33, 4, 55, 6, '连通']
console.log(v1);
v1.splice(1,1,'h');// ['连通', 'h', 11, 22, 33, 4, 55, 6, '连通']
console.log(v1);

v1.pop();//尾部删除
console.log(v1);
v1.shift();//首部删除
console.log(v1);
v1.splice(2,1);//索引为2的删除
console.log(v1);

// for循环遍历数组
for (var i = 0; i < v1.length; i++) {
    data = v1[i];
    console.log(data);
}
console.log("**********************************")
for (let i = 0; i < v1.length; i++) {
    data = v1[i];
    console.log(data);
}
console.log("**********************************")
for (var idx in v1){
    data = v1[idx];
    console.log(data);
}
console.log("**********************************")

// 动态数据
function dtdata(){
    var city = document.getElementById("city");
    var list = ["北京","上海","广州","深圳"]
    for(var i=0;i<list.length;i++){
        var tag = document.createElement("li");
        tag.innerText=list[i];
        city.appendChild(tag);
    }
}
dtdata();

// 字典
function zddata(){
    var data = [
        {id:1, name:"小明", age:19},
        {id:2, name:"小明", age:19},
        {id:3, name:"小明", age:19},
        {id:4, name:"小明", age:19},
        {id:5, name:"小明", age:19},
        {id:6, name:"小明", age:19},
        {id:7, name:"小明", age:19},
    ]
    var tbody = document.getElementById("tbody");
    for(var i=0;i<data.length;i++){
        var tagtr = document.createElement("tr");
        var zddata = data[i]
        console.log(zddata)
        for (var key in zddata){
            var tagtd = document.createElement("td");
            tagtd.innerText=zddata[key];
            tagtr.appendChild(tagtd);
            console.log(zddata[key]);
        }
        tbody.appendChild(tagtr);
    }
}
zddata()




























