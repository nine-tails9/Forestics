var app = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue!',
    lat: '',
    lng: '',
    images: []
  },
  methods: {
    addLocation(){
      fetch('http://127.0.0.1:5000/addnew?lat=' + this.lat + '&lng=' + this.lng);
      this.lat = '';
      this.lng = '';

    }
  },
  async created(){
    let res = await fetch('http://127.0.0.1:5000/getpaths');
    this.images = await res.json();
  }
})