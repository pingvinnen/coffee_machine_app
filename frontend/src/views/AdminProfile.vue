<template>
  <div class="app-container">
    <AppNavbar/>
    <div class="main-content d-flex">
      <SideBar/>
      <div class="row py-5 px-4">
        <div class="col-md-5 mx-auto">
          <!-- Profile widget -->
          <div class="bg-white shadow rounded overflow-hidden">
            <div class="px-4 pt-0 pb-4 cover">
              <div class="media align-items-end profile-head">
                <div class="profile mr-3">
                  <img :src="profilePicture" alt="Profile Picture"  width="130" class="rounded mb-2 img-thumbnail">
                </div>
                <button class="btn btn-primary mt-2 " @click="handleProfileEdit">Edit profile</button>
                <div class="media-body mb-5">
                  <h4 class="mt-0 mb-0"><span>Name: </span>{{ user.name }}</h4>
                  <p class="small mb-4"><span> Position: </span><i
                      class="fas fa-map-marker-alt mr-2"></i> {{ user.position }} </p>
                </div>
              </div>
            </div>

            <div class="px-4 py-3">
              <h5 class="mb-0">About</h5>
              <div class="p-4 rounded shadow-sm bg-light">
                <p class="font-italic mb-0">{{ user.description }}</p>
              </div>
            </div>

          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useRouter } from 'vue-router';
import AppNavbar from "@/components/AppNavbar.vue";
import SideBar from "@/components/SideBar.vue";
import axios from 'axios'
import { ref, onMounted } from 'vue';

export default {
  components: {
    AppNavbar,
    SideBar,
  },
  setup() {
    const user = ref({
      description: " ",
      id: " ",
      name: " ",
      position: " ",
    });
    const profilePicture = ref("");

    const fetchUserProfile = async () => {
      const id = localStorage.getItem('user.id');
      try {
        const response = await axios.get(`http://127.0.0.1:5000/profiles/${id}`);

        if (response.data) {
          user.value.description = response.data.description;
          user.value.id = response.data.id;
          user.value.name = response.data.name;
          user.value.position = response.data.position;

        }
      } catch (error) {
        console.error('There was an error fetching the user profile:', error);
      }
    };

    const fetchProfilePicture = async () => {
      const id = localStorage.getItem('user.id');
      try {
        const response = await axios.get(`http://127.0.0.1:5000/profiles/${id}`);
        // image returned from the server
        if (response.data && response.data.profilePicture) {
          profilePicture.value = 'data:image/jpeg;base64,' + response.data.profilePicture;
        }
      } catch (error) {
        console.error('Error fetching the profile picture:', error);
      }
    };

    const router = useRouter();

    const handleProfileEdit = () => {
      router.push('/profileedit');
    };

    onMounted(async () => {
      await fetchUserProfile();
      await fetchProfilePicture();
    });

    return {
      user,
      profilePicture,
      handleProfileEdit
    };
  },
};
</script>



<style scoped>

body {
  overflow-x: hidden;
}


span {

  font-weight: bold;

}

h5 {
  margin-bottom: 1rem;
  font-weight: bold;


}

p {
  font-weight: normal;

}

.sidebar {
  height: 100vh;
}


.app-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: #f5f5f5;
  overflow-x: hidden;

}

.main-content {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: center;
  width: 100%;
}

.row {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  width: 100%;
}

.col-md-5 {
  max-width: 800px;
  width: 100%;
}

img {
  height: 150px;
  width: 150px;
  border: 3px #CBB26A solid;
  margin-top: 1rem;

}


</style>



