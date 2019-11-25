var app = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue!'
  },
  async created(){
    let url = "https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static/93.1673,26.5889,15/800x600?access_token=pk.eyJ1IjoibmluZS10YWlsczkiLCJhIjoiY2szYnVkN200MHB0MDNwczEzdnpzdXUwZSJ9.y_Kl7N0k9MjGx6HI1YNITw"
    fetch(url)
  .then(res=>{return res.blob()})
  .then(blob=>{
    var img = URL.createObjectURL(blob);
      document.getElementById('img').setAttribute('src', img);
  })
  }
})