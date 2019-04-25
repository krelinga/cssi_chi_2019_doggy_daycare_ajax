document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("dogArea").innerHTML = "loading dogs...";
  fetch("/api/getdogs")
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      document.getElementById('dogArea').innerHTML = data.dogs;
    });
});
