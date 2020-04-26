function postRegist(argUserName, argUserPass) {
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
            //CLOSE Popup
            //根据服务器的响应内容格式处理响应结果
            if (xhr.getResponseHeader('content-type') === 'application/json') {
                console.log(xhr.responseText);
                var resultJSON = JSON.parse(xhr.responseText);
                if (resultJSON.errorcode === 0) {
                    alert("注册成功!"); //返回登录界面
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
function regist(){
    var username=document.getElementById("username").value;
    var password=document.getElementById("password").value;
    var password2=document.getElementById("confirm_password").value;
    var regx =/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^]{8,16}$/;
    console.log("用户输入:", username, password)
    if(password.length<20&&password.length>5&&password===password2)
    {postRegist(username, password);}
    if(password.length>20){alert("密码必须小于20位")}
    if(password.length<=5){alert("密码必须大于5位")}
    if(password.length<20&&password.length>5&&password!=password2){alert("两次输入密码不一致")}
    if(password.match(regx)==null){alert("密码格式不正确！");
        return;}


}

function myFunction2() {
    document.getElementById("bbb");window.location.href="login.html";
}