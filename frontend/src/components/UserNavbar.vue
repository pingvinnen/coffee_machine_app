<template>
  <nav class="navbar">
    <div class="container" >
      <a class="navbar-brand" >
        <img
            src="../assets/logo2.png"
            alt="Logo"
            width="300"
            height="60"
            class="d-inline-block align-text-top"
        />
      </a>
      <ul class="nav ms-auto">
        <li>
          <button type="button" class="btn btn-primary">
            Notifications <span class="badge badge-warning">4</span>
          </button>
        </li>
        <li class="nav-item dropdown">

          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown"
             aria-expanded="false">
            <span class="ms-2">{{name }}</span> <i class="bi bi-person"></i>
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
            <li><a class="dropdown-item" href="/userprofile">Profile</a></li>
            <li><a class="dropdown-item" href=" ">News</a></li>
            <li>
              <hr class="dropdown-divider">
            </li>
            <li><a class="dropdown-item" href="#" @click.prevent="logout">Logout</a></li>
          </ul>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
import {reactive} from 'vue';
import {useRouter} from 'vue-router';

export default {
  setup() {
    const router = useRouter();
    const state = reactive({
      loggedIn: false,
    });

    const logout = () => {

      state.loggedIn = false;
      localStorage.removeItem('role');
      localStorage.removeItem('isLoggedIn');
      localStorage.removeItem('name')
      router.push('/');
    };

    return {state, logout};
  },

  created() {
    this.name = localStorage.getItem('name');
    this.isLoggedIn = localStorage.getItem('isLoggedIn') === 'true';
  }

};


</script>

<style scoped>
.container {
  padding-left: 1rem;
  background: #061434

}

nav {
  position: absolute;
  background-color: #424242;
  top: 0;
  width: 100%;
  height: 80px;
  margin: 0;
  padding: 0;

}

. a {
  color: #63B3ED;
}


.navbar {

  background: #061434;


}

nav ul li a {

  color: #63B3ED;
  margin-right:-250px;


}


nav a:hover {
  color: #CBB26A;


}


</style>
