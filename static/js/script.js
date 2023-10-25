const words = ["fast", "potential", "audience"];
let index = 0;
let letterIndex = 0;
let currentWord = "";
let isDeleting = false;

const typewriter = document.getElementById("typewriter");

function typeWords() {
  const speed = Math.random() * (100 - 50) + 50;

  if (isDeleting) {
    currentWord = words[index].substring(0, letterIndex - 1);
    letterIndex--;
  } else {
    currentWord = words[index].substring(0, letterIndex + 1);
    letterIndex++;
  }

  typewriter.innerHTML = currentWord;

  // Check the screen width
  const screenWidth = window.innerWidth;

  if (screenWidth <= 768) {
    // Adjust this value as needed
    typewriter.innerHTML += "<br>"; // Add a line break if the screen is smaller
  }

  if (!isDeleting && letterIndex === words[index].length) {
    isDeleting = true;
    setTimeout(() => {
      typeWords();
    }, 2000);
  } else if (isDeleting && letterIndex === 0) {
    isDeleting = false;
    index++;
    if (index === words.length) {
      index = 0;
    }
    setTimeout(() => {
      typeWords();
    }, 500);
  } else {
    setTimeout(() => {
      typeWords();
    }, speed);
  }
}

typeWords();

const about_typewriter_words = ["r brand", "r business"];
let aboutIndex = 0;
let aboutLetterIndex = 0;
let aboutCurrentWord = false;

const about_typewriter = document.getElementById("about_typewriter");

function typeAboutWords() {
  const speed = Math.random() * (100 - 50) + 50;

  if (isDeleting) {
    aboutCurrentWord = about_typewriter_words[aboutIndex].substring(
      0,
      aboutLetterIndex - 1
    );
    aboutLetterIndex--;
  } else {
    aboutCurrentWord = about_typewriter_words[aboutIndex].substring(
      0,
      aboutLetterIndex + 1
    );
    aboutLetterIndex++;
  }

  about_typewriter.innerHTML = aboutCurrentWord;

  if (
    !isDeleting &&
    aboutLetterIndex === about_typewriter_words[aboutIndex].length
  ) {
    isDeleting = true;
    setTimeout(() => {
      typeAboutWords();
    }, 3000);
  } else if (isDeleting && aboutLetterIndex === 0) {
    isDeleting = false;
    aboutIndex++;
    if (aboutIndex === about_typewriter_words.length) {
      aboutIndex = 0;
    }
    setTimeout(() => {
      typeAboutWords();
    }, 500);
  } else {
    setTimeout(() => {
      typeAboutWords();
    }, speed);
  }
}

typeAboutWords();

//Get the button
let mybutton = document.getElementById("btn-back-to-top");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () {
  scrollFunction();
};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}
// When the user clicks on the button, scroll to the top of the document
mybutton.addEventListener("click", backToTop);

function backToTop() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}
