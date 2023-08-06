<template>
    <div class="logo">
      <img
          src="../assets/logo2.png"
          alt="Logo"
          width="300"
          height="60"

        />
  </div>


<div>
    <h1> 404 Error</h1>
    <p>The Page You Are Trying to Visit Does Not Exist</p>
    <router-link to="/LoginForm">Back to Home </router-link>
  </div>
</template>

<script>
export default {
    name: "ErrorPage"
}
</script>

<style scoped>
h1 {
    font-family: "Open Sans", sans-serif;

 }
p{

   font-family: "Open Sans", sans-serif;
   font-size: 1.5em;

}


</style>