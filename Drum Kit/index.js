function makeSound(key) {
    switch (key) {
        case "w":
            var tom1S = new Audio('sounds/tom-1.mp3');
            tom1S.play();
            break;
        case "a":
            var tom2S = new Audio('sounds/tom-2.mp3')
            tom2S.play();
            break;
        case "s":
            var tom3S = new Audio('sounds/tom-3.mp3');
            tom3S.play();
            break;
        case "d":
            var tom4S = new Audio('sounds/tom-4.mp3')
            tom4S.play();
            break;
        case "j":
            var snare = new Audio('sounds/snare.mp3');
            snare.play();
            break;
        case "k":
            var crash = new Audio('sounds/crash.mp3')
            crash.play();
            break;
        case "l":
            var kick_bass = new Audio('sounds/kick-bass.mp3');
            kick_bass.play();
            break;
        default:
            console.log(whichButtonClickedMouse)
    }
}
function buttonAnimation(currentKey) {
    var activeButton = document.querySelector("." + currentKey);
    activeButton.classList.add("pressed");
    setTimeout(function () {
        activeButton.classList.remove("pressed");
    }, 100)
}
let buttonLength = document.querySelectorAll('.drum').length;
for (let i = 0; i < buttonLength; i++) {
    document.querySelectorAll('.drum')[i].addEventListener('click', function () {
        var whichButtonClickedMouse = this.innerHTML;
        makeSound(whichButtonClickedMouse);
        buttonAnimation(whichButtonClickedMouse);
    })
}
document.addEventListener("keypress", function (event) {
    var whichKeyPressed = event.key;
    makeSound(whichKeyPressed);
    buttonAnimation(whichKeyPressed);
})