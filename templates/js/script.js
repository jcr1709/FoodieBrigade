let searchButton = document.querySelector("#search");
let indianButton = document.querySelector("#indian");





//Add an event listener to the button that runs the function sendApiRequest when it is clicked
searchButton.addEventListener("click", () => {
  console.log("button pressed");
  sendApiRequest();
});

indianButton.addEventListener("click", () => {
  console.log("button pressed");
  requestIndia();
});

async function requestIndia() {
  let APP_ID = "9b4b97e4";
  let APP_KEY = "31f7927645b3ee71c5bf4afe34059488";
  let cuisine = document.getElementById("indian").value;
  let response = await fetch(
    `https://api.edamam.com/search?app_id=${APP_ID}&app_key=${APP_KEY}&q=${cuisine}`
  );
  console.log(response);
  let data = await response.json();
  console.log(data);
  useApiDataIndian(data);
}

//An asynchronous function to fetch data from the API.
async function sendApiRequest() {
  let APP_ID = "9b4b97e4";
  let APP_KEY = "31f7927645b3ee71c5bf4afe34059488";
  var user = document.getElementById("user_input").value;
  let response = await fetch(
    `https://api.edamam.com/search?app_id=${APP_ID}&app_key=${APP_KEY}&q=${user}`
  );
  console.log(response);
  let data = await response.json();
  console.log(data);
  useApiData(data);
}

//function that does something with the data received from the API. The name of the function should be customized to whatever you are doing with the data
function useApiData(data) {
  document.querySelector("#content").innerHTML = `
  <div class="row row-cols-1 row-cols-md-3 g-4">
  <div class="col">
    <div class="card h-90">
      <img src="${data.hits[0].recipe.image}" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">${data.hits[0].recipe.label}</h5>
        <p class="card-text">Cuisine: <span style="text-transform:uppercase">${data.hits[0].recipe.cuisineType}<br>
        </span>Dish Type: <span style="text-transform:uppercase">${data.hits[0].recipe.dishType}</span><br>
        Calories: <span style="text-transform:uppercase">${data.hits[0].recipe.calories}</span><br>
        Diet Labels: <br><span style="text-transform:uppercase">${data.hits[0].recipe.dietLabels}</span><br>
        </p><center>
        <a href="${data.hits[0].recipe.url}" class="btn btn-primary">Click For Full Recipe</a></center>
        </div>
    </div>
  </div>
  <div class="col">
    <div class="card h-90">
    <img src="${data.hits[1].recipe.image}" class="card-img-top" alt="...">
    <div class="card-body">
      <h5 class="card-title">${data.hits[1].recipe.label}</h5>
      <p class="card-text">Cuisine: <span style="text-transform:uppercase">${data.hits[1].recipe.cuisineType}</span><br>
      Dish Type: <span style="text-transform:uppercase">${data.hits[1].recipe.dishType}</span><br>
      Calories: <span style="text-transform:uppercase">${data.hits[1].recipe.calories}</span><br>
      Diet Labels: <br><span style="text-transform:uppercase">${data.hits[1].recipe.dietLabels}</span><br>
      </p><center>
      <a href="${data.hits[1].recipe.url}" class="btn btn-primary">Click For Full Recipe</a></center>
    </div>
  </div>
  </div>
  <div class="col">
    <div class="card h-90">
    <img src="${data.hits[2].recipe.image}" class="card-img-top" alt="...">
    <div class="card-body">
      <h5 class="card-title">${data.hits[2].recipe.label}</h5>
      <p class="card-text">Cuisine: <span style="text-transform:uppercase">${data.hits[2].recipe.cuisineType}<br>
      </span>Dish Type: <span style="text-transform:uppercase">${data.hits[2].recipe.dishType}</span><br>
      Calories: <span style="text-transform:uppercase">${data.hits[2].recipe.calories}</span><br>
      Diet Labels: <br><span style="text-transform:uppercase">${data.hits[2].recipe.dietLabels}</span><br>
      </p><center>
      <a href="${data.hits[2].recipe.url}" class="btn btn-primary">Click For Full Recipe</a></center>
    </div>
  </div>
</div>
<div class="col">
<div class="card h-90">
<img src="${data.hits[3].recipe.image}" class="card-img-top" alt="...">
<div class="card-body">
  <h5 class="card-title">${data.hits[3].recipe.label}</h5>
  <p class="card-text">Cuisine: <span style="text-transform:uppercase">${data.hits[3].recipe.cuisineType}<br>
  </span>Dish Type: <span style="text-transform:uppercase">${data.hits[3].recipe.dishType}</span><br>
  Calories: <span style="text-transform:uppercase">${data.hits[3].recipe.calories}</span><br>
  Diet Labels: <br><span style="text-transform:uppercase">${data.hits[3].recipe.dietLabels}</span><br>
  </p><center>
  <a href="${data.hits[3].recipe.url}" class="btn btn-primary">Click For Full Recipe</a></center>
</div>
</div>
</div>

    `;
}

