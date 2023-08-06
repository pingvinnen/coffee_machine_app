<template>
    <div class="sidebar">
        <nav class="nav flex-column">
            <router-link class="nav-link d-flex align-items-center" to="/userdashboard">
                <i class="bi bi-house"></i>
                <span class="ms-2">Home</span>
            </router-link>
            <router-link class="nav-link d-flex align-items-center" to="/usermessages">
                <i class="bi bi-cup-hot"></i>
                <span class="ms-2">Messages</span>
            </router-link>
        </nav>
    </div>
</template>

<script>
export default {
    name: 'UserSidebar',
};
</script>

<style scoped>
.sidebar {
    background-color: #061434;
    min-height: 10vh;
    padding: 1rem;

}

.sidebar .nav-link {
    color: #ffffff;
    transition: 0.2s;
}

.sidebar .nav-link:hover {
    color: #cccccc;
    background-color: rgba(255, 255, 255, 0.1);
}

.sidebar .nav-link .bi {
    margin-right: 1rem;
}

.btn {
    background-color: #061434 !important;
    border-color: #061434 !important;
    color: #63B3ED;
}

i {
    color: #63B3ED;
}

span {
    color: #63B3ED;

}
</style>
