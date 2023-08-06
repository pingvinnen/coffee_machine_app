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
                        <label for="id" class="form-label">ID</label>
                        <input type="text" class="form-control" id="id" v-model="id">
                    </div><div v-if="formErrors.id" class="alert alert-warning" role="alert">
                            {{ formErrors.id }}
                        </div>
                    <div class="mb-3" v-if="mode === 'add'">
                        <label for="name" class="form-label">Name</label>
                        <input type="text" class="form-control" id="name" v-model="name">

                    </div><div v-if="formErrors.name" class="alert alert-warning" role="alert">
                            {{ formErrors.name }}
                        </div>
                    <div class="mb-3" v-if="mode === 'add'">
                        <label for="title" class="form-label">Title</label>
                        <select class="form-select" id="title" v-model="title_id">
                            <option value="admin">Admin</option>
                            <option value="technician">Technician</option>
                            <option value="caretaker">Caretaker</option>
                        </select>

                    </div><div v-if="formErrors.title_id" class="alert alert-warning" role="alert">
                            {{ formErrors.title_id }}
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
            mode: 'add',
            id: '',
            name: '',
            title_id: '',
            responseMessage: '',
            isSuccess: null,
            formErrors: {
                id: null,
                name: null,
                title_id: null
            }
        };
    },
    methods: {
        async handleSubmit(event) {
            event.preventDefault();

            this.formErrors.id = this.validateInput('id', this.id, "ID");
            if (this.mode === 'add') {
                this.formErrors.name = this.validateInput('name', this.name, "Name");
                this.formErrors.title_id = !this.title_id ? "Title is required." : null;
            }


            if (!this.formErrors.id && (this.mode === 'delete' || (!this.formErrors.name && !this.formErrors.title_id))) {
                // Prepare the data
                const userData = {
                    id: this.id,
                    name: this.name,
                    title_id: this.title_id
                };


                try {
                    let response;
                    if (this.mode === 'add') {
                        response = await axios.post('http://127.0.0.1:5000/user', userData);
                    } else if (this.mode === 'delete') {
                        response = await axios.delete(`http://127.0.0.1:5000/user/${this.id}`);
                    }

                    console.log(response.data.message);
                    this.responseMessage = response.data.message;
                    this.isSuccess = response.status === 200;
                } catch (error) {
                    this.responseMessage = error.response.data.message;
                    this.isSuccess = false;
                }
            }
        },
        validateInput(field, value, label) {
            if (!value) {
                return `${label} is required.`;
            } else if (!/^[a-z0-9]+$/i.test(value)) {
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
    height: 100vh; /* Adjust as needed */
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



select{
    border-color: #CBB26A;

}

</style>