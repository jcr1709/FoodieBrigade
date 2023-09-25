async function alertbox(element){
    let APP_ID = "9b4b97e4";
    let APP_KEY = "31f7927645b3ee71c5bf4afe34059488";
    let pamu = element;
    let response = await fetch(
    `https://api.edamam.com/search?app_id=${APP_ID}&app_key=${APP_KEY}&q=${pamu}`
  );
  console.log(response);
  let data = await response.json();
  console.log(data);
  useApiData(data);
}

function useApiData(data) {
    document.querySelector("#content").innerHTML = `
    <div class="container">
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
    </div></div>
    `;
}