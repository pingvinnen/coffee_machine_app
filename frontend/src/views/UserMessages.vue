<template>


  <div class="app-container">
    <AppNavbar/>
    <div class="row">
      <div class="col-3">
        <UserSidebar/>
      </div>
      <div class="col-2">
        <div class="container">
          <div>
            <div v-for="(notification, index) in notifications" :key="index" class="alert alert-primary">
              <p class="mb-0" >{{ notification.message }}</p>
              <button @click="deleteNotification(index)" class="btn btn-sm btn-primary ml-3">Dismiss</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import AppNavbar from "@/components/AppNavbar.vue";
import UserSidebar from "@/components/UserSidebar.vue";

export default {
  components: {UserSidebar, AppNavbar},
  data() {
    return {
      notifications: [
        {message: 'Machine 2019125 is down'},
        {message: 'Machine 20214578 needs maintenance'},
        {message: 'New coffee beans have arrived'},
        {message: 'Monthly report is available'}
      ]
    }
  },
  methods: {
    deleteNotification(index) {
      this.notifications.splice(index, 1)
    }
  }
}
</script>

<style scoped>

.app-container {
    overflow-x: hidden;
}


.container {
  margin-top: 100px;
  margin-left:0px
}
.sidebar {
    height: 100vh;
    width:250px;
}


.notification {
  border: 1px solid #CBB26A;
  margin-bottom: 10px;
  padding: 10px;
  position: relative;
}

.notification button {
  position: absolute;
  top: 15px;
  right: 10px;
}

p {



}
</style>