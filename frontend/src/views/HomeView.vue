<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <h1>{{flask_mess}}</h1>
  </div>
</template>

<script>
const axios = require('axios').default;

export default {

  data(){
    return{
      flask_mess : ''
    }
  },
  created(){
    consol.log('This is create')
    axios.get('https://api-flask-test1.herokuapp.com')
    //axios.get('http://0.0.0.0:5000')
    .then( (res) => this.flask_mess=res.data )
    .catch( (err) => console.log(err) )
  }
}
</script>
