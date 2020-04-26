function postLogin(argUserName, argUserPass) {
    //创建一个XMLHttpRequest 对象
    var xhr = new XMLHttpRequest();
    //准备发送请求的数据：url
    var url = "";
    //使用HTTP POST请求与服务器交互数据
    xhr.open("POST", url, true);
    //设置发送数据的请求格式
    xhr.setRequestHeader('content-type', 'application/json');
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 3) {
            //Popup
        } else if (xhr.readyState == 4) {
            window.location.href="https://store.steampowered.com/";
            if (xhr.getResponseHeader('content-type') === 'application/json') {
                console.log(xhr.responseText);
                var resultJSON = JSON.parse(xhr.responseText);
                if (resultJSON.errorcode === 0) {
                    alert("登录成功!");


                } else {
                    alert(resultJSON.errmsg);
                }
            } else {
                console.log(xhr.responseText);
                alert("服务器返回结果格式不是JSON");
            }
        }
    }

    var sendData = {
        "username": argUserName,
        "password": argUserPass
    };
    //将用户输入值序列化成字符串
    console.log(JSON.stringify(sendData));
    xhr.send(JSON.stringify(sendData));

}

function gotoregist() {
    document.getElementById("aaa");window.location.href="register.html"
}
function f() {
    document.getElementById("ccc");window.location.href="login.html"
}
function login() {
    var username=document.getElementById("username").value;
    var password = document.getElementById("password").value;
    console.log("用户输入:", username, password)
    postLogin(username, password);
}