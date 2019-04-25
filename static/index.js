function renderDogInfo(data) {
  var template = Handlebars.compile(document.getElementById('dogAreaTemplate').innerHTML);
  document.getElementById('dogArea').innerHTML = template(data);
}

document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("dogArea").innerHTML = "loading dogs...";
  fetch("/api/getdogs")
    .then((response) => {
      return response.json();
    })
    .then(renderDogInfo);
});