//indian cuisine

function useApiDataIndian(data) {
  document.querySelector("#content").innerHTML = `
<div class="row row-cols-1 row-cols-md-3 g-4">
<div class="col">
  <div class="card h-90">
    <img src="${data.hits[0].recipe.image}" class="card-img-top" alt="...">
    <div class="card-body">
      <h5 class="card-title">${data.hits[0].recipe.label}</h5>
      <p class="card-text">Cuisine: <span style="text-transform:uppercase">${data.hits[0].recipe.cuisineType}<br>
      </span>Dish Type: <span style="text-transform:uppercase">${data.hits[0].recipe.dishType}</span><br>
      Calories: <span style="text-transform:uppercase">${data.hits[0].recipe.calories}</span><br>
      Diet Labels: <br><span style="text-transform:uppercase">${data.hits[0].recipe.dietLabels}</span><br>
      </p><center>
      <a href="${data.hits[0].recipe.url}" class="btn btn-primary">Click For Full Recipe</a></center>
      </div>
  </div>
</div>
<div class="col">
  <div class="card h-90">
  <img src="${data.hits[1].recipe.image}" class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">${data.hits[1].recipe.label}</h5>
    <p class="card-text">Cuisine: <span style="text-transform:uppercase">${data.hits[1].recipe.cuisineType}</span><br>
    Dish Type: <span style="text-transform:uppercase">${data.hits[1].recipe.dishType}</span><br>
    Calories: <span style="text-transform:uppercase">${data.hits[1].recipe.calories}</span><br>
    Diet Labels: <br><span style="text-transform:uppercase">${data.hits[1].recipe.dietLabels}</span><br>
    </p><center>
    <a href="${data.hits[1].recipe.url}" class="btn btn-primary">Click For Full Recipe</a></center>
  </div>
</div>
</div>
<div class="col">
  <div class="card h-90">
  <img src="${data.hits[2].recipe.image}" class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">${data.hits[1].recipe.label}</h5>
    <p class="card-text">Cuisine: <span style="text-transform:uppercase">${data.hits[2].recipe.cuisineType}<br>
    </span>Dish Type: <span style="text-transform:uppercase">${data.hits[2].recipe.dishType}</span><br>
    Calories: <span style="text-transform:uppercase">${data.hits[2].recipe.calories}</span><br>
    Diet Labels: <br><span style="text-transform:uppercase">${data.hits[2].recipe.dietLabels}</span><br>
    </p><center>
    <a href="${data.hits[2].recipe.url}" class="btn btn-primary">Click For Full Recipe</a></center>
  </div>
</div>
</div>
<div class="col">
<div class="card h-90">
<img src="${data.hits[3].recipe.image}" class="card-img-top" alt="...">
<div class="card-body">
<h5 class="card-title">${data.hits[1].recipe.label}</h5>
<p class="card-text">Cuisine: <span style="text-transform:uppercase">${data.hits[3].recipe.cuisineType}<br>
</span>Dish Type: <span style="text-transform:uppercase">${data.hits[3].recipe.dishType}</span><br>
Calories: <span style="text-transform:uppercase">${data.hits[3].recipe.calories}</span><br>
Diet Labels: <br><span style="text-transform:uppercase">${data.hits[3].recipe.dietLabels}</span><br>
</p><center>
<a href="${data.hits[3].recipe.url}" class="btn btn-primary">Click For Full Recipe</a></center>
</div>
</div>
</div>

  `;
}
