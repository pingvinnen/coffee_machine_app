<template>

    <div class="sidebar">
        <nav class="nav flex-column">
            <router-link class="nav-link d-flex align-items-center" to="/admindashboard">
                <i class="bi bi-house-fill"></i>
                <span class="ms-2">Home</span>
            </router-link>
            <router-link class="nav-link d-flex align-items-center" to="/reports">
                <i class="bi bi-file-bar-graph-fill"></i>
                <span class="ms-2">Reports</span>
            </router-link>
            <router-link class="nav-link d-flex align-items-center" to="/messages">
                <i class="bi bi-bell-fill"></i>
                <span class="ms-2">Notifications</span>
            </router-link>

            <div class="dropdown d-flex align-items-center">
                <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton2"
                        data-bs-toggle="dropdown" aria-expanded="false">
                    <i class="bi bi-people-fill"></i> <span class="ms-2">Manage Users</span>
                </button>
                <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton2">
                    <li><a class="dropdown-item" href="/addremoveemployee">Add User</a></li>
                    <li><a class="dropdown-item" href="/addremoveemployee">Delete User</a></li>
                    <li><a class="dropdown-item" href="/updateemployee">Update User</a></li>
                    <li><a class="dropdown-item" href="/employees">List Staff</a></li>
                </ul>
            </div>
            <div class="dropdown d-flex align-items-center">
                <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton1"
                        data-bs-toggle="dropdown" aria-expanded="false">
                    <i class="bi bi-gear-fill"></i> <span class="ms-2">Manage Machines</span>
                </button>
                <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                    <li><a class="dropdown-item" href="/removeaddmachine">Delete Machine</a></li>
                    <li><a class="dropdown-item" href="#">Add Machine</a></li>
                    <li><a class="dropdown-item" href="/editmachines">Update Machine</a></li>
                </ul>

            </div>

        </nav>
    </div>
</template>

<script>
export default {
    name: 'SideBar',
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

span{
    color: #63B3ED;

}
</style>
