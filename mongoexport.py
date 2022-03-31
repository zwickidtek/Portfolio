let url = 'https://api.sheety.co/1dd8818803e588fc51a17ec92c66018b/copyOfAlgorithmDemo/collegeData';
fetch(url)
.then((response) => response.json())
.then(json => {
  // Do something with the data
  console.log(json.collegeData);
});