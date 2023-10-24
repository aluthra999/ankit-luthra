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
