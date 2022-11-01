let count = 0

document.querySelector("#click-btn").addEventListener("click", e => {
    document.querySelector("#clicks").innerHTML = ++count
})