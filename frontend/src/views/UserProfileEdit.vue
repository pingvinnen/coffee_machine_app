<template>

  <head>

    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" rel="stylesheet">
  </head>
  <div class="app-container">
    <UserNavbar/>
    <div class="main-content d-flex">
      <UserSidebar/>
      <div class="col-md-4 mx-auto profile-edit-container">
        <div class="bg-white shadow rounded overflow-hidden">
          <div class="px-4 pt-0 pb-4 cover">
            <div class="media align-items-end profile-head">
              <div class="container">
                <h2 class="form-signin-heading">Edit Profile</h2>
                <form @submit.prevent="submitForm">
                  <input type="hidden" v-model="userId">
                  <div class="row">
                    <!-- Name and Position inputs  -->
                    <div class="col-12 form-group">
                      <label for="profile-name"> <span>Name</span></label>
                      <input type="text" class="form-control" id="profile-name" v-model="name" placeholder="Enter name">
                    </div>
                    <div class="col-12 form-group">
                      <label for="profile-position"><span> Position </span> </label>
                      <input type="text" class="form-control" id="profile-position" v-model="position "
                             placeholder="Enter position">
                    </div>
                    <!-- Profile Picture Upload-->
                    <div class="col-12">
                      <div class="profile mr-3  ">
                        <input type="file" id="profilePicture" class="rounded mb-2 img-thumbnail"
                               v-on:change="handleFileUpload"/>
                      </div>
                    </div>

                    <!-- Text Area -->

                    <div class="col-12">
                      <label for="comments"> <span> About </span></label>
                      <div class="media-body mb-5 text-white">
                        <textarea class="form-control" id="comments" rows="5" v-model="description"></textarea>
                      </div>
                      <!-- Save Button -->
                      <div class="col-12">
                        <button type="submit" class="btn btn-primary btn-sm ">Save Changes</button>
                      </div>
                      <div v-if="error" class="alert alert-danger" role="alert">
                        {{ errorMessage }}
                      </div>
                      <div v-if="!error && errorMessage" class="alert alert-success" role="alert">
                        {{ errorMessage }}
                      </div>
                    </div>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import UserNavbar from "@/components/UserNavbar.vue";
import UserSidebar from "@/components/UserSidebar.vue";
import axios from 'axios';
import {onMounted, ref} from "vue";

export default {
  components: {
    UserNavbar,
    UserSidebar,
  },
  setup() {
    const profilePicture = ref(null);
    const description = ref("");
    const name = ref("");
    const position = ref("");
    const error = ref(false);
    const errorMessage = ref("");
    const id = ref(localStorage.getItem('user.id'));

    const fetchUserProfile = async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:5000/adminprofile/${id.value}`);
        if (response.status === 200 && response.data && response.data.imagePath) {
          profilePicture.value = require(`@/assets/${response.data.imagePath}`);
        }
      } catch (error) {
        console.error('Error fetching the user profile:', error);
      }
    };

    onMounted(fetchUserProfile);

    const handleFileUpload = async (event) => {
      let selectedFile = event.target.files[0];
      if (selectedFile && ['image/jpeg', 'image/png'].includes(selectedFile.type) && selectedFile.size <= 8000000) {
        let reader = new FileReader();
        reader.onloadend = async () => {
          profilePicture.value = reader.result.split(",")[1];

          // upload file to the server
          const formData = new FormData();
          formData.append('file', selectedFile);
          await axios.post('http://127.0.0.1:5000/upload', formData, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          });
        };
        reader.readAsDataURL(selectedFile);
        error.value = false;
      } else {
        error.value = true;
        if (selectedFile.size > 8000000) {
          errorMessage.value = 'File size exceeds limit of 8MB';
        } else {
          errorMessage.value = 'Invalid file type. Please select a JPEG or PNG file';
        }
      }
    };


    const submitForm = async () => {
      try {
        if (!/^[a-z0-9]+$/i.test(name.value) || !/^[a-z0-9]+$/i.test(position.value)) {
          error.value = true;
          errorMessage.value = 'Name and position should only contain alphanumeric characters.';
          return;
        }


        const response = await axios.post('http://127.0.0.1:5000/profileedit', {
          id: id.value,
          profilePicture: profilePicture.value,
          description: description.value,
          position: position.value,
          name: name.value
        });
        if (response.status === 200) {
          error.value = false;
          errorMessage.value = 'Profile updated successfully';

          profilePicture.value = null;
          description.value = "";
          name.value = "";
          position.value = "";
        } else {
          error.value = true;
          errorMessage.value = 'Failed to update profile';
        }
      } catch (error) {
        console.error(error);
        error.value = true;
        errorMessage.value = 'An error occurred while updating the profile';
      }
    };

    return {
      profilePicture, description, name, position,
      handleFileUpload, submitForm,
      error, errorMessage, id
    };
  },
};
</script>


<style scoped>


.app-container, h1, h2, h3, h4, h5, h6 {
  font-family: Arial, Helvetica, sans-serif;
}

.profile {

  margin-top: inherit;


}

label {

  text-align: left;
  display: block;


}

.bg-white {

  margin-top: 5px;
  height: inherit;


}

.col-12 {

  margin-bottom: 10px;

}

span {

  font-weight: bold;

}


.sidebar {
  height: 100vh;
}

.profile-edit-container {

  width: 700px;
  height: 700px;
  box-sizing: border-box;
  font-size: 1rem;
  margin: 80px auto;
}

.form-control {
  border-color: #CBB26A;


}

.form-signin-heading {
  margin-top: 20px;


}
</style>
