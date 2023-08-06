<template>
    <div class="app-container">
        <AppNavbar/>

        <div class="main-content">
            <SideBar/>

            <div class="form-container">
                <form @submit="handleSubmit">
                    <div class="mb-3">
                        <label for="serialNumber" class="form-label">Serial Number</label>
                        <input type="text" class="form-control" id="serialNumber" v-model="id" placeholder="numeric only" >

                    </div><div v-if="formErrors.id" class="alert alert-warning" role="alert">
                            {{ formErrors.id }}
                        </div>
                    <div class="mb-3">
                        <label for="model" class="form-label">Model</label>
                        <input type="text" class="form-control" id="model" v-model="model" placeholder="alphanumeric only">

                    </div><div v-if="formErrors.model" class="alert alert-warning" role="alert">
                            {{ formErrors.model }}
                        </div>
                    <div class="mb-3">
                        <label for="location" class="form-label">Location</label>
                        <input type="text" class="form-control" id="location" v-model="location_id" placeholder="numeric only">

                    </div> <div v-if="formErrors.location_id" class="alert alert-warning" role="alert">
                            {{ formErrors.location_id }}
                        </div>
                    <button type="submit" class="btn btn-primary">Submit</button>
                    <div class="alert" v-if="responseMessage" :class="isSuccess ? 'alert-success' : 'alert-danger'"
                         role="alert">
                        {{ responseMessage }}
                    </div>
                </form>
            </div>
        </div>
    </div>

</template>
<script>
import axios from 'axios';
import AppNavbar from "@/components/AppNavbar.vue";
import SideBar from "@/components/SideBar.vue";


export default {
    components: {SideBar, AppNavbar},
    data() {
        return {
            id: '',
            model: '',
            location_id: '',
            responseMessage: '',
            isSuccess: null,
            formErrors: {
                id: null,
                model: null,
                location_id: null
            }
        };
    },
    methods: {
        async handleSubmit(event) {
            event.preventDefault();

            this.formErrors.id = this.validateInput('id', this.id, "Serial Number");
            this.formErrors.model = this.validateInput('model', this.model, "Model");
            this.formErrors.location_id = this.validateInput('location_id', this.location_id, "Location");

            if (!this.formErrors.id && !this.formErrors.model && !this.formErrors.location_id) {

                const machineData = {
                    id: this.id,
                    model: this.model,
                    location_id: this.location_id
                };

                try {
                    const response = await axios.post('http://127.0.0.1:5000/editmachines', machineData);
                    console.log(response.data.message);
                    this.responseMessage = response.data.message;
                    this.isSuccess = response.status === 200;
                } catch (error) {
                    this.responseMessage = error.response.data.message;
                    this.isSuccess = false;
                }
            }
        },
        validateInput(fieldName, value, label) {
            if (!value) {
                return `${label} is required.`;
            } else if (fieldName !== 'location_id' && !/^[a-zA-Z0-9]+$/.test(value)) {
                return `${label} can only contain alphanumeric characters.`;
            } else {
                return null;
            }
        }
    }

};
</script>



<style scoped>

form {

    width: 500px;
    height: 450px;
    margin-left: 0;
    margin-top: 10px;


}

.container {
    margin-top: 2px;
    margin-left: 400px;
}

.sidebar {

    margin-top: 20px;

}

.form-signin-heading {
    color: #CBB26A;

}

.wrapper {

    margin-left: 400px;
    background-color: #1b8dbb;
    width: 800px;


}

.form-label {
    float: left;
    margin-right: 1em;
    color: #CBB26A;

}


.form-check-label {
    float: left;


}

.form-check-label {
    color: #CBB26A;


}

.form-signin {
    max-width: 480px;
    padding: 15px 35px 45px;
    margin: 0 auto;
    background-color: #fff;
    border: 1px solid rgba(0, 0, 0, 0.1);
}

.form-signin-heading,
.checkbox {
    margin-bottom: 30px;
}

.checkbox {
    font-weight: normal;
}

.form-control {
    position: relative;
    font-size: 16px;
    height: auto;
    padding: 10px;
    box-sizing: border-box;
    border-color: #CBB26A;
}

.form-control:focus {
    z-index: 2;
}

input[type='serialNumber '] {
    margin-bottom: -1px;

}

input[type='model'] {
    margin-bottom: 20px;

}

input[type='location'] {
    margin-bottom: 20px;

}





.app-container {
    display: flex;
    flex-direction: column;
    height: 100vh;
}

.main-content {
    display: flex;
    flex-grow: 1;
}



.form-container {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-grow: 1;
}




</style>