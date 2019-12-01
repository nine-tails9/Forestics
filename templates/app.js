var app = new Vue({
  el: '#app',
  delimiters: ['[[',']]'],     
  data: {
    message: 'Hello Vue!',
    lat: '',
    lng: '',
    images: [],
    name: ''
  },
  methods: {
    addLocation(){
      fetch('http://127.0.0.1:5000/addnew?lat=' + this.lat + '&lng=' + this.lng + '&name=' + this.name);

      this.lat = '';
      this.lng = '';
      this.name = '';

    }
  },
  async created(){
    let res = await fetch('http://127.0.0.1:5000/getpaths');
    this.images = await res.json();
  }
})