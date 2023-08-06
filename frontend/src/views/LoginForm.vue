
<template>
    <div class="logo">
        <img
                src="../assets/logo2.png"
                alt="Logo"
                width="300"
                height="60"

        />
    </div>
    <div class="wrapper">

        <div class="container">
            <form @submit.prevent="handleSubmit" class="form-signin">
                <h2 class="form-signin-heading">Login</h2>
                <div class="mb-3">
                    <label for="username" class="form-label">Username:</label>
                    <input
                            type="text"
                            class="form-control"
                            name="username"
                            placeholder="Username"
                            required=""
                            autofocus=""
                            v-model="username"
                    />
                </div>
                <div class="mb-3">
                    <label for="password" class="form-label">Password:</label>
                    <input
                            type="password"
                            class="form-control"
                            name="password"
                            placeholder="Password"
                            required=""
                            v-model="password"
                    />
                </div>
                <div class="form-group form-check">
                    <input type="checkbox" class="form-check-input" id="exampleCheck1">
                    <label class="form-check-label" for="exampleCheck1">Remember Me</label>
                </div>
                <button class="btn btn-lg btn-primary btn-block" type="submit" @click.prevent="handleSubmit">Sign in
                </button>
                <div v-if="showWarning" class="alert alert-warning mt-3 " role="alert">
                    {{ warningMessage}}
                </div>

            </form>
        </div>
    </div>
</template>

<script>
import {reactive, ref} from 'vue';
import {useRouter} from 'vue-router';
import axios from 'axios';
import DOMPurify from 'dompurify';

export default {
    setup() {
        const username = ref('');
        const password = ref('');
        const showWarning = ref(false);
        const router = useRouter();
        const warningMessage = ref('');
        const state = reactive({
            loggedIn: false,
        });

        const handleSubmit = async () => {
            const sanitizedUsername = DOMPurify.sanitize(username.value);
            const sanitizedPassword = DOMPurify.sanitize(password.value);

            if (sanitizedUsername === '' || sanitizedPassword === '') {
                showWarning.value = true;
                warningMessage.value = 'Username or password cannot be empty.';
                return;
            }

            if (!/^[a-zA-Z0-9]+$/.test(sanitizedUsername) || !/^[a-zA-Z0-9]+$/.test(sanitizedPassword)) {
                showWarning.value = true;
                warningMessage.value = 'Your username or password contains unwanted characters.';
                return;
            }

            try {
                const response = await axios.post('http://127.0.0.1:5000/authenticate', {
                    username: sanitizedUsername,
                    password: sanitizedPassword,
                });

                if (response.data.result === 'success') {
                    const role = response.data.role;
                    const name = response.data.name;
                    const id = response.data.id;
                    state.loggedIn = true;
                    localStorage.setItem('isLoggedIn', 'true');
                    localStorage.setItem('role', role);
                    localStorage.setItem('name', name);
                    localStorage.setItem('user.id', id);

                    switch (role) {
                        case 'admin':
                            await router.push('/admindashboard');
                            break;
                        case 'user':
                            await router.push('/userdashboard');
                            break;
                        default:
                            await router.push('/error');
                    }
                } else {
                    showWarning.value = true;
                    warningMessage.value = 'Invalid username or password.';
                }
            } catch (error) {
                console.error('There was an error with the authentication:', error);
                showWarning.value = true;
                warningMessage.value = 'There was an error with the authentication.';
            }
        };

        const isAdmin = () => {
            const isLoggedIn = localStorage.getItem('isLoggedIn');
            const role = localStorage.getItem('role');
            return isLoggedIn && role === 'admin';
        };

        return {username, password, handleSubmit, showWarning, warningMessage, isAdmin};
    },
};
</script>


<style scoped>

form {

    width: 500px;
    height: 450px;


}





.form-signin-heading {
    color: #CBB26A;

}

.wrapper {
    margin-top: 180px;
    margin-bottom: 80px;

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

input[type='text'] {
    margin-bottom: -1px;

}

input[type='password'] {
    margin-bottom: 20px;

}

.logo {


}
</style>

