const localhostURL = 'ws://127.0.0.1:8765';
const timers = [];
//const jqueryDom = createDanmaku('hihihi'); // test danmaku, delete it as you like
//addInterval(jqueryDom);// test danmaku, delete it as you like

// TODO: construct websocket for communication
let socket = null;
socket = singletonSocket();

/**
 * 单例模式的WebSocket连接，避免重复构造连接浪费资源。
 * @returns {null|WebSocket}
 */

function singletonSocket() {
    if (socket == null) {
        socket = new WebSocket(localhostURL);
        socket.onmessage = function (messageEvent) {
            let dm = createDanmaku(messageEvent.data);
            addInterval(dm);
        }
        return socket;
    }
    return socket;
}

$(".send").on("click", function () {
    let data = document.getElementById("danmakutext").value;
    if (data.length === 0) {
        data = 'Danmaku~'
    }
    socket = singletonSocket();
    let color = document.getElementById('colorSelection').value;
    //console.log(document.getElementsByName('color')[0].value+'|||'+data)
    let fontSize = document.getElementById("fontSizeSelection")
    let index = fontSize.selectedIndex
    if (index === undefined) {
        index = 0;
    }
    // console.log(index)

    fontSize = fontSize.options[index].value;

    socket.send(color + '|||' + fontSize + '|||' + data);
});

/**
 * 此处同HTTP版本的createDanmaku
 * @param text
 * @returns {*|jQuery|HTMLElement}
 */

// create a Dom object corresponding to a danmaku
function createDanmaku(text) {

    const splited = text.split('|||')
    const font = splited[1]
    const jqueryDom = $("<div class='bullet'>" + splited[2] + "</div>");
    const fontColor = splited[0];
    const fontSize = font === 'Large' ? "20px" : "15px";
    let top = Math.floor(Math.random() * 400) + "px";
    const left = $(".screen_container").width() + "px";
    jqueryDom.css({
        "position": 'absolute',
        "color": fontColor,
        "font-size": fontSize,
        "left": left,
        "top": top,
    });
    $(".screen_container").append(jqueryDom);
    return jqueryDom;
}

// add timer task to let the danmaku fly from right to left
function addInterval(jqueryDom) {
    let left = jqueryDom.offset().left - $(".screen_container").offset().left;
    const timer = setInterval(function () {
        left--;
        jqueryDom.css("left", left + "px");
        if (jqueryDom.offset().left + jqueryDom.width() < $(".screen_container").offset().left) {
            jqueryDom.remove();
            clearInterval(timer);
        }
    }, 5); // set delay as 5ms,which means the danmaku changes its position every 5ms
    timers.push(timer);
}