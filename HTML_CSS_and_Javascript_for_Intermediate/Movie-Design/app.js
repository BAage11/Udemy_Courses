
// -------------------------- SLIDER --------------------------

const arrows = document.querySelectorAll(".arrow");
const movieLists = document.querySelectorAll(".movie-list");

arrows.forEach((arrow, i) => {
    // Check if user is at the end of movielist
    const itemNum = movieLists[i].querySelectorAll("img").length;
    let clickCounter = 0;

    arrow.addEventListener("click", () => {
        // Get the width of the browser, to have the window responsive
        const ratio = Math.floor(window.innerWidth / 270);

         clickCounter++;
        if(itemNum - (5 + clickCounter) + (5 - ratio) >= 0) {
            movieLists[i].style.transform = `translateX(${
                movieLists[i].computedStyleMap().get("transform")[0].x.value-300}px)`;            
        } else {
            // Move to the beginning of movielist, when end is reached
            movieLists[i].style.transform = "translateX(0)";
            clickCounter = 0;
        }
    });
});




// -------------------------- TOGGLE --------------------------

const ball = document.querySelector(".toggle-ball");
const items = document.querySelectorAll(".container, .movie-list-title, .navbar-container, .sidebar, .left-menu-icon, .toggle")

// Change from light mode, to dark mode (and vice versa)
ball.addEventListener("click", () => {
    items.forEach(item => {
        item.classList.toggle("active");
    })
    ball.classList.toggle("active");
})





// Back tick on keyboard: Alt + 96
