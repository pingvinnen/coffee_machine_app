<template>
    <div class="app-container">
        <AppNavbar/>

        <div class="main-content">
            <SideBar/>

            <div class="form-container">
                <form @submit="handleSubmit">
                    <div class="mb-3">
                        <label for="mode" class="form-label">Operation Mode</label>
                        <select class="form-control" id="mode" v-model="mode">
                            <option value="add">Add</option>
                            <option value="delete">Delete</option>
                        </select>
                    </div>
                    <div class="mb-3">
                        <label for="serialNumber" class="form-label">Serial Number</label>
                        <input type="text" class="form-control" id="serialNumber" v-model="id">
                    </div>
                    <div class="mb-3" v-if="mode === 'add'">
                        <label for="model" class="form-label">Model</label>
                        <input type="text" class="form-control" id="model" v-model="model">
                    </div>
                    <div class="mb-3" v-if="mode === 'add'">
                        <label for="location" class="form-label">Location</label>
                        <input type="text" class="form-control" id="location" v-model="location_id">
                    </div>
                    <button type="submit" class="btn btn-primary">Submit</button>
                    <div class="alert alert-warning" role="alert" v-if="formErrors.id">
                        Serial Number is required.
                    </div>
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
            mode: 'add',
            id: '',
            model: '',
            location_id: '',
            coffeeMachines: [],
            responseMessage: '',
            isSuccess: null,
            formErrors: {
                id: false,
                model: false,
                location_id: false
            }
        };
    },
    async mounted() {

        const response = await axios.get('http://127.0.0.1:5000/coffee_machines');
        this.coffeeMachines = response.data.coffee_machines;
    },
    methods: {
        async handleSubmit(event) {
            event.preventDefault();


            this.formErrors.id = !this.id;
            if (this.mode === 'add') {
                this.formErrors.model = !this.model;
                this.formErrors.location_id = !this.location_id;
            }


            if (!this.formErrors.id && (this.mode === 'delete' || (!this.formErrors.model && !this.formErrors.location_id))) {

                const machineData = {
                    id: this.id,
                    model: this.model,
                    location_id: this.location_id
                };


                try {
                    let response;
                    if (this.mode === 'add') {
                        response = await axios.post('http://127.0.0.1:5000/addmachine', machineData);
                    } else if (this.mode === 'delete') {
                        response = await axios.delete(`http://127.0.0.1:5000/deletemachine/${this.id}`);
                    }

                    console.log(response.data.message);
                    this.responseMessage = response.data.message;
                    this.isSuccess = response.status === 200;


                    const refreshResponse = await axios.get('http://127.0.0.1:5000/coffee_machines');
                    this.coffeeMachines = refreshResponse.data.coffee_machines;
                } catch (error) {
                    this.responseMessage = error.response.data.message;
                    this.isSuccess = false;
                }
            }
        },
        confirmDelete() {
            if (window.confirm(`Are you sure you would like to delete the '${this.id}' coffee machine?`)) {
                this.handleSubmit(event);
            }
        }
    }
};
</script>



<style scoped>

form {

    width: 500px;
    height: 450px;
    margin-left: 0px;
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